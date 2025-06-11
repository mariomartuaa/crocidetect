import streamlit as st
from PIL import Image
from utils.utils import get_user_id, load_inception_model, predict_instar, make_gradcam_heatmap, insert_database

    
loading_model = st.empty()
loading_model.info("⏳ Loading Model...")
inception_model = load_inception_model()
loading_model.success("✅ Berhasil Mengload Model")
loading_model.empty()

user_id = get_user_id()

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
                      <li>Gambar memiliki resolusi minimal <strong>512 x 512 piksel</strong> dan tidak buram,  
                          agar hasil prediksi lebih akurat.</li>
                      <li>Ukuran file maksimum <strong>20 MB</strong>.</li>
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
    uploaded_file = st.file_uploader(label ='Unggah gambar', type=['jpg', 'jpeg', 'png'])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

        if st.button("Klasifikasi Gambar"):
            status_placeholder = st.empty()
            status_placeholder.info("⏳ Memproses dan memprediksi gambar...")

            predicted_class_inception, confidence_inception, df_confidence = predict_instar(inception_model, image)

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
                st.dataframe(df_confidence.style.format({'Akurasi (%)': '{:.2f}'}))
                    
            gradcam_status_placeholder = st.empty()
            gradcam_status_placeholder.info("⏳ Membuat Grad-CAM visualisasi...")

            # Grad-CAM InceptionV3
            grad_cam = make_gradcam_heatmap(image, inception_model, "mixed10")

            # Tampilkan Grad-CAM
            if user_id is None:
                st.warning("Prediksi tidak disimpan karena cookie user tidak tersedia.")
                st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Grad-CAM Visualisasi</h1>', unsafe_allow_html=True)
                st.image(grad_cam, caption="Grad-CAM InceptionV3", use_column_width=True)
                gradcam_status_placeholder.success("✅ Grad-CAM berhasil dibuat!")
            else: 
                insert_database(user_id, image, grad_cam, predicted_class_inception, df_confidence)
                st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Grad-CAM Visualisasi</h1>', unsafe_allow_html=True)
                st.image(grad_cam, caption="Grad-CAM InceptionV3", use_column_width=True)
                gradcam_status_placeholder.success("✅ Grad-CAM berhasil dibuat dan data disimpan!")

with margin_col3:
    st.write("")
