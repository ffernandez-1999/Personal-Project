# pages/3_Notes.py
import streamlit as st
import textwrap

st.set_page_config(
    page_title="Artículos Macro",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS - LIGHT THEME + Merriweather/Lato
# ============================================================
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');

      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      [data-testid="collapsedControl"] { display: none !important; }
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
        margin-bottom: 3rem;
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

      /* Botón de volver */
      .stButton > button {
        background: #10b981 !important;
        border: none !important;
        color: #ffffff !important;
        font-family: 'Lato', sans-serif !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 4px rgba(16, 185, 129, 0.25) !important;
      }

      .stButton > button:hover {
        background: #059669 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(16, 185, 129, 0.35) !important;
      }

      /* Contenedor ancho */
      .block-container { max-width: 1450px; }

      /* Título principal */
      .notes-title {
        font-size: 2.5rem;
        font-weight: 900;
        margin: 0 0 2rem 0;
        color: #1a1a1a;
        font-family: 'Merriweather', Georgia, serif;
        text-align: center;
      }

      /* Sidebar de notas */
      .notes-sidebar {
        position: sticky;
        top: 70px;
        padding: 1.5rem;
        border-radius: 12px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      }

      .notes-sidebar h4{
        margin: 0 0 1rem 0;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #718096;
        font-weight: 600;
        font-family: 'Lato', sans-serif;
      }

      .notes-item{
        display:block;
        padding: 1rem;
        border-radius: 8px;
        text-decoration: none !important;
        color: #1a1a1a !important;
        font-weight: 500;
        border: 1px solid #e2e8f0;
        background: white;
        margin-bottom: 0.75rem;
        transition: all .2s ease;
        font-family: 'Lato', sans-serif;
      }

      .notes-item:hover{
        border-color: #10b981;
        background: #f7fafc;
        transform: translateY(-2px);
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.15);
      }

      .notes-item .date{
        display:block;
        margin-top: 0.5rem;
        font-size: 0.75rem;
        font-weight: 400;
        color: #718096;
      }

      .note-anchor { scroll-margin-top: 100px; }

      .note-h2{
        margin: 0 0 0.5rem 0;
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a1a;
        font-family: 'Merriweather', Georgia, serif;
      }

      .note-meta{
        margin: 0 0 1rem 0;
        font-size: 0.75rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-family: 'Lato', sans-serif;
      }

      .note-text{
        margin: 0 0 1.5rem 0;
        font-size: 1rem;
        line-height: 1.7;
        color: #1a1a1a;
        font-family: 'Lato', sans-serif;
      }

      hr {
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 2rem 0;
      }

      @media (max-width: 768px) {
        .home-name {
          font-size: 2rem;
        }
        .home-links {
          flex-direction: column;
          gap: 1rem;
        }
        .notes-title {
          font-size: 2rem;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Header (igual al resto de páginas)
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
    unsafe_allow_html=True,
)

# ============================================================
# Botón volver
# ============================================================

if st.button("← Volver"):
    st.switch_page("app.py")

# ============================================================
# Notas (placeholder)
# ============================================================
NOTAS = [
    {"id": "nota-01", "titulo": "📌 Nota 1 — Tasa real y crédito", "fecha": "2026-02-12",
     "texto": "Lorem ipsum dolor sit amet: una nota corta para visualizar el layout. La idea es que acá vaya tu análisis macro."},
    {"id": "nota-02", "titulo": "💱 Nota 2 — Tipo de cambio real y competitividad", "fecha": "2026-02-05",
     "texto": "Contenido de ejemplo: discusión breve sobre TCR, pass-through y precios relativos."},
    {"id": "nota-03", "titulo": "🏭 Nota 3 — Actividad industrial y EMAE", "fecha": "2026-01-28",
     "texto": "Texto de placeholder: un párrafo sobre nivel de actividad, arrastre estadístico y señales de la industria."},
    {"id": "nota-04", "titulo": "📊 Nota 4 — Inflación núcleo vs estacionales", "fecha": "2026-01-15",
     "texto": "Ejemplo: una nota corta sobre dinámica de inflación núcleo, regulados y estacionales."},
]

# Title
st.markdown("<div class='notes-title'>Artículos Macro</div>", unsafe_allow_html=True)

# Layout (izquierda un toque más grande como pediste)
left, right = st.columns([1.5, 4], gap="large")

with left:
    items = []
    for n in NOTAS:
        items.append(
            f'<a class="notes-item" href="#{n["id"]}">{n["titulo"]}<span class="date">{n["fecha"]}</span></a>'
        )

    sidebar_html = (
        '<div class="notes-sidebar">'
        '<h4>Índice</h4>'
        + "".join(items) +
        "</div>"
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)

with right:
    for i, n in enumerate(NOTAS):
        st.markdown(
            textwrap.dedent(f"""
            <div id="{n['id']}" class="note-anchor">
              <div class="note-h2">{n['titulo']}</div>
              <div class="note-meta">{n['fecha']}</div>
              <div class="note-text">{n['texto']}</div>
            </div>
            """).strip(),
            unsafe_allow_html=True,
        )
        if i < len(NOTAS) - 1:
            st.markdown("<hr/>", unsafe_allow_html=True)
