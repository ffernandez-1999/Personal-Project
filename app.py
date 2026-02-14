import streamlit as st

st.set_page_config(
    page_title="Francisco Fernandez Amato",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');

/* Ocultar sidebar */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stSidebarNav"] { display: none !important; }

/* Fondo */
.stApp {
    background: #f5f7fa !important;
}

/* Tipografía */
html, body, [class*="css"] {
    font-family: 'Lato', sans-serif !important;
    color: #1a1a1a !important;
}

h1, h2, h3 {
    font-family: 'Merriweather', serif !important;
}

/* Header */
.home-header {
    margin-bottom: 4rem;
}

.home-name {
    font-size: 2.5rem;
    font-weight: 900;
}

.home-role {
    font-size: 1.1rem;
    color: #4a5568;
    margin-bottom: 1.5rem;
}

.home-links {
    display: flex;
    gap: 2rem;
    font-size: 0.9rem;
}

.home-links a {
    color: #64748b;
    text-decoration: none;
}

.home-links a:hover {
    color: #1e293b;
}

/* Cards */
.card-container {
    background: white;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

.card-container:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

.card-accent {
    height: 5px;
    background: #10b981;
}

.card-accent-blue {
    background: #3b82f6;
}

.card-content {
    padding: 2rem;
}

.card-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
}

.card-desc {
    color: #475569;
    margin-bottom: 1.5rem;
}

/* BOTONES */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #10b981, #059669) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
    padding: 0.9rem !important;
    box-shadow: 0 6px 14px rgba(16,185,129,0.35) !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 10px 22px rgba(16,185,129,0.45) !important;
}

/* Botón azul */
.blue-button .stButton > button {
    background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
    box-shadow: 0 6px 14px rgba(59,130,246,0.35) !important;
}

.blue-button .stButton > button:hover {
    box-shadow: 0 10px 22px rgba(59,130,246,0.45) !important;
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

    # CARD 1
    with col1:
        st.markdown("""
        <div class="card-container">
            <div class="card-accent"></div>
            <div class="card-content">
                <div class="card-title">Dashboard interactivo</div>
                <div class="card-desc">
                    Indicadores macroeconómicos actualizados en tiempo real
                </div>
        """, unsafe_allow_html=True)

        btn1, btn2 = st.columns(2)
        with btn1:
            st.page_link("pages/2_IPC.py", label="Ver IPC", use_container_width=True)
        with btn2:
            st.page_link("pages/4_TC_Bandas.py", label="Ver TC y Bandas", use_container_width=True)

        st.markdown("</div></div>", unsafe_allow_html=True)

    # CARD 2
    with col2:
        st.markdown("""
        <div class="card-container">
            <div class="card-accent card-accent-blue"></div>
            <div class="card-content">
                <div class="card-title">Notas</div>
                <div class="card-desc">
                    Artículos y publicaciones sobre economía argentina
                </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="blue-button">', unsafe_allow_html=True)
        st.page_link("pages/3_Notes.py", label="Ver artículos", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div></div>", unsafe_allow_html=True)
