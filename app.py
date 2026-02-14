import streamlit as st

# ============================================================
# CONFIG
# ============================================================
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

/* Ocultar sidebar y toolbar */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }

/* Fondo */
.stApp {
    background-color: #f5f7fa;
}

/* Header superior */
header[data-testid="stHeader"] {
    background-color: #f5f7fa;
}

/* Tipografía global */
html, body, [class*="css"], p, span, div {
    font-family: 'Lato', sans-serif !important;
    color: #1a1a1a !important;
}

h1, h2, h3, h4 {
    font-family: 'Merriweather', serif !important;
    color: #1a1a1a !important;
}

/* Header principal */
.home-header {
    margin-bottom: 4rem;
    padding: 0 1rem;
}

.home-name {
    font-size: 2.8rem;
    font-weight: 900;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}

.home-role {
    font-size: 1.15rem;
    color: #4a5568;
    margin-bottom: 1.5rem;
}

.home-links {
    display: flex;
    gap: 2rem;
    font-size: 0.875rem;
}

.home-links a {
    color: #718096;
    text-decoration: none;
    transition: color 0.3s;
}

.home-links a:hover {
    color: #2d3748;
}

/* ===== CARD BUTTON STYLE ===== */
div[data-testid="stButton"] > button {
    height: 250px !important;
    border-radius: 16px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    font-family: 'Merriweather', serif !important;
    text-align: left !important;
    padding: 2.5rem !important;
    white-space: pre-line !important;
    transition: all 0.3s ease !important;
    position: relative !important;
    overflow: hidden !important;
    color: #1a1a1a !important;
}

/* Borde superior verde para primera card */
div[data-testid="column"]:nth-child(1) div[data-testid="stButton"] > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: #10b981;
}

/* Borde superior azul para segunda card */
div[data-testid="column"]:nth-child(2) div[data-testid="stButton"] > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: #3b82f6;
}

/* Hover */
div[data-testid="stButton"] > button:hover {
    transform: translateY(-8px) !important;
    box-shadow: 0 16px 35px rgba(0,0,0,0.15) !important;
}

/* Efecto hover verde para primera card */
div[data-testid="column"]:nth-child(1) div[data-testid="stButton"] > button:hover {
    box-shadow: 0 16px 35px rgba(16, 185, 129, 0.2) !important;
}

/* Efecto hover azul para segunda card */
div[data-testid="column"]:nth-child(2) div[data-testid="stButton"] > button:hover {
    box-shadow: 0 16px 35px rgba(59, 130, 246, 0.2) !important;
}

/* Container para centrar */
[data-testid="column"] {
    padding: 0 1rem;
}

@media (max-width: 768px) {
    .home-name {
        font-size: 2rem;
    }
    
    div[data-testid="stButton"] > button {
        height: 200px !important;
        font-size: 1.3rem !important;
    }
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
            "Dashboard interactivo\n\nIndicadores macroeconómicos actualizados en tiempo real",
            key="ipc",
            use_container_width=True,
        ):
            st.switch_page("pages/2_IPC.py")
    
    # NOTES CARD
    with col2:
        if st.button(
            "Notas\n\nArtículos y publicaciones sobre economía argentina",
            key="notes",
            use_container_width=True,
        ):
            st.switch_page("pages/3_Notes.py")
