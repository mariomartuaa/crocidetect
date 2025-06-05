import streamlit as st
from PIL import Image

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
    .main .block-container {
        padding: 0;
        margin: 0;
        overflow-x: hidden;
    }

[data-testid="baseButton-headerNoPadding"] {
    background: #fef9c3; 
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

[data-testid="stHorizontalBlock"]{
    padding-left: 5rem;
    padding-right: 5rem;
}

.banner-picture {
    background-image: url('https://images.unsplash.com/photo-1486328228599-85db4443971f?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2FiYmFnZXxlbnwwfHwwfHx8MA%3D%3D');
    background-size: cover;
    background-position: center;
    height: 100vh;
    position: absolute;
    top:-16px;
    right:0;
    left:0;
}

.banner {
    top: -2rem;
    left: 0;
    right: 0;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: absolute;
    padding-bottom: 10vh;
    z-index: 9998;
}
.banner h1 {
    font-size: clamp(1.5rem, 5vw, 3rem);
    color: #ffffff;
    margin: 10px;
    text-shadow: 1px 1px 3px #000;
}
.banner h2 {
    font-size: clamp(1rem, 3vw, 1.5rem);
    color: #f0f0f0;
    margin: 0 20px;
    text-shadow: 1px 1px 2px #000;
}

.banner button {
    font-size: clamp(0.875rem, 2vw, 1.125rem);
    padding: 0 clamp(1rem, 5vw, 2.5rem);
    height: clamp(50px, 5vh, 50px);
    border-radius: 30px;
    border: 2px solid #ffffff;
    background: linear-gradient(145deg, #fefae0, #e9f5db);
    color: #1b4332;
    font-weight: 600;
    cursor: pointer;
    margin-top: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    text-align: center;
}

.banner button:hover {
    background: #d8f3dc;
    color: #2d6a4f;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
    transform: translateY(-2px);
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
    background: linear-gradient(135deg, #e9f5db 0%, #c7e9b0 40%, #fef9c3 100%);
    border: 1px solid #2e5339;
    color: #2e5339;
    font-size: clamp(0.9rem, 1.5vw, 1.2rem);
}

.card-informasi {
    border-radius: 10px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    background: linear-gradient(135deg, #e9f5db 0%, #c7e9b0 40%, #fef9c3 100%);
    border: 1px solid #2e5339;
    color: #2e5339;
    font-size: clamp(0.9rem, 1.5vw, 1.2rem);
    height: 100%;
}

/* Optional: semua heading dan teks lainnya */

[data-testid="baseButton-secondary"] {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: clamp(0.875rem, 2vw, 1.125rem);
    padding: 0 clamp(1rem, 5vw, 2.5rem);
    height: clamp(50px, 5vh, 50px);
    border-radius: 30px;
    border: 2px solid #ffffff;
    background: linear-gradient(145deg, #fefae0, #e9f5db);
    color: #1b4332;
    font-weight: 600;
    cursor: pointer;
    margin-top: 60vh;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    text-align: center;
    z-index: 9999;
}

[data-testid="baseButton-secondary"]:hover {
    background: #d8f3dc;
    color: #2d6a4f;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
    border-color: #a7f6db;
}

.hero-section {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.logo-img {
    width: clamp(300px, 50vw, 1000px);
    height: clamp(100px, 13vw, 276px);
}

.logo-img2 {
    height: clamp(80px, 10vw, 150px);
    width: clamp(80px, 10vw, 150px);
}

.hero-title {
    font-size: clamp(32px, 10vw, 100px);
    margin: 0;
    color: rgba(225, 225, 225, 0.01);
    background-image: url("https://img.antarafoto.com/cache/1200x775/2023/09/15/panen-sawi-hijau-di-jombang-1864u-dom.jpg");
    background-repeat: repeat;
    -webkit-background-clip: text;
    animation: animateText 15s ease-in-out infinite;
    text-transform: uppercase;
    font-weight: 900;
}

@keyframes animateText {
    0%, 100% { background-position: left top; }
    25% { background-position: right bottom; }
    50% { background-position: left bottom; }
    75% { background-position: right top; }
}

[data-testid="stMarkdownContainer"] p {
    color:#2e5339;
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="banner-picture"> </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="banner">
        <img src="https://i.imgur.com/YsneW2i.png" class="logo-img">
        <h2>Unggah gambar larva Crocidolomia pavonana dan lihat hasil prediksi tahapan instarnya secara otomatis.</h2>
    </div>
""", unsafe_allow_html=True)

if st.button("Mulai"):
    st.session_state.start_app = True
    st.rerun()
    
st.markdown("""<div style="margin-bottom: 100vh"></div>""",unsafe_allow_html=True)

st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Fitur Utama</h1>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        '<div class="card"><strong>Prediksi Instar Otomatis</strong><br>'
        'Model AI kami mengidentifikasi instar larva dengan akurat berdasarkan citra yang diunggah.</div>',
        unsafe_allow_html=True
    )
    
    with st.expander("Baca selengkapnya"):
        st.markdown(
            """
            <div class="card">
                <ul>
                    <li>Menggunakan Model Pretrained CNN InceptionV3.</li>
                    <li>Memprediksi tahapan instar (1 hingga 4) berdasarkan citra larva yang diunggah.</li>
                    <li>Menampilkan hasil prediksi berserta tingkat kepercayaan (confidence score) model.</li>
                    <li>Membantu pengguna mengidentifikasi fase larva dengan cepat dan akurat.</li>
                </ul>
            </div>""",
            unsafe_allow_html=True
        )
        st.image("assets/prediksi-otomatis.jpg")


with col2:
    st.markdown(
        '<div class="card"><strong>Visualisasi Grad-CAM</strong><br>'
        'Lihat bagian gambar mana yang menjadi fokus model dalam menentukan klasifikasi.</div>',
        unsafe_allow_html=True
    )
    with st.expander("Baca selengkapnya"):
        st.markdown(
            """
            <div class="card">
                Menampilkan area penting pada gambar yang mempengaruhi hasil keputusan prediksi model.
            </div>""",
            unsafe_allow_html=True
        )
        st.image('assets/grad-cam.jpg')

st.markdown("""<hr style="background-color: black; margin-left:5rem; margin-right:5rem;">""",unsafe_allow_html=True)

st.markdown('<div style="display: flex; justify-content: center;"><img src="https://i.imgur.com/9zNBhxV.png" alt="Alternative text" style="height: 40%;"></div>', unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Crocidolomia Pavonana</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Klasifikasi Ilmiah</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div class="card-informasi">
            <ul>
                <li><strong>Kingdom</strong>: Animalia</li>
                <li><strong>Phylum</strong>: Arthropoda<br></li>
                <li><strong>Class</strong>: Insecta</li>
                <li><strong>Ordo</strong>: Lepidoptera</li>
                <li><strong>Family</strong>: Crambidae</li>
                <li><strong>Genus</strong>: Crocidolomia</li>
                <li><strong>Spesies</strong>: <em>Crocidolomia pavonana</em> (Fabricius)</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True)

with col2:
    st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Dampak Kerusakan</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div class="card-informasi">
            <ul>
                <li>Menyerang daun muda dan titik tumbuh tanaman.</li>
                <li>Kerusakan hingga 100% pada musim kemarau.</li>
                <li>Larva memakan daun hingga tersisa tulangnya saja.</li>
                <li>Mengakibatkan gagal panen total jika tidak dikendalikan.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True)
    
st.markdown("""<hr style="background-color: black; margin-left:5rem; margin-right:5rem;">""",unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Tanaman Inang</h1>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Kubis</h1>', unsafe_allow_html=True)
    st.image("assets/kubis.jpg", use_column_width=True)

with col2:
    st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Sawi</h1>', unsafe_allow_html=True)
    st.image("assets/sawi.jpg", use_column_width=True)

with col3:
    st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Brokoli</h1>', unsafe_allow_html=True)
    st.image("assets/brokoli.jpg", use_column_width=True)
    
with col4:
    st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Lobak</h1>', unsafe_allow_html=True)
    st.image("assets/lobak.jpg", use_column_width=True)

st.markdown("""<hr style="background-color: black; margin-left:5rem; margin-right:5rem;">""",unsafe_allow_html=True)

st.markdown(f'<h1 style="text-align: center; font-size: 30px; color: #2e5339;">Pengendalian Hama</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<h1 style="text-align: center; font-size: 25px; color: #2e5339;">Pestisida Nabati Tanaman Mindi</h1>', unsafe_allow_html=True)
    st.image("assets/Mindi.jpg")
    st.markdown("""
        <div class="card-informasi">
            <p><strong>Efek terhadap hama:</strong></p>
            <ul>
                <li>Penolak (repellent)</li>
                <li>Penghambat aktivitas makan (antifeedant)</li>
                <li>Menghambat pembentukan telur</li>
                <li>Menghambat perkembangan serangga</li>
                <li>Racun perut dan racun kontak</li>
                <li>Bersifat sebagai insektisida, bakterisida, nematisida dan fungisida</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True)
    with st.expander("Baca selengkapnya"):
        st.markdown(
            """
            <div class="card">
                <p><strong>Bagian tanaman yang digunakan:</strong> daun dan biji</p>
                <p><strong>Cara pembuatan:</strong></p>
                <p>Biji mindi dikupas / daun ditumbuk lalu direndam dalam air dengan konsentrasi 25 – 50 gram/l selama 24 jam, 
                Larutan yang dihasilkan disaring agar didapatkan larutan yang siap diaplikasikan</p>
                <p><strong>Cara penggunaan:</strong> Semprotkan ke seluruh bagian tanaman yang terserang</p>
            </div>""",
            unsafe_allow_html=True)

with col2:
    st.markdown(f'<h1 style="text-align: center; font-size: 25px; color: #2e5339;">Pestisida Nabati Tanaman Pacar cina</h1>', unsafe_allow_html=True)
    st.image("assets/Pacar Cina.jpg")
    st.markdown("""
        <div class="card-informasi">
            <p><strong>Efek terhadap hama:</strong></p>
            <ul>
                <li>Bersifat sebagai insektisida</li>
                <li>Penghambat makan (antifeedant)</li>
                <li>Penghambat perkembangan serangga (Growth regulator)</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True)
    with st.expander("Baca selengkapnya"):
        st.markdown(
            """
            <div class="card">
                <p><strong>Bagian tanaman yang digunakan:</strong> daun</p>
                <p><strong>Cara pembuatan:</strong></p>
                <p>Hancurkan ranting atau kulit batang pacar cina. Tambahkan 1 liter air. Didihkan selama 45 – 75 menit. Dinginkan. Tambahkan deterjen 
                aduk sampai rata. Lalu terakhir, Saring </p>
                <p><strong>Cara penggunaan:</strong> Semprotkan ke seluruh bagian tanaman yang terserang pada pagi atau sore hari</p>
            </div>""",
            unsafe_allow_html=True)

st.markdown("""<hr style="background-color: black; margin-left:5rem; margin-right:5rem;">""",unsafe_allow_html=True)

st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Tahapan Instar Larva</h1>', unsafe_allow_html=True)
st.markdown(f"""<h1 style="text-align: center; font-size: clamp(14px, 3vw, 20px); color: #2e5339; margin-left: 5rem; margin-right: 5rem;">Sebuah instar adalah sebuah tahap perkembangan pada artropoda seperti serangga. Perbedaan diantara instar umumnya dapat dilihat dari perubahan ukuran tubuh, warna, pola, dan perilaku.</h1>""", unsafe_allow_html=True)

cols = st.columns(4)

with cols[0]:
    st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Instar 1</h1>', unsafe_allow_html=True)
    st.image("assets/instar1.jpg", use_column_width=True)
    st.markdown('<div class="card">Berukuran 1.84–2.51 mm. Warna hijau muda, kepala hitam. Tubuh halus dan lebih banyak diam.</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Instar 2</h1>', unsafe_allow_html=True)
    st.image("assets/instar2.jpg", use_column_width=True)
    st.markdown('<div class="card">Berukuran 5.1–6.82 mm. Kepala coklat kemerahan. Sudah aktif makan dan merusak daun.</div>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Instar 3</h1>', unsafe_allow_html=True)
    st.image("assets/instar3.jpg", use_column_width=True)
    st.markdown('<div class="card">Berukuran 11.97–15.85 mm. Menyebar, menyerang daun bagian dalam dan pucuk tanaman.</div>', unsafe_allow_html=True)

with cols[3]:
    st.markdown('<h1 style="text-align: center; font-size: 20px; color: #2e5339;">Instar 4</h1>', unsafe_allow_html=True)
    st.image("assets/instar4.jpg", use_column_width=True)
    st.markdown('<div class="card">Berukuran 14.25–18.7 mm. Garis-garis tubuh lebih jelas. Kepala dan kaki kecoklatan.</div>', unsafe_allow_html=True)

st.markdown("""<hr style="background-color: black; margin-left:5rem; margin-right:5rem;">""",unsafe_allow_html=True)
st.markdown("""
        <div style="padding-left: 5rem; padding-right: 5rem; font-size: clamp(0.9rem, 1.5vw, 1.2rem);">
                <strong>Referensi Penjelasan:</strong><br>
                📚 Rany Badjo et al. (2015). SERANGAN HAMA ULAT KROP (Crocidolomia pavonana F.) PADA TANAMAN KUBIS (Brassica oleracea var. capitata L.) DI KELURAHAN KAKASKASEN II, KECAMATAN TOMOHON UTARA, KOTA TOMOHON. Vol. 6 No. 14 (2015). DOI: https://doi.org/10.35791/cocos.v6i14.8755<br>
                📚 Frangky J. Paat dan Jantje Pelealu. (2021). MORFOLOGI DAN PERILAKU HAMA Crocidolomia pavonana PADA TANAMAN KUBIS. Vol. 12 No. 4 (2020): EDISI OKTOBER-DESEMBER 2020. DOI: https://doi.org/10.35791/cocos.v1i1.31819<br>
                📚 Setiawati, Wiwin et al. (2008). Tumbuhan Bahan Pestisida Nabati dan Cara Pembuatannya untuk Pengendalian Organisme Pengganggu Tumbuhan (OPT). Balai Penelitian Tanaman Sayuran. Sumber: https://repository.pertanian.go.id/handle/123456789/8741<br>
                📚 Wikipedia. (n.d.). Instar. Wikipedia bahasa Indonesia. Diakses pada 4 Juni 2025, dari https://id.wikipedia.org/wiki/Instar<br>
                📚 Mirza Devara. (2017). PERILAKU KAWIN NGENGAT Crocidolomia pavonana F. UT-Faculty of Mathematics and Natural Sciences. Available at: https://repository.unej.ac.id/handle/123456789/79509
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
        <div style="padding-left: 5rem; padding-right: 5rem; padding-bottom: 5rem; font-size: clamp(0.9rem, 1.5vw, 1.2rem);">
                <strong>Sumber Gambar:</strong><br>
                📷 <strong>Crocidolomia Pavonana:</strong> https://en.wikipedia.org/wiki/Crocidolomia_pavonana<br>
                📷 <strong>Kubis:</strong> https://www.financialexpress.com/life/5-must-have-vegetables-that-must-have-this-winter-know-all-about-their-benefits-and-side-effects-3321427/<br>
                📷 <strong>Sawi:</strong> https://akcdn.detik.net.id/visual/2020/08/06/ilustrasi-tanaman-pakcoy_43.jpeg?w=720&q=90<br>
                📷 <strong>Brokoli:</strong> https://img.lovepik.com/bg/20240128/broccoli-plants-are-growing-in-the-dirt-field_3115265_wh300.jpg<br>
                📷 <strong>Lobak:</strong> https://images.genpi.co/uploads/banten/arsip/normal/2021/11/08/lobak-putih-yang-mempunyai-khasiat-luar-biasa-untuk-mencegah-8pz7.jpg<br>
                📷 <strong>Mindi:</strong> https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Starr_070302-4984_Melia_azedarach.jpg/1024px-Starr_070302-4984_Melia_azedarach.jpg<br>
                📷 <strong>Pacar Cina:</strong> https://static.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/p2/28/2024/10/22/Screenshot_274-2586125066.jpg<br>
                📷 <strong>Tahapan Instar:</strong> Risnawati, Rodiah et al. (2025). An optimized transfer learning-based approach for Crocidolomia pavonana larvae classification. IAES International Journal of Artificial Intellignce (IJ-AI): Vol. 14, No. 33. DOI: 10.11591/ijai.v14.i3.pp2270-2281 
        </div>
        """, unsafe_allow_html=True)
