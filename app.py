import streamlit as st

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

/* FONDO GENERAL */
.stApp {
    background: #f5f7fa;
}

/* HEADER SUPERIOR (no blanco feo) */
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

/* HEADER */
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

/* CARDS */
.card {
    background: white;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(0,0,0,0.15);
}

.card-accent-green {
    height: 6px;
    background: #10b981;
}

.card-accent-blue {
    height: 6px;
    background: #3b82f6;
}

.card-content {
    padding: 2rem;
}

.card-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.8rem;
}

.card-desc {
    color: #475569;
    margin-bottom: 2rem;
}

/* BOTONES REALES (anchor estilizado) */
.btn {
    display: inline-block;
    width: 100%;
    text-align: center;
    padding: 0.9rem;
    border-radius: 8px;
    font-weight: 700;
    text-decoration: none;
    color: white;
    transition: all 0.2s ease;
    box-shadow: 0 6px 14px rgba(0,0,0,0.15);
}

.btn-green {
    background: linear-gradient(135deg, #10b981, #059669);
}

.btn-green:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 28px rgba(16,185,129,0.35);
}

.btn-blue {
    background: linear-gradient(135deg, #3b82f6, #2563eb);
}

.btn-blue:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 28px rgba(59,130,246,0.35);
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
        <div class="card">
            <div class="card-accent-green"></div>
            <div class="card-content">
                <div class="card-title">Dashboard interactivo</div>
                <div class="card-desc">
                    Indicadores macroeconómicos actualizados en tiempo real
                </div>
                <div style="display:flex; gap:1rem;">
                    <a href="/2_IPC" class="btn btn-green">Ver IPC</a>
                    <a href="/4_TC_Bandas" class="btn btn-green">Ver TC y Bandas</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # CARD 2
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-accent-blue"></div>
            <div class="card-content">
                <div class="card-title">Notas</div>
                <div class="card-desc">
                    Artículos y publicaciones sobre economía argentina
                </div>
                <a href="/3_Notes" class="btn btn-blue">Ver artículos</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
