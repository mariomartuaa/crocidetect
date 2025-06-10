import streamlit as st

def home_style():
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