import streamlit as st

# === GAMBAR CROCIDILOMIA DEWASA ===

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write(' ')

# with col2:
#     st.image("assets/crocidolomia_adult.jpg")

# with col3:
#     st.write(' ')
    

st.markdown('<div style="display: flex; justify-content: center;"><img src="https://i.imgur.com/9zNBhxV.png" alt="Alternative text" style="height: 40%;"></div>', unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Crocidolomia Pavonana</h1>', unsafe_allow_html=True)

# === PENJELASAN ILMIAH ===
# === INFORMASI PENTING (Menyamping 2 kolom seperti fitur utama) ===
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
                <li>Kerusakan hingga 100%pada musim kemarau.</li>
                <li>Larva memakan daun hingga tersisa tulangnya saja.</li>
                <li>Mengakibatkan <strong>gagal panen total jika tidak dikendalikan.</li>
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

# === INSTAR SEBAGAI KARTU ===
st.markdown(f'<h1 style="text-align: center; font-size: 40px; color: #2e5339;">Tahapan Instar Larva</h1>', unsafe_allow_html=True)
instar_data = [
    {
        "title": "Instar 1",
        "img": "assets/instar1.jpg",
        "desc": "Ukuran 1.84–2.51 mm. Warna hijau muda, kepala hitam. Tubuh halus dan lebih banyak diam."
    },
    {
        "title": "Instar 2",
        "img": "assets/instar2.jpg",
        "desc": "Ukuran 5.1–6.82 mm. Kepala coklat kemerahan. Sudah aktif makan dan merusak daun."
    },
    {
        "title": "Instar 3",
        "img": "assets/instar3.jpg",
        "desc": "Ukuran 11.97–15.85 mm. Menyebar, menyerang daun bagian dalam dan pucuk tanaman."
    },
    {
        "title": "Instar 4",
        "img": "assets/instar4.jpg",
        "desc": "Ukuran 14.25–18.7 mm. Garis-garis tubuh lebih jelas. Kepala dan kaki kecoklatan."
    }
]

cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.markdown(f'<h1 style="text-align: center; font-size: 20px; color: #2e5339;">{instar_data[i]["title"]}</h1>', unsafe_allow_html=True)
        st.image(instar_data[i]["img"], use_column_width=True)
        st.markdown(f'<div class="card">{instar_data[i]["desc"]}</div>', unsafe_allow_html=True)

# === FOOTER ===
st.markdown("""<hr style="background-color: black; margin-left:5rem; margin-right:5rem;">""",unsafe_allow_html=True)
st.markdown("""
        <div style="padding-left: 5rem; padding-right: 5rem; padding-bottom: 5rem; font-size: clamp(0.9rem, 1.5vw, 1.2rem);">
                Penjelasan Berdasarkan Penelitian:<br>
                📚 Rany Badjo et al. (2015). SERANGAN HAMA ULAT KROP (Crocidolomia pavonana F.) PADA TANAMAN KUBIS (Brassica oleracea var. capitata L.) DI KELURAHAN KAKASKASEN II, KECAMATAN TOMOHON UTARA, KOTA TOMOHON. Vol. 6 No. 14 (2015). DOI: https://doi.org/10.35791/cocos.v6i14.8755<br>
                📚 Frangky J. Paat dan Jantje Pelealu. (2021). MORFOLOGI DAN PERILAKU HAMA Crocidolomia pavonana PADA TANAMAN KUBIS. Vol. 12 No. 4 (2020): EDISI OKTOBER-DESEMBER 2020. DOI: https://doi.org/10.35791/cocos.v1i1.31819<br>
                📚 Mirza Devara. (2017). PERILAKU KAWIN NGENGAT Crocidolomia pavonana F. UT-Faculty of Mathematics and Natural Sciences. Available at: https://repository.unej.ac.id/handle/123456789/79509
        </div>
        """, unsafe_allow_html=True)
