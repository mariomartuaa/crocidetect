import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from pages.db import get_predictions_by_user, delete_prediction
import pandas as pd
from PIL import Image
import io
import json

# Manajemen cookie login
cookies = EncryptedCookieManager(
    prefix="crocidetect_",
    password=st.secrets["COOKIE_SECRET"])
if not cookies.ready():
    st.stop()

user_id = cookies["user_id"]

# Layout 3 kolom (tengah utama)
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
            rec_id, timestamp, orig_img_bytes, gradcam_img_bytes, pred_class, conf_json_str = rec

            st.write(f"### Prediksi pada: {timestamp}")

            # Tampilkan gambar
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image(Image.open(io.BytesIO(orig_img_bytes)), caption="Gambar Asli", use_column_width=True)
            with img_col2:
                st.image(Image.open(io.BytesIO(gradcam_img_bytes)), caption="Grad-CAM Visualisasi", use_column_width=True)

            # Tampilkan hasil & confidence
            hasil_col1, hasil_col2 = st.columns(2)
            with hasil_col1:
                st.markdown(f"""
                    <div class="card">
                        <strong>Model:</strong> InceptionV3<br>
                        <strong>Prediksi:</strong> {pred_class}<br>
                    </div>
                """, unsafe_allow_html=True)

            with hasil_col2:
                try:
                    df_conf = pd.read_json(io.StringIO(conf_json_str))
                except:
                    df_conf = pd.DataFrame(json.loads(conf_json_str))  # fallback
                st.dataframe(df_conf.style.format({'Akurasi (%)': '{:.2f}'}))

            # Tombol hapus
            if st.button("Hapus", key=f"del_{rec_id}"):
                delete_prediction(rec_id)
                st.rerun()

            st.divider()

with margin_col3:
    st.write("")
