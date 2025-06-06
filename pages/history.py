import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from pages.db import get_predictions_by_user, delete_prediction
import pandas as pd
from PIL import Image
import io
from pages.db import user_id

cookies = EncryptedCookieManager(
    prefix="crocidetect_",
    password="ini_password_super_rahasia_123!"
)
if not cookies.ready():
    st.stop()

user_id = cookies["user_id"]

margin_col1, margin_col2, margin_col3 = st.columns([1, 3, 1])

with margin_col1:
    st.write("")

with margin_col2:
    st.header("Riwayat Klasifikasi", divider="green")

    records = get_predictions_by_user(user_id)

    if not records:
        st.info("Belum ada riwayat prediksi.")
    else:
        for rec in records:
            rec_id, timestamp, orig_img_blob, gradcam_img_blob, pred_class, conf_json = rec

            st.write(f"### Prediksi pada: {timestamp}")

            # Gambar dalam 2 kolom
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image(Image.open(io.BytesIO(orig_img_blob)), caption="Gambar Asli", use_column_width=True)
            with img_col2:
                st.image(Image.open(io.BytesIO(gradcam_img_blob)), caption="Grad-CAM Visualisasi", use_column_width=True)

            # Hasil prediksi dan tabel confidence dalam 2 kolom
            hasil_col1, hasil_col2 = st.columns(2)
            with hasil_col1:
                st.markdown(f"""
                    <div class="card">
                        <strong>Model:</strong> InceptionV3<br>
                        <strong>Prediksi:</strong> {pred_class}<br>
                    </div>
                """, unsafe_allow_html=True)

            with hasil_col2:
                df_conf = pd.read_json(io.StringIO(conf_json))
                st.dataframe(df_conf.style.format({'Akurasi (%)': '{:.2f}'}))

            if st.button("Hapus", key=f"del_{rec_id}"):
                    delete_prediction(rec_id)
                    st.rerun()

            st.divider()

with margin_col3:
    st.write("")
