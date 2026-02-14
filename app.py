import streamlit as st

st.set_page_config(
    page_title="Francisco Fernandez Amato",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');
      
      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 2rem; }
      
      /* Ocultar/aclarar header de Streamlit */
      header[data-testid="stHeader"] {
        background-color: #f5f7fa !important;
      }
      
      /* Ocultar toolbar arriba */
      [data-testid="stToolbar"] {
        display: none !important;
      }

      /* Fondo claro */
      .stApp {
        background: #f5f7fa !important;
        color: #1a1a1a;
      }

      /* Tipografía global */
      html, body, [class*="css"], p, span, div {
        font-family: 'Lato', sans-serif !important;
        color: #1a1a1a !important;
      }
      
      h1, h2, h3, h4 {
        font-family: 'Merriweather', Georgia, serif !important;
        color: #1a1a1a !important;
      }

      /* Header simple */
      .home-header {
        margin-bottom: 4rem;
        padding: 0 1rem;
      }

      .home-name {
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        color: #1a1a1a;
        font-family: 'Merriweather', Georgia, serif;
      }

      .home-role {
        font-size: 1.1rem;
        color: #4a5568;
        margin-bottom: 1.5rem;
        font-family: 'Lato', sans-serif;
      }

      .home-links {
        display: flex;
        gap: 2rem;
        font-size: 0.875rem;
      }

      .home-links a {
        color: #718096;
        text-decoration: none;
        transition: color 0.2s;
        font-family: 'Lato', sans-serif;
      }

      .home-links a:hover {
        color: #2d3748;
      }

      /* Cards con mismo ancho */
      .card-container {
        background: #ffffff;
        padding: 0;
        border-radius: 12px;
        overflow: hidden;
        transition: all 0.3s;
        position: relative;
        margin-bottom: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      }

      .card-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
      }

      .card-accent {
        height: 4px;
        background: #10b981;
      }

      .card-accent-pink {
        background: #3b82f6;
      }

      .card-content {
        padding: 2rem;
      }

      .card-title {
        font-size: 1.75rem;
        font-weight: 700;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        color: #1a1a1a !important;
        font-family: 'Merriweather', Georgia, serif !important;
      }

      .card-desc {
        font-size: 0.95rem;
        line-height: 1.6;
        color: #4a5568 !important;
        margin-bottom: 2rem;
        font-family: 'Lato', sans-serif !important;
      }

      /* Botones personalizados */
      .stButton > button {
        width: 100% !important;
        background: #10b981 !important;
        border: 2px solid #10b981 !important;
        color: #ffffff !important;
        padding: 0.875rem 1rem !important;
        font-family: 'Lato', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
        text-align: center !important;
        border-radius: 8px !important;
        margin-bottom: 0.75rem !important;
        box-shadow: 0 2px 4px rgba(16, 185, 129, 0.2) !important;
      }

      .stButton > button:hover {
        background: #059669 !important;
        border-color: #059669 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(16, 185, 129, 0.3) !important;
      }
      
      /* Botones en la segunda columna (Notas) */
      [data-testid="column"]:nth-child(2) .stButton > button {
        background: #3b82f6 !important;
        border-color: #3b82f6 !important;
        box-shadow: 0 2px 4px rgba(59, 130, 246, 0.2) !important;
      }
      
      [data-testid="column"]:nth-child(2) .stButton > button:hover {
        background: #2563eb !important;
        border-color: #2563eb !important;
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.3) !important;
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
