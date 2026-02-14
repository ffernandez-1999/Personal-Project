import streamlit as st

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
    font-size: 2.6rem;
    font-weight: 900;
}

.home-role {
    font-size: 1.1rem;
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

/* CARD ESTÉTICA */
.card-box {
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    height: 210px;
    padding: 2rem;
}

.card-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 45px rgba(0,0,0,0.18);
}

.card-accent-green {
    height: 6px;
    background: #10b981;
    border-radius: 16px 16px 0 0;
    margin: -2rem -2rem 1.5rem -2rem;
}

.card-accent-blue {
    height: 6px;
    background: #3b82f6;
    border-radius: 16px 16px 0 0;
    margin: -2rem -2rem 1.5rem -2rem;
}

.card-title {
    font-size: 1.6rem;
    font-weight: 700;
    margin-bottom: 0.7rem;
}

.card-desc {
    color: #475569;
    font-size: 0.95rem;
}

/* BOTÓN INVISIBLE QUE CUBRE TODA LA CARD */
.card-button > button {
    position: absolute !important;
    width: 100% !important;
    height: 210px !important;
    opacity: 0 !important;
    border-radius: 16px !important;
    cursor: pointer !important;
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

    # CARD IPC
    with col1:
        container = st.container()
        with container:
            st.markdown('<div class="card-box">', unsafe_allow_html=True)
            st.markdown('<div class="card-accent-green"></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">IPC Canasta 2017/18</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-desc">Seguimiento interactivo del IPC base ENGHo 2017/18.</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card-button">', unsafe_allow_html=True)
        if st.button("", key="ipc_card"):
            st.switch_page("pages/2_IPC.py")
        st.markdown('</div>', unsafe_allow_html=True)

    # CARD NOTES
    with col2:
        container = st.container()
        with container:
            st.markdown('<div class="card-box">', unsafe_allow_html=True)
            st.markdown('<div class="card-accent-blue"></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">Notas</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-desc">Artículos y publicaciones sobre economía argentina.</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card-button">', unsafe_allow_html=True)
        if st.button("", key="notes_card"):
            st.switch_page("pages/3_Notes.py")
        st.markdown('</div>', unsafe_allow_html=True)
