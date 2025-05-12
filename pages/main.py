import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.cm as cm
from tensorflow.keras.applications.convnext import preprocess_input as convnext_preprocess
from tensorflow.keras.applications.inception_v3 import preprocess_input as inception_preprocess
import os
import gdown
import cv2
from io import BytesIO

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .main .block-container {
            padding-top: 2rem;
            height: 500%;
            overflow-x: hidden;
        }

[data-testid="stFileDropzoneInstructions"].small.st-emotion-cache-7oyrr6 e1bju1570 {
    color: #2e5339;
}
[data-testid="stHeader"] {
    background-color: #ffff;
}

[data-testid="stAppViewBlockContainer"] {
    background: linear-gradient(45deg, #d7eac2 25%, #a9d7a9 50%, #f0e58a 75%, #e3d26f 100%);
    animation: backgroundGradientShift 10s ease infinite;
    background-size: 300% 300%;
    background-attachment: fixed;
}

@keyframes backgroundGradientShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

[data-testid="stSpinner"] {
    background: linear-gradient(130deg, #fdf6ec 0%, #e6f4ea 50%, #fff9c4 100%);
}

[data-testid="baseButton-headerNoPadding"], [data-testid="baseButton-secondary"], [data-testid="stUploadedFile"], [data-testid="stFileUploadDropzone"], [data-testid="stFileDropzoneInstructions"] {
    color:#2e5339;
}

[data-testid="stFileUploaderDropzoneInstructions"] small:nth-of-type(1), [data-testid="element-container"], [data-testid="stFileUploaderDropzone"] {
    color:#2e5339;
}

[data-testid="baseButton-secondary"] {
    background-color: white;
}

# [data-testid="stSidebarUserContent"], [data-testid="stFileUploaderDropzone"], [data-testid="stSidebarHeader"] {
#     background: linear-gradient(135deg, #e9f5db 0%, #c7e9b0 40%, #fef9c3 100%); 
# }

# [data-testid="stSidebarUserContent"]{
#     height: 100%; 
#     padding-top: 2rem;
# }

.banner {
    background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20230912/pngtree-the-whole-field-was-full-of-cabbages-image_13120953.png');
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.banner h1 {
    font-size: 3rem;
    color: #ffffff;
    margin: 10px;
    text-shadow: 1px 1px 3px #000;
}
.banner h2 {
    font-size: 1.5rem;
    color: #f0f0f0;
    margin: 0 20px;
    text-shadow: 1px 1px 2px #000;
}
.banner button {
    height: 45px;
    padding: 0 40px;
    border-radius: 100px;
    border: 1px solid #ffffff;
    background-color: rgba(255, 255, 255, 0.8);
    color: #1b4332;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
}

.streamlit-expanderHeader {
    color: red;
}

[data-testid="stMarkdownContainer"]{
    color:#2e5339;
}

/* Judul besar */
.big-title {
    font-size: 36px;
    font-weight: 700;
    color: #1b4332;
}

/* Subjudul */
.sub-title {
    font-size: 20px;
    color: #3a5a40;
}

/* Kartu fitur dan deskripsi instar */
.card {
    border-radius: 10px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    border: 1px solid #2e5339;
    border-color: white;
    color: #2e5339;
    background: linear-gradient(135deg, #e9f5db 0%, #a7f6db 40%, #fef9c3 100%);
}

.card-informasi {
    border-radius: 10px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    background-color: #ffff;
    border: 1px solid #2e5339;
    color: #2e5339;
    height: 250px;
}

[data-testid="stHeadingWithActionElements"] {
    text-align: center;
}

[data-testid="baseButton-secondary"] {
    border-radius: 30px;
    border: 2px solid #ffffff;
    background: linear-gradient(145deg, #fefae0, #e9f5db);
    color: #1b4332;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    text-align: center;
    border-color:
}

[data-testid="baseButton-secondary"]:hover {
    background: #d8f3dc;
    color: #2d6a4f;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
    border-color: #a7f6db;
}

</style>
""", unsafe_allow_html=True)
@st.cache_resource
def load_inception_model():
    model_path = 'InceptionV31_model.keras'
    if not os.path.exists(model_path):
        url = 'https://drive.google.com/uc?id=1brLqWkd9AQbhvSGkk7rM03V5I_NfebUj'
        gdown.download(url, model_path, quiet=False)
    return tf.keras.models.load_model(model_path)

inception_model = load_inception_model()

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
        model.input, 
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
    # Convert PIL image to array and ensure RGB
    img = img.convert("RGB")
    img = np.array(img)

    # Resize heatmap ke ukuran gambar
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))

    heatmap = np.uint8(255 * heatmap)
    heatmap = cm.jet(heatmap)[:, :, :3] * 255
    heatmap = np.uint8(heatmap)

    superimposed_img = cv2.addWeighted(img, 1 - alpha, heatmap, alpha, 0)
    return superimposed_img



# 📤 Upload gambar untuk prediksi
margin_col1, margin_col2, margin_col3 = st.columns([1, 3, 1])
with margin_col1:
    st.write("")

with margin_col2:
    st.header("Klasifikasi Tahapan Instar Crocidolomia Pavonana", divider="green")
    tab1, tab2 = st.tabs(["Klasifikasi", "Contoh Gambar"])
    with tab1:
        uploaded_file = st.file_uploader(label="Upload gambar", type=['jpg', 'jpeg', 'png'])
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
                gradcam_col1, gradcam_col2, gradcam_col3 = st.columns(3)
                
                # Simpan ke session state (history)
                if "history" not in st.session_state:
                    st.session_state.history = []

                # Konversi gambar asli dan hasil gradcam jadi bentuk yang bisa disimpan
                from io import BytesIO

                def pil_to_bytes(img):
                    buf = BytesIO()
                    img.save(buf, format="PNG")
                    return buf.getvalue()

                from PIL import Image

                # Konversi hasil superimposed jadi PIL Image dulu
                result_pil = Image.fromarray(superimposed_img_inception)

                st.session_state.history.append({
                    "original": image.copy(),
                    "heatmap": Image.fromarray(superimposed_img_inception),
                    "prediction": predicted_class_inception,
                    "confidence": confidence_inception,
                    "df_confidence": pd.DataFrame({
                        'Tahap Instar': class_names,
                        'Akurasi (%)': prediction_inception[0] * 100
                    })
                })

                
                st.image(superimposed_img_inception, caption="Grad-CAM InceptionV3", use_column_width=True)
                gradcam_status_placeholder.success("✅ Grad-CAM berhasil dibuat!")
    with tab2:
        st.subheader("Contoh Gambar Instar")
        instar_data = [
            {
                "title": "Instar 1",
                "img": "assets/instar1.jpg",
            },
            {
                "title": "Instar 2",
                "img": "assets/instar2.jpg",
            },
            {
                "title": "Instar 3",
                "img": "assets/instar3.jpg",
            },
            {
                "title": "Instar 4",
                "img": "assets/instar4.jpg",
            }
        ]

        cols = st.columns(2)
        for i in range(0,2):
            with cols[i]:
                st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">{instar_data[i]["title"]}</h1>', unsafe_allow_html=True)
                st.image(instar_data[i]["img"], use_column_width=True)
        
        cols = st.columns(2)
        for i in range(2,4):
            with cols[i-2]:
                st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">{instar_data[i]["title"]}</h1>', unsafe_allow_html=True)
                st.image(instar_data[i]["img"], use_column_width=True)

with margin_col3:
    st.write("")
