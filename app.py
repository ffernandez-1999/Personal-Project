import streamlit as st

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Francisco Fernandez Amato",
    layout="wide",
)

# ============================================================
# CSS
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

/* Header */
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

/* ================= HEADER ================= */

.home-header {
    margin-bottom: 5rem;
}

.home-name {
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 0.4rem;
}

.home-role {
    font-size: 1.2rem;
    color: #4a5568;
    margin-bottom: 1.5rem;
}

.home-links {
    display: flex;
    gap: 2rem;
}

.home-links a {
    color: #6b7280;
    text-decoration: none;
    font-weight: 500;
}

.home-links a:hover {
    color: #10b981;
}

/* ================= CARDS ================= */

div[data-testid="stButton"] > button {
    height: 250px;
    border-radius: 18px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 12px 30px rgba(0,0,0,0.07) !important;
    text-align: left !important;
    padding: 2.5rem !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    white-space: pre-line !important;
    transition: all 0.3s ease !important;
    position: relative !important;
}

/* Barra verde superior */
div[data-testid="stButton"] > button::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 6px;
    width: 100%;
    background: #10b981;
    border-radius: 18px 18px 0 0;
}

/* Hover elegante */
div[data-testid="stButton"] > button:hover {
    transform: translateY(-10px) !important;
    box-shadow: 0 28px 60px rgba(16,185,129,0.25) !important;
}

/* Texto secundario */
div[data-testid="stButton"] > button span {
    font-size: 1rem !important;
    font-weight: 400 !important;
    color: #4a5568 !important;
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
# CARDS (3 SIMÉTRICAS)
# ============================================================

left, center, right = st.columns([1, 12, 1])

with center:
    col1, col2, col3 = st.columns(3, gap="large")

    # IPC
    with col1:
        if st.button(
            "IPC Canasta 2017/18\n\nSeguimiento interactivo del IPC base ENGHo 2017/18.",
            key="ipc",
            use_container_width=True,
        ):
            st.switch_page("pages/2_IPC.py")

    # TC
    with col2:
        if st.button(
            "Tipo de Cambio y Bandas\n\nAnálisis del tipo de cambio oficial, paralelo y esquema de bandas.",
            key="tc",
            use_container_width=True,
        ):
            st.switch_page("pages/4_TC_Bandas.py")

    # NOTES
    with col3:
        if st.button(
            "Notas\n\nArtículos y publicaciones sobre economía argentina.",
            key="notes",
            use_container_width=True,
        ):
            st.switch_page("pages/3_Notes.py")
