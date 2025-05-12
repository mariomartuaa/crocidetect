import streamlit as st

margin_col1, margin_col2, margin_col3 = st.columns([1, 2, 1])

with margin_col1:
    st.write("")
    
with margin_col2:
    st.header("Cara Penggunaan Aplikasi", divider="green")
    st.subheader("1. Upload Gambar")
    st.write("Unggah gambar larva *Crocidolomia pavonana* dalam format `.jpg`, `.jpeg`, atau `.png`.")
    with st.expander("Lihat selengkapnya"):
        st.image("assets/guide/1.png")

    st.subheader("2. Lihat Pratinjau Gambar")
    st.write("Gambar yang Anda unggah akan otomatis ditampilkan sebagai pratinjau di halaman utama.")
    with st.expander("Lihat selengkapnya"):
        st.image("assets/guide/2.png")

    st.subheader("3. Klik Tombol 'Klasifikasi Gambar'")
    st.write("Tekan tombol ini untuk memulai proses klasifikasi tahapan instar menggunakan model deep learning.")
    with st.expander("Lihat selengkapnya"):
        st.image("assets/guide/3.png")

    # st.subheader("4. Tunggu Proses Prediksi")
    # st.write("Sistem akan memproses gambar dan menampilkan hasil prediksi beserta tingkat akurasinya.")

    st.subheader("4. Tinjau Hasil Klasifikasi")
    st.write("Hasil klasifikasi ditampilkan dalam bentuk kelas instar, nilai akurasi, dan tabel confidence untuk semua kelas.")
    with st.expander("Lihat selengkapnya"):
        st.image("assets/guide/5.png")

    st.subheader("5. Lihat Visualisasi Grad-CAM")
    st.write("Grad-CAM menunjukkan area penting dari gambar yang memengaruhi keputusan model. Ini membantu memahami hasil prediksi.")
    with st.expander("Lihat selengkapnya"):
        st.image("assets/guide/6.png")
        
    st.subheader("6. Lihat Riwayat (Opsional)")
    st.write("Buka menu **History** di sidebar untuk melihat gambar dan visualisasi Grad-CAM sebelumnya selama sesi berjalan.")
    with st.expander("Lihat selengkapnya"):
        st.image("assets/guide/7.png")

with margin_col3:
    st.write("")
