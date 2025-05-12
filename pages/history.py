import streamlit as st
from PIL import Image
from io import BytesIO

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
