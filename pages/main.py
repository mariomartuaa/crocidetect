# Refactored main.py
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.cm as cm
from tensorflow.keras.applications.inception_v3 import preprocess_input as inception_preprocess
import os
import gdown
import cv2
from io import BytesIO
from pages.db import init_db, insert_prediction
import uuid

# ============ INIT MODEL ============
@st.cache_resource
def load_inception_model():
    model_path = 'InceptionV32_model.keras'
    if not os.path.exists(model_path):
        url = 'https://drive.google.com/uc?id=1H5QA7p4j7wNtsdnzVbtE1l3deaBh_KAi'
        gdown.download(url, model_path, quiet=False)
    return tf.keras.models.load_model(model_path)

loading_model = st.empty()
loading_model.info("⏳ Loading Model...")
inception_model = load_inception_model()
loading_model.success("✅ Berhasil Mengload Model")
loading_model.empty()

# ============ INIT DB ============
init_db()

# ============ COOKIE HANDLING ============
cookies = EncryptedCookieManager(prefix="crocidetect_", password=st.secrets["COOKIE_SECRET"])
if not cookies.ready():
    st.stop()

user_id = cookies.get("user_id")
if "user_id" not in st.session_state:
    if user_id is None:
        user_id = str(uuid.uuid4())
        cookies["user_id"] = user_id
        cookies.save()
    st.session_state.user_id = user_id
else:
    user_id = st.session_state.user_id

# ============ INIT SESSION STATE ============
if "image" not in st.session_state:
    st.session_state.image = None
if "run_prediction" not in st.session_state:
    st.session_state.run_prediction = False
if "predicted_class" not in st.session_state:
    st.session_state.predicted_class = None
if "confidence_table" not in st.session_state:
    st.session_state.confidence_table = None

# ============ UTILS ============
def preprocess_image_inception(image: Image.Image):
    image = image.resize((512, 512))
    image_array = np.array(image)
    if image_array.shape[-1] == 4:
        image_array = image_array[:, :, :3]
    image_array = np.expand_dims(image_array, axis=0)
    image_array = inception_preprocess(image_array)
    return image_array

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    grad_model = tf.keras.models.Model(model.inputs, [model.get_layer(last_conv_layer_name).output, model.output])
    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

def superimpose_heatmap(img, heatmap, alpha=0.4):
    img = np.array(img.convert("RGB"))
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cm.jet(heatmap)[:, :, :3] * 255
    heatmap = np.uint8(heatmap)
    return cv2.addWeighted(img, 1 - alpha, heatmap, alpha, 0)

# ============ UI ============
st.markdown("""
<div class="hero-section">
    <img src="https://i.imgur.com/6FYuwbg.png" class="logo-img2">
    <h1 class="hero-title">CROCIDETECT</h1>
</div>
""", unsafe_allow_html=True)

margin_col1, margin_col2, margin_col3 = st.columns([1, 3, 1])
with margin_col2:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Spesifikasi Gambar Input")
    with st.expander("📷 Gambar yang disarankan"):
        st.markdown("""
            <ul class="indent-list">
              <li>Resolusi minimal <strong>512 x 512 piksel</strong>.</li>
              <li>Ukuran file maksimum <strong>200 MB</strong>.</li>
              <li>Format file: <strong>JPG, JPEG, PNG</strong>.</li>
            </ul>
        """, unsafe_allow_html=True)

    with st.expander("🐛 Contoh Gambar Instar"):
        cols = st.columns(2)
        for i in range(1, 5):
            with cols[i % 2]:
                st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Contoh Gambar Instar {i}</h1>', unsafe_allow_html=True)
                st.image(f"assets/instar{i}.jpg", use_column_width=True)

    st.header("Unggah Gambar")
    uploaded_file = st.file_uploader(label='Unggah gambar', type=['jpg', 'jpeg', 'png'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.session_state.image = image  # Simpan ke session state
        st.image(image, use_column_width=True)


        if st.button("Klasifikasi Gambar"):
            st.session_state.run_prediction = True

    # Jika sudah ada hasil prediksi dan user klik klasifikasi
    if st.session_state.get("run_prediction") and st.session_state.get("image") is not None:
        image = st.session_state.image
        status = st.empty()
        status.info("⏳ Memproses dan memprediksi gambar...")

        class_names = ['Instar 1', 'Instar 2', 'Instar 3', 'Instar 4']
        preprocessed = preprocess_image_inception(image)
        prediction = inception_model.predict(preprocessed)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction) * 100

        st.session_state.predicted_class = predicted_class
        st.session_state.confidence_table = pd.DataFrame({
            'Tahap Instar': class_names,
            'Akurasi (%)': prediction[0] * 100
        })

        status.success("✅ Klasifikasi selesai!")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <div class="card">
                    <strong>Model:</strong> InceptionV3<br>
                    <strong>Prediksi:</strong> {predicted_class}<br>
                    <strong>Akurasi:</strong> {confidence:.2f}%<br>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.dataframe(st.session_state.confidence_table.style.format({'Akurasi (%)': '{:.2f}'}))

        grad_status = st.empty()
        grad_status.info("⏳ Membuat Grad-CAM visualisasi...")

        heatmap = make_gradcam_heatmap(preprocessed, inception_model, "mixed10")
        gradcam_img = superimpose_heatmap(image, heatmap)
        st.image(gradcam_img, caption="Grad-CAM InceptionV3", use_column_width=True)

        original_img_bytes = BytesIO()
        image.save(original_img_bytes, format='PNG')
        gradcam_img_bytes = cv2.imencode('.png', gradcam_img)[1].tobytes()
        insert_prediction(
            user_id=user_id,
            original_image=original_img_bytes.getvalue(),
            gradcam_image=gradcam_img_bytes,
            predicted_class=predicted_class,
            confidence_table=st.session_state.confidence_table.to_json(orient="records")
        )

        grad_status.success("✅ Grad-CAM berhasil dibuat dan data disimpan!")

        # Reset flag supaya tidak rerun terus
        st.session_state.run_prediction = False

