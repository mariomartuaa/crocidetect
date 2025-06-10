import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.cm as cm
from tensorflow.keras.applications.inception_v3 import preprocess_input as inception_preprocess
from io import BytesIO
from utils.db import insert_prediction, upload_image_to_storage
import uuid

class_names = ['Instar 1', 'Instar 2', 'Instar 3', 'Instar 4']

def get_user_id():
    cookies = EncryptedCookieManager(prefix="crocidetect_", password=st.secrets["COOKIE_SECRET"])
    if not cookies.ready():
        st.stop()

    user_id = cookies.get("user_id")
    
    if user_id is None:
        user_id = cookies.get("ajs_anonymous_id")
    
    return user_id

@st.cache_resource
def load_inception_model():
    return tf.keras.models.load_model("model/InceptionV32_model.keras")

def preprocess_image_inception(image):
    image = image.resize((512, 512))
    image_array = np.array(image)[..., :3]  # otomatis hilangkan alpha jika ada
    image_array = np.expand_dims(image_array, axis=0)
    return inception_preprocess(image_array)


def predict_instar(model, image):
    img_array = preprocess_image_inception(image)
    predictions = model.predict(img_array)[0]
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100
    
    df_confidence = pd.DataFrame({
        'Tahap Instar': class_names,
        'Akurasi (%)': predictions * 100
    })
    return predicted_class, confidence, df_confidence


def make_gradcam_heatmap(image, model, last_conv_layer_name):
    img_array = preprocess_image_inception(image)
    
    grad_model = tf.keras.models.Model(
        model.inputs, 
        [model.get_layer(last_conv_layer_name).output, model.output]
    )


    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    # Gradients terhadap output feature map
    grads = tape.gradient(class_channel, conv_outputs)

    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]

    heatmap = tf.reduce_sum(conv_outputs * pooled_grads, axis=-1)

    # Normalisasi heatmap
    heatmap = tf.maximum(heatmap, 0) / tf.reduce_max(heatmap)
    heatmap = heatmap.numpy()
    
    grad_cam = superimpose_heatmap(image, heatmap)
    return grad_cam

def superimpose_heatmap(image, heatmap, alpha=0.4):
    image = image.convert("RGB")
    image_array = np.array(image)

    # Resize dan ubah heatmap ke uint8
    heatmap = np.uint8(255 * heatmap)
    heatmap_resized = Image.fromarray(heatmap).resize(
        (image_array.shape[1], image_array.shape[0]), Image.BILINEAR
    )
    heatmap_resized = np.array(heatmap_resized)

    # Apply colormap
    heatmap_color = np.uint8(cm.jet(heatmap_resized / 255.0)[..., :3] * 255)

    # Blend heatmap dengan gambar asli
    superimposed = np.uint8((1 - alpha) * image_array + alpha * heatmap_color)

    # Kembalikan dalam format PIL.Image
    return Image.fromarray(superimposed)

def insert_database(user_id, image, superimposed_img_inception, predicted_class_inception, df_confidence):
    unique_id = str(uuid.uuid4())

    original_img_bytes = BytesIO()
    image.save(original_img_bytes, format='PNG')
    original_img_bytes = original_img_bytes.getvalue()
    
    gradcam_img_bytes = BytesIO()
    superimposed_img_inception.save(gradcam_img_bytes, format="PNG")
    gradcam_img_bytes =  gradcam_img_bytes.getvalue()


    # Upload ke Supabase Storage
    original_img_url = upload_image_to_storage(original_img_bytes, f"{unique_id}_original.png", folder=user_id)
    gradcam_img_url = upload_image_to_storage(gradcam_img_bytes, f"{unique_id}_gradcam.png", folder=user_id)

    # Simpan metadata ke database
    insert_prediction(
        user_id=user_id,
        original_img_url=original_img_url,
        gradcam_img_url=gradcam_img_url,
        predicted_class=predicted_class_inception,
        confidence_table=df_confidence.to_dict(orient="records"))
