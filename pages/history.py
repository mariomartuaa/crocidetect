import streamlit as st
from PIL import Image
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

margin_col1, margin_col2, margin_col3 = st.columns([1, 3, 1])

with margin_col1:
    st.write("")
    
with margin_col2:
    if "history" not in st.session_state:
        st.session_state.history = []
    else:
        # Filter hanya item yang lengkap
        st.session_state.history = [
            h for h in st.session_state.history
            if all(k in h for k in ["original", "heatmap", "prediction", "confidence", "df_confidence"])
        ]
    
    st.header("Riwayat Klasifikasi", divider="green")

    if not st.session_state.history:
        st.info("Belum ada riwayat klasifikasi pada sesi ini.")
    else:
        for i, item in enumerate(reversed(st.session_state.history), 1):
            st.write(f"Hasil #{len(st.session_state.history) - i + 1}")
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image(item["original"], caption="Gambar Input", use_column_width=True)
            with img_col2:
                st.image(item["heatmap"], caption="Grad-CAM", use_column_width=True)
            
            hasil_col1, hasil_col2 = st.columns(2)
            with hasil_col1:
                st.markdown(f"""
                    <div class="card">
                        <strong>Model: </strong>InceptionV3<br>
                        <strong>Prediksi: </strong>{item['prediction']}<br>
                        <strong>Akurasi: </strong>{item['confidence']:.2f}%<br>
                    </div>
                                    """, unsafe_allow_html=True)
            
            with hasil_col2:
                st.dataframe(item["df_confidence"].style.format({'Akurasi (%)': '{:.2f}'}))

            st.divider()
with margin_col3:
    st.write("")
