import streamlit as st

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Francisco Fernandez Amato",
    layout="wide",
)

# ============================================================
# CSS GLOBAL
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');

/* Ocultar sidebar */
[data-testid="stSidebar"] { display: none !important; }

/* Fondo */
.stApp {
    background: #f5f7fa;
}

/* Header superior */
header[data-testid="stHeader"] {
    background: #f5f7fa;
}

/* Tipografía */
html, body {
    font-family: 'Lato', sans-serif;
    color: #1a1a1a;
}

h1, h2, h3 {
    font-family: 'Merriweather', serif;
}

/* Header */
.home-header {
    margin-bottom: 4rem;
}

.home-name {
    font-size: 2.8rem;
    font-weight: 900;
}

.home-role {
    font-size: 1.15rem;
    color: #475569;
    margin-bottom: 1.5rem;
}

.home-links {
    display: flex;
    gap: 2rem;
}

.home-links a {
    color: #64748b;
    text-decoration: none;
}

.home-links a:hover {
    color: #0f172a;
}

/* CARD BUTTON STYLE */
div[data-testid="stButton"] > button {
    height: 220px;
    border-radius: 18px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 10px 28px rgba(0,0,0,0.08) !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    text-align: left !important;
    padding: 2.2rem !important;
    white-space: pre-line !important;
    transition: all 0.3s ease !important;
    position: relative !important;
}

/* Hover */
div[data-testid="stButton"] > button:hover {
    transform: translateY(-8px) !important;
    box-shadow: 0 22px 50px rgba(0,0,0,0.18) !important;
}

/* Línea verde IPC */
div[data-testid="stButton"] > button[key="ipc"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 6px;
    background: #10b981;
    border-radius: 18px 18px 0 0;
}

/* Línea azul Notes */
div[data-testid="stButton"] > button[key="notes"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 6px;
    background: #3b82f6;
    border-radius: 18px 18px 0 0;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="home-header">
    <div class="home-name">Francisco Fernandez Amato</div>
    <div class="home-role">Macroeconomista</div>
    <div class="home-links">
        <a href="mailto:franciscofernandezz1999@gmail.com">Email</a>
        <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">LinkedIn</a>
        <a href="https://github.com/ffernandez-1999" target="_blank">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CARDS
# ============================================================

left, center, right = st.columns([0.5, 10, 0.5])

with center:
    col1, col2 = st.columns(2, gap="large")

    # IPC CARD
    with col1:
        if st.button(
            "IPC Canasta 2017/18\n\nSeguimiento interactivo del IPC base ENGHo 2017/18.",
            key="ipc",
            use_container_width=True,
        ):
            st.switch_page("pages/2_IPC.py")

    # NOTES CARD
    with col2:
        if st.button(
            "Notas\n\nArtículos y publicaciones sobre economía argentina.",
            key="notes",
            use_container_width=True,
        ):
            st.switch_page("pages/3_Notes.py")
