import streamlit as st

st.set_page_config(
    page_title="Francisco Fernandez Amato",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS - DARK TECH (CORREGIDO - PROPORCIONES)
# ============================================================

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap');
      
      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 1.2rem; }

      /* Variables CSS */
      :root {
        --bg-primary: #0a0e17;
        --bg-secondary: #141824;
        --bg-card: #1a1f2e;
        --accent-primary: #00d4aa;
        --accent-secondary: #0099ff;
        --text-primary: #e8eaed;
        --text-secondary: #9ba3af;
        --text-muted: #6b7280;
        --border-color: #2a3041;
      }

      /* Fondo general */
      .stApp {
        background-color: var(--bg-primary);
        background-image: 
          radial-gradient(circle at 20% 50%, rgba(0, 212, 170, 0.03) 0%, transparent 50%),
          radial-gradient(circle at 80% 80%, rgba(0, 153, 255, 0.03) 0%, transparent 50%);
        color: var(--text-primary);
      }

      /* Tipografía global */
      html, body, [class*="css"], p, span, div, h1, h2, h3, h4 {
        font-family: 'JetBrains Mono', monospace !important;
        color: var(--text-primary) !important;
      }

      /* Header central MÁS CHICO */
      .home-header {
        text-align: center;
        padding: 2rem 2rem;
        background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-secondary) 100%);
        border-radius: 16px;
        border: 1px solid var(--border-color);
        margin-bottom: 2rem;
        position: relative;
      }

      .home-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
      }

      .home-title {
        font-family: 'Syne', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.02em;
      }

      .home-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
      }

      .home-links a {
        color: var(--text-secondary);
        text-decoration: none;
        font-size: 0.875rem;
        transition: all 0.2s ease;
      }

      .home-links a:hover {
        color: var(--accent-primary);
      }

      /* Cards de contenido MÁS VISIBLES */
      [data-testid="stVerticalBlock"] > [data-testid="element-container"] > div[data-testid="stVerticalBlock"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        transition: all 0.3s ease;
      }

      [data-testid="stVerticalBlock"] > [data-testid="element-container"] > div[data-testid="stVerticalBlock"]:hover {
        border-color: var(--accent-primary) !important;
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 212, 170, 0.15);
      }

      /* Títulos de las cards */
      h4 {
        font-family: 'Syne', sans-serif !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.75rem !important;
        color: var(--text-primary) !important;
      }

      /* Párrafos */
      p {
        font-size: 0.875rem !important;
        line-height: 1.6 !important;
        color: var(--text-secondary) !important;
        margin-bottom: 1.25rem !important;
      }

      /* Botones de página MÁS VISIBLES */
      .stButton > button {
        width: 100% !important;
        background: var(--bg-secondary) !important;
        border: 1px solid var(--accent-primary) !important;
        color: var(--accent-primary) !important;
        font-family: 'JetBrains Mono', monospace !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.25rem !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
      }

      .stButton > button:hover {
        background: var(--accent-primary) !important;
        border-color: var(--accent-primary) !important;
        color: var(--bg-primary) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0, 212, 170, 0.4) !important;
      }

      /* Divider */
      hr {
        border-color: var(--border-color) !important;
        margin: 1.5rem 0 !important;
        opacity: 0.3;
      }

      /* Responsive */
      @media (max-width: 768px) {
        .home-title {
          font-size: 1.5rem !important;
        }

        .home-links {
          flex-direction: column;
          gap: 1rem;
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
        <h2 class="home-title">Francisco Fernandez Amato</h2>
        <div class="home-links">
            <a href="mailto:franciscofernandezz1999@gmail.com">📧 Gmail</a>
            <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">💼 LinkedIn</a>
            <a href="https://github.com/ffernandez-1999" target="_blank">🔗 GitHub</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# CONTENIDO
# ============================================================

left, center, right = st.columns([0.5, 8, 0.5])

with center:
    st.divider()
    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2, gap="large")
    
    with c1:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📊 Dashboard interactivo</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Indicadores macroeconómicos actualizados.</p>",
                unsafe_allow_html=True
            )
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.page_link("pages/2_IPC.py", label="Ver IPC →", use_container_width=True)
            with col_b:
                st.page_link("pages/4_TC_Bandas.py", label="Ver TC →", use_container_width=True)
    
    with c2:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📝 Notas macroeconómicas</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Artículos y publicaciones sobre economía.</p>",
                unsafe_allow_html=True
            )
            st.page_link("pages/3_Notes.py", label="Ver artículos →", use_container_width=True)
