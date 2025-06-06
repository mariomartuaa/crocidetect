import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from pages.db import get_predictions_by_user, delete_prediction
import pandas as pd
from PIL import Image
import io

cookies = EncryptedCookieManager(
    prefix="crocidetect_",
    password=st.secrets["COOKIE_SECRET"])

if not cookies.ready():
    st.stop()

if "user_id" not in cookies or cookies["user_id"] is None:
    st.warning("User ID tidak ditemukan. Silakan lakukan prediksi dulu di halaman utama.")
    st.stop()

user_id = cookies["user_id"]

# Inisialisasi session state
if "history_records" not in st.session_state:
    st.session_state.history_records = get_predictions_by_user(user_id)

margin_col1, margin_col2, margin_col3 = st.columns([1, 3, 1])
with margin_col1:
    st.write("")

with margin_col2:
    st.header("Riwayat Klasifikasi", divider="green")

    if not st.session_state.history_records:
        st.info("Belum ada riwayat prediksi.")
    else:
        # Buat key khusus untuk daftar yang ingin dihapus
        if "deleted_ids" not in st.session_state:
            st.session_state.deleted_ids = set()

        # Tampilkan setiap record
        for i, rec in enumerate(st.session_state.history_records):
            rec_id, timestamp, orig_img_blob, gradcam_img_blob, pred_class, conf_json = rec

            # Lewati record yang sudah dihapus
            if rec_id in st.session_state.deleted_ids:
                continue

            st.write(f"### Prediksi pada: {timestamp}")

            # Gambar
            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image(Image.open(io.BytesIO(orig_img_blob)), caption="Gambar Asli", use_column_width=True)
            with img_col2:
                st.image(Image.open(io.BytesIO(gradcam_img_blob)), caption="Grad-CAM Visualisasi", use_column_width=True)

            # Info prediksi
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

            # Tombol hapus
            if st.button("🗑️ Hapus", key=f"del_{rec_id}"):
                delete_prediction(rec_id)
                st.session_state.deleted_ids.add(rec_id)
                st.success(f"Berhasil menghapus prediksi {timestamp}")

            st.divider()

with margin_col3:
    st.write("")
