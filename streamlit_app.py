import streamlit as st
from styles.main_style import main_style

st.set_page_config(layout="wide", page_title="CrociDetect", initial_sidebar_state="auto", page_icon="🍃")

if 'start_app' not in st.session_state:
    st.session_state.start_app = False

if not st.session_state.start_app:
    try:
        with open("pages/Homepage.py", "r") as f:
            exec(f.read())
    except FileNotFoundError:
        st.error("Error: homepage.py not found.")
else:
    
    main_style()
    
    app = st.Page(
        "pages/main.py",
        title="Aplikasi",
        icon="🧠",
        default=True
    )

    history = st.Page(
        "pages/history.py",
        title="Riwayat Klasifikasi",
        icon="📃"
    )
    
    information = st.Page(
        "pages/Information.py",
        title="Mengenai Crocidolomia Pavonana",
        icon="🐛"
    )
    
    guide = st.Page(
        "pages/guide.py",
        title="Cara Penggunaan Aplikasi",
        icon="❓"
    )

    pg = st.navigation([app, history, information, guide])

    st.logo("assets/logo.png", icon_image="assets/logo.png")


    pg.run()
