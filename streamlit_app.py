import streamlit as st

st.set_page_config(layout="wide", page_title="Instar", initial_sidebar_state="auto")

if 'start_app' not in st.session_state:
    st.session_state.start_app = False

if not st.session_state.start_app:
    try:
        with open("pages/homepage.py", "r") as f:
            exec(f.read())
    except FileNotFoundError:
        st.error("Error: homepage.py not found.")
else:
    st.markdown("""
        <style>
        div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
            height: 3rem;
            width: auto;
        }
        
        div[data-testid="stSidebarHeader"], div[data-testid="stSidebarHeader"] > *,
        div[data-testid="collapsedControl"], div[data-testid="collapsedControl"] > * {
            display: flex;
            align-items: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    app = st.Page(
        "pages/main.py",
        title="Aplikasi",
        default=True
    )

    history = st.Page(
        "pages/history.py",
        title="Riwayat Klasifikasi"
    )
    
    information = st.Page(
        "pages/information.py",
        title="Mengenai Crocidolomia Pavonana"
    )
    
    guide = st.Page(
        "pages/guide.py",
        title="Cara Penggunaan Aplikasi"
    )

    pg = st.navigation([app, history, information, guide])

    st.logo("assets/logo.png", icon_image="assets/logo.png")


    pg.run()