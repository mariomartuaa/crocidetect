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

init_db()
# Init cookie manager
cookies = EncryptedCookieManager(
    prefix="crocidetect_",
    password=st.secrets["COOKIE_SECRET"])

if not cookies.ready():
    st.stop()

# Dapatkan user_id dari cookie, kalau belum ada buat baru dan simpan ke cookie
user_id = cookies.get("user_id")
if user_id is None:
    user_id = str(uuid.uuid4())
    cookies["user_id"] = user_id
    cookies.save()

# Preprocessing function
def preprocess_image_inception(image: Image.Image):
    image = image.resize((512, 512))
    image_array = np.array(image)
    if image_array.shape[-1] == 4:
        image_array = image_array[:, :, :3]
    image_array = np.expand_dims(image_array, axis=0)
    image_array = inception_preprocess(image_array)
    return image_array

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    grad_model = tf.keras.models.Model(
        model.inputs, 
        [model.get_layer(last_conv_layer_name).output, model.output]
    )


    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    # Gradients terhadap output feature map
    grads = tape.gradient(class_channel, conv_outputs)

    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]

    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    heatmap = heatmap.numpy()

    return heatmap

def superimpose_heatmap(img, heatmap, alpha=0.4):
    img = img.convert("RGB")
    img = np.array(img)

    # Resize heatmap ke ukuran gambar
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))

    heatmap = np.uint8(255 * heatmap)
    heatmap = cm.jet(heatmap)[:, :, :3] * 255
    heatmap = np.uint8(heatmap)

    superimposed_img = cv2.addWeighted(img, 1 - alpha, heatmap, alpha, 0)
    return superimposed_img

st.markdown("""
<div class="hero-section">
    <img src="https://i.imgur.com/6FYuwbg.png" class="logo-img2">
    <h1 class="hero-title">CROCIDETECT</h1>
</div>
""", unsafe_allow_html=True)
margin_col1, margin_col2, margin_col3 = st.columns([1, 3, 1])
with margin_col1:
    st.write("")

with margin_col2:
    st.markdown("""<hr>""",unsafe_allow_html=True)
    st.header("Spesifikasi Gambar Input")
    with st.expander("📷 Gambar yang disarankan"):
        st.markdown("""
                <div class="card">
                    <ul class="indent-list">
                      <li>Resolusi minimal <strong>512 x 512 piksel</strong> dan tidak buram,  
                          agar hasil prediksi lebih akurat.</li>
                      <li>Ukuran file maksimum <strong>200 MB</strong>.</li>
                      <li>Format file yang diterima: <strong>JPG, JPEG, PNG</strong>.</li>
                    </ul>
                </div>
        """, unsafe_allow_html=True)
    with st.expander("🐛 Contoh Gambar Instar"):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Contoh Gambar Instar 1</h1>', unsafe_allow_html=True)
            st.image("assets/instar1.jpg", use_column_width=True)
        
        with col2:
            st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Contoh Gambar Instar 2</h1>', unsafe_allow_html=True)
            st.image("assets/instar2.jpg", use_column_width=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Contoh Gambar Instar 3</h1>', unsafe_allow_html=True)
            st.image("assets/instar3.jpg", use_column_width=True)
        
        with col4:
            st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Contoh Gambar Instar 4</h1>', unsafe_allow_html=True)
            st.image("assets/instar4.jpg", use_column_width=True)

    
    st.header("Unggah Gambar")
    uploaded_file = st.file_uploader(label ='', type=['jpg', 'jpeg', 'png'])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

        if st.button("Klasifikasi Gambar"):
            status_placeholder = st.empty()
            status_placeholder.info("⏳ Memproses dan memprediksi gambar...")

            # Mapping kelas
            class_names = ['Instar 1', 'Instar 2', 'Instar 3', 'Instar 4']

            # Prediksi InceptionV3
            preprocessed_inception = preprocess_image_inception(image)
            prediction_inception = inception_model.predict(preprocessed_inception)
            predicted_class_inception = class_names[np.argmax(prediction_inception)]
            confidence_inception = np.max(prediction_inception) * 100

            status_placeholder.success("✅ Klasifikasi selesai!")
            hasil_col1, hasil_col2 = st.columns(2)
            with hasil_col1:
                st.markdown(f"""
                    <div class="card">
                        <strong>Model: </strong>InceptionV3<br>
                        <strong>Prediksi: </strong>{predicted_class_inception}<br>
                        <strong>Akurasi: </strong>{confidence_inception:.2f}%<br>
                    </div>
                                    """, unsafe_allow_html=True)
            
            with hasil_col2:
                # Data untuk visualisasi
                df_confidence = pd.DataFrame({
                    'Tahap Instar': class_names,
                    'Akurasi (%)': prediction_inception[0] * 100
                })
                st.dataframe(df_confidence.style.format({'Akurasi (%)': '{:.2f}'}))
                    
            gradcam_status_placeholder = st.empty()
            gradcam_status_placeholder.info("⏳ Membuat Grad-CAM visualisasi...")
            
            # Grad-CAM InceptionV3
            heatmap_inception = make_gradcam_heatmap(preprocessed_inception, inception_model, "mixed10")
            superimposed_img_inception = superimpose_heatmap(image, heatmap_inception)


            # Grad-CAM InceptionV3
            heatmap_inception = make_gradcam_heatmap(preprocessed_inception, inception_model, "mixed10")
            superimposed_img_inception = superimpose_heatmap(image, heatmap_inception)

            # Tampilkan Grad-CAM
            st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Grad-CAM Visualisasi</h1>', unsafe_allow_html=True)
            st.image(superimposed_img_inception, caption="Grad-CAM InceptionV3", use_column_width=True)

            # Simpan ke DB
            original_img_bytes = BytesIO()
            image.save(original_img_bytes, format='PNG')
            original_img_bytes = original_img_bytes.getvalue()

            gradcam_img_bytes = cv2.imencode('.png', superimposed_img_inception)[1].tobytes()
            confidence_json = df_confidence.to_json(orient="records")

            insert_prediction(
                user_id=user_id,
                original_image=original_img_bytes,
                gradcam_image=gradcam_img_bytes,
                predicted_class=predicted_class_inception,
                confidence_table=confidence_json
            )
            
            gradcam_status_placeholder.success("✅ Grad-CAM berhasil dibuat dan data disimpan!")

with margin_col3:
    st.write("")
