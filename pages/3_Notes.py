# pages/3_Notes.py
import streamlit as st
import textwrap

st.set_page_config(
    page_title="Notas — Macro",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS GLOBAL + Header style (copiado de tu otra page)
# ============================================================
st.markdown(
    """
    <style>
      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      [data-testid="collapsedControl"] { display: none !important; }

      /* Reducir padding superior */
      section.main > div { padding-top: 1rem; }

      /* Tipografía general */
      html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      }

      /* Header personalizado */
      .custom-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.2rem;
        color: white;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
      }

      .header-title { font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; }
      .header-subtitle { font-size: 1.1rem; opacity: 0.95; font-weight: 500; }

      .header-links {
        font-size: 0.95rem;
        opacity: 0.95;
        margin-top: 0.5rem;
        white-space: nowrap;
      }

      .header-links a {
        color: white !important;
        text-decoration: none;
        margin-left: 1rem;
        font-weight: 500;
      }
      .header-links a:hover { text-decoration: underline; }

      /* Botón volver estilo violeta (HTML link) */
      .back-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.55rem 1.1rem;
        font-weight: 600;
        text-decoration: none !important;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
        transition: all 0.25s ease;
      }
      .back-btn:hover{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
      }

      /* Contenedor ancho como venías usando */
      .block-container { max-width: 1450px; }

      /* ====== Estilos de Notas (los tuyos) ====== */
      :root{
        --ink:#0b2b4c;
        --muted:#5b6b82;
        --line: rgba(15, 23, 42, 0.10);
        --card: rgba(255,255,255,0.92);
        --shadow: 0 6px 18px rgba(2,6,23,0.05);
        --hover: rgba(37, 99, 235, 0.25);
      }

      .notes-title {
        font-size: 40px;
        font-weight: 800;
        margin: 0;
        color: var(--ink);
      }

      .notes-sub {
        color: var(--muted);
        margin: 6px 0 22px 0;
        font-size: 15px;
      }

      .notes-sidebar {
        position: sticky;
        top: 70px;
        padding: 16px;
        border-radius: 18px;
        background: var(--card);
        border: 1px solid var(--line);
        box-shadow: var(--shadow);
      }

      .notes-sidebar h4{
        margin: 0 0 14px 2px;
        font-size: 12px;
        letter-spacing: .4px;
        text-transform: uppercase;
        color: var(--muted);
        font-weight: 600;
      }

      .notes-item{
        display:block;
        padding: 14px 14px;
        border-radius: 16px;
        text-decoration: none !important;
        color: var(--ink) !important;
        font-weight: 500;
        border: 1px solid rgba(15, 23, 42, 0.08);
        background: white;
        margin-bottom: 12px;
        transition: all .15s ease;
      }

      .notes-item:hover{
        border-color: var(--hover);
        transform: translateY(-1px);
      }

      .notes-item .date{
        display:block;
        margin-top: 6px;
        font-size: 12px;
        font-weight: 400;
        color: #6b7280;
      }

      .note-anchor { scroll-margin-top: 100px; }

      .note-h2{
        margin: 0 0 6px 0;
        font-size: 26px;
        font-weight: 700;
        color: var(--ink);
      }

      .note-meta{
        margin: 0 0 12px 0;
        font-size: 12px;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: .4px;
      }

      .note-text{
        margin: 0 0 16px 0;
        font-size: 16px;
        line-height: 1.65;
        color: var(--ink);
      }

      hr {
        border: none;
        border-top: 1px solid rgba(15, 23, 42, 0.12);
        margin: 26px 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Header (igual al tuyo)
# ============================================================
st.markdown(
    """
    <div class="custom-header">
        <div style="display:flex; justify-content:space-between; align-items:center; gap: 18px;">
            <div>
                <div class="header-title">Francisco Fernandez Amato</div>
                <div class="header-subtitle">Macroeconomista</div>
            </div>
            <div class="header-links">
                <a href="mailto:franciscofernandezz1999@gmail.com">📧 Email</a>
                <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">💼 LinkedIn</a>
                <a href="https://github.com/ffernandez-1999" target="_blank">🔗 GitHub</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Botón volver (link estable)
# - "/" vuelve al Home (app.py) en la mayoría de deployments
# - si querés otro destino, cambiá href
# ============================================================
st.markdown(
    """
    <a class="back-btn" href="/">← Volver</a>
    """,
    unsafe_allow_html=True,
)

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
st.markdown("<div class='notes-title'>Notas — Macro</div>", unsafe_allow_html=True)
st.markdown("<div class='notes-sub'>Índice a la izquierda (sticky) + notas completas a la derecha</div>", unsafe_allow_html=True)

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
