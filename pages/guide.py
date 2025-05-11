import streamlit as st

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
    animation: backgroundGradientShift 20s ease infinite;
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

margin_col1, margin_col2, margin_col3 = st.columns([1, 2, 1])

with margin_col1:
    st.write("")
    
with margin_col2:
    st.header("Langkah-langkah Penggunaan", divider="green")
    st.subheader("1. Upload Gambar")
    st.write("Unggah gambar larva *Crocidolomia pavonana* dalam format `.jpg`, `.jpeg`, atau `.png`.")
    with st.expander("Baca selengkapnya"):
        st.image("assets/guide/1.png")

    st.subheader("2. Lihat Pratinjau Gambar")
    st.write("Gambar yang Anda unggah akan otomatis ditampilkan sebagai pratinjau di halaman utama.")
    with st.expander("Baca selengkapnya"):
        st.image("assets/guide/2.png")

    st.subheader("3. Klik Tombol 'Klasifikasi Gambar'")
    st.write("Tekan tombol ini untuk memulai proses klasifikasi tahapan instar menggunakan model deep learning.")
    with st.expander("Baca selengkapnya"):
        st.image("assets/guide/3.png")

    # st.subheader("4. Tunggu Proses Prediksi")
    # st.write("Sistem akan memproses gambar dan menampilkan hasil prediksi beserta tingkat akurasinya.")

    st.subheader("4. Tinjau Hasil Klasifikasi")
    st.write("Hasil klasifikasi ditampilkan dalam bentuk kelas instar, nilai akurasi, dan tabel confidence untuk semua kelas.")
    with st.expander("Baca selengkapnya"):
        st.image("assets/guide/5.png")

    st.subheader("5. Lihat Visualisasi Grad-CAM")
    st.write("Grad-CAM menunjukkan area penting dari gambar yang memengaruhi keputusan model. Ini membantu memahami hasil prediksi.")
    with st.expander("Baca selengkapnya"):
        st.image("assets/guide/6.png")
        
    st.subheader("6. Lihat Riwayat (Opsional)")
    st.write("Buka menu **History** di sidebar untuk melihat gambar dan visualisasi Grad-CAM sebelumnya selama sesi berjalan.")
    with st.expander("Baca selengkapnya"):
        st.image("assets/guide/7.png")

with margin_col3:
    st.write("")