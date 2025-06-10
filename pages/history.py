import streamlit as st
from utils.db import get_predictions_by_user, delete_prediction
import pandas as pd
import json
from datetime import datetime
from utils.utils import get_user_id

user_id = get_user_id()

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
            rec_id = rec['id']
            timestamp = rec['timestamp']
            orig_img_url = rec['original_image']
            gradcam_img_url = rec['gradcam_image']
            pred_class = rec['predicted_class']
            conf_json = json.loads(rec['confidence_table'])


            dt = datetime.fromisoformat(timestamp)
            formatted = dt.strftime("%d-%m-%Y Pukul %H:%M:%S")
            st.write(f"### Prediksi pada: {formatted}")

            img_col1, img_col2 = st.columns(2)
            with img_col1:
                st.image(orig_img_url, caption="Gambar Asli", use_column_width=True)
            with img_col2:
                st.image(gradcam_img_url, caption="Grad-CAM", use_column_width=True)

            hasil_col1, hasil_col2 = st.columns(2)
            with hasil_col1:
                st.markdown(f"""
                    <div class="card">
                        <strong>Model:</strong> InceptionV3<br>
                        <strong>Prediksi:</strong> {pred_class}<br>
                    </div>
                """, unsafe_allow_html=True)

            with hasil_col2:
                df_conf = pd.DataFrame(conf_json)
                st.dataframe(df_conf.style.format({'Akurasi (%)': '{:.2f}'}))

            if st.button("Hapus", key=f"del_{rec_id}"):
                delete_prediction(rec_id)
                delete_placeholder = st.empty()
                delete_placeholder.info("⏳ Menghapus data...")
                st.rerun()
                delete_placeholder.success("✅ Data berhasil dihapus")

            st.divider()

with margin_col3:
    st.write("")
