import streamlit as st

st.set_page_config(
    page_title="Francisco Fernandez Amato",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
      
      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 2rem; }

      /* Fondo más claro */
      .stApp {
        background: #1a1a1a !important;
        color: #fff;
      }

      /* Tipografía global */
      html, body, [class*="css"], p, span, div, h1, h2, h3, h4 {
        font-family: 'Inter', sans-serif !important;
        color: #fff !important;
      }

      /* Header simple */
      .home-header {
        margin-bottom: 4rem;
        padding: 0 1rem;
      }

      .home-name {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        color: #fff;
      }

      .home-role {
        font-size: 0.95rem;
        color: #888;
        margin-bottom: 1.5rem;
      }

      .home-links {
        display: flex;
        gap: 2rem;
        font-size: 0.875rem;
      }

      .home-links a {
        color: #888;
        text-decoration: none;
        transition: color 0.2s;
      }

      .home-links a:hover {
        color: #fff;
      }

      /* Cards con mismo ancho */
      .card-container {
        background: #0a0a0a;
        padding: 0;
        border-radius: 0;
        overflow: hidden;
        transition: transform 0.3s;
        position: relative;
        margin-bottom: 1.5rem;
      }

      .card-container:hover {
        transform: scale(1.02);
      }

      .card-accent {
        height: 4px;
        background: #00ff88;
      }

      .card-accent-pink {
        background: #ff0088;
      }

      .card-content {
        padding: 2rem;
      }

      .card-title {
        font-size: 1.75rem;
        font-weight: 800;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        color: #fff !important;
      }

      .card-desc {
        font-size: 0.9rem;
        line-height: 1.6;
        color: #888 !important;
        margin-bottom: 2rem;
      }

      /* Botones personalizados */
      .stButton > button {
        width: 100% !important;
        background: transparent !important;
        border: 1px solid #333 !important;
        color: #fff !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        transition: all 0.2s !important;
        text-align: left !important;
        border-radius: 0 !important;
        margin-bottom: 0.75rem !important;
      }

      .stButton > button:hover {
        border-color: #00ff88 !important;
        background: rgba(0, 255, 136, 0.05) !important;
      }

      /* Container para centrar */
      [data-testid="column"] {
        padding: 0 1rem;
      }

      @media (max-width: 768px) {
        .home-name {
          font-size: 2rem;
        }
      }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="home-header">
        <div class="home-name">Francisco Fernandez Amato</div>
        <div class="home-role">Macroeconomista</div>
        <div class="home-links">
            <a href="mailto:franciscofernandezz1999@gmail.com">Email</a>
            <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">LinkedIn</a>
            <a href="https://github.com/ffernandez-1999" target="_blank">GitHub</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# CONTENIDO - 2 CARDS EN FILA (MISMO ANCHO)
# ============================================================

left, center, right = st.columns([0.5, 10, 0.5])

with center:
    card1, card2 = st.columns(2, gap="large")
    
    with card1:
        # Card 1: Dashboard
        st.markdown(
            """
            <div class="card-container">
                <div class="card-accent"></div>
                <div class="card-content">
                    <div class="card-title">Dashboard interactivo</div>
                    <div class="card-desc">Indicadores macroeconómicos actualizados en tiempo real</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        btn1, btn2 = st.columns(2)
        with btn1:
            st.page_link("pages/2_IPC.py", label="Ver IPC", use_container_width=True)
        with btn2:
            st.page_link("pages/4_TC_Bandas.py", label="Ver TC y Bandas", use_container_width=True)
    
    with card2:
        # Card 2: Notas
        st.markdown(
            """
            <div class="card-container">
                <div class="card-accent card-accent-pink"></div>
                <div class="card-content">
                    <div class="card-title">Notas</div>
                    <div class="card-desc">Artículos y publicaciones sobre economía argentina</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.page_link("pages/3_Notes.py", label="Ver artículos", use_container_width=True)
