import streamlit as st

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
    
    st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .main .block-container {
                padding-top: 2rem;
                height: 500%;
                overflow-x: hidden;
            }

    [data-testid="stFileDropzoneInstructions"].small.st-emotion-cache-7oyrr6 e1bju1570 {
        color: #2e5339;
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

    [data-testid="stSpinner"] {
        background: linear-gradient(130deg, #fdf6ec 0%, #e6f4ea 50%, #fff9c4 100%);
    }

    [data-testid="baseButton-headerNoPadding"], [data-testid="baseButton-secondary"], [data-testid="stUploadedFile"], [data-testid="stFileUploadDropzone"], [data-testid="stFileDropzoneInstructions"] {
        color:#2e5339;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] small:nth-of-type(1), [data-testid="element-container"], [data-testid="stFileUploaderDropzone"] {
        color:#2e5339;
    }

    [data-testid="baseButton-secondary"] {
        background-color: white;
    }

    # [data-testid="stSidebarUserContent"], [data-testid="stFileUploaderDropzone"], [data-testid="stSidebarHeader"] {
    #     background: linear-gradient(135deg, #e9f5db 0%, #c7e9b0 40%, #fef9c3 100%); 
    # }

    # [data-testid="stSidebarUserContent"]{
    #     height: 100%; 
    #     padding-top: 2rem;
    # }

    .banner {
        background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20230912/pngtree-the-whole-field-was-full-of-cabbages-image_13120953.png');
        background-size: cover;
        background-position: center;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .banner h1 {
        font-size: 3rem;
        color: #ffffff;
        margin: 10px;
        text-shadow: 1px 1px 3px #000;
    }
    .banner h2 {
        font-size: 1.5rem;
        color: #f0f0f0;
        margin: 0 20px;
        text-shadow: 1px 1px 2px #000;
    }
    .banner button {
        height: 45px;
        padding: 0 40px;
        border-radius: 100px;
        border: 1px solid #ffffff;
        background-color: rgba(255, 255, 255, 0.8);
        color: #1b4332;
        font-size: 16px;
        cursor: pointer;
        margin-top: 20px;
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
        border: 1px solid #2e5339;
        border-color: white;
        color: #2e5339;
        background: linear-gradient(135deg, #e9f5db 0%, #a7f6db 40%, #fef9c3 100%);
    }

    .card-informasi {
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        background: linear-gradient(135deg, #e9f5db 0%, #a7f6db 40%, #fef9c3 100%);
        border: 1px solid #2e5339;
        color: #2e5339;
        height: 250px;
    }

    [data-testid="stHeadingWithActionElements"] {
        text-align: center;
    }

    [data-testid="baseButton-secondary"] {
        border-radius: 30px;
        border: 2px solid #ffffff;
        background: linear-gradient(145deg, #fefae0, #e9f5db);
        color: #1b4332;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
        text-align: center;
        border-color:
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

    .logo-img2 {
        height: clamp(80px, 10vw, 150px);
        width: clamp(80px, 10vw, 150px);
    }

    .hero-title {
        font-size: clamp(32px, 6vw, 100px);
        margin: 20px 0 0 0;
        color: rgba(225, 225, 225, 0.01);
        background-image: url("https://www.pollybell.co.uk/wp-content/uploads/2023/06/IMG_3543-sml.jpg");
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

    </style>
    """, unsafe_allow_html=True)
    
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
