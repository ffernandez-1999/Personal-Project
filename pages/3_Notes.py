# pages/3_Notes.py
import streamlit as st

# ============================================================
# Page config
# ============================================================
st.set_page_config(
    page_title="Notas — Macro",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# Hide Streamlit multipage sidebar (hay que hacerlo en cada page)
# ============================================================
st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      [data-testid="collapsedControl"] { display: none !important; }

      /* más ancho el contenido */
      .block-container { max-width: 1400px; padding-top: 1.2rem; }
      section.main > div { padding-top: 1.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Data (placeholder)
# ============================================================
NOTAS = [
    {
        "id": "nota-01",
        "titulo": "📌 Nota 1 — Tasa real y crédito",
        "fecha": "2026-02-12",
        "texto": "Lorem ipsum dolor sit amet: una nota corta para visualizar el layout. La idea es que acá vaya tu análisis macro.",
    },
    {
        "id": "nota-02",
        "titulo": "💱 Nota 2 — Tipo de cambio real y competitividad",
        "fecha": "2026-02-05",
        "texto": "Contenido de ejemplo: discusión breve sobre TCR, pass-through y precios relativos.",
    },
    {
        "id": "nota-03",
        "titulo": "🏭 Nota 3 — Actividad industrial y EMAE",
        "fecha": "2026-01-28",
        "texto": "Texto de placeholder: un párrafo sobre nivel de actividad, arrastre estadístico y señales de la industria.",
    },
    {
        "id": "nota-04",
        "titulo": "📊 Nota 4 — Inflación núcleo vs estacionales",
        "fecha": "2026-01-15",
        "texto": "Ejemplo: una nota corta sobre dinámica de inflación núcleo, regulados y estacionales.",
    },
]

# ============================================================
# CSS (aplica a todo porque NO usamos iframe)
# ============================================================
st.markdown(
    """
    <style>
      :root{
        --ink:#0b2b4c;
        --muted:#526484;
        --line: rgba(15, 23, 42, 0.10);
        --card: rgba(255,255,255,0.98);
        --shadow: 0 10px 24px rgba(2,6,23,0.06);
        --shadow2: 0 6px 16px rgba(2,6,23,0.08);
        --blue: rgba(37, 99, 235, 0.35);
      }

      /* Top */
      .notes-title { font-size: 38px; font-weight: 950; margin: 0; color: var(--ink); }
      .notes-sub { color: var(--muted); margin: 6px 0 18px 0; font-weight: 700; font-size: 15px; }

      /* Back button look (for st.page_link wrapper) */
      .back-wrap {
        display:flex;
        justify-content:flex-start;
        margin-bottom: 8px;
      }
      .back-wrap a, .back-wrap button {
        font-weight: 850 !important;
      }

      /* Sidebar */
      .notes-sidebar {
        position: sticky;
        top: 70px;
        padding: 12px;
        border-radius: 16px;
        background: rgba(255,255,255,0.88);
        border: 1px solid var(--line);
        backdrop-filter: blur(10px);
        box-shadow: 0 6px 18px rgba(2,6,23,0.05);
      }
      .notes-sidebar h4{
        margin: 0 0 10px 2px;
        font-size: 12px;
        letter-spacing: .35px;
        text-transform: uppercase;
        color: var(--muted);
        font-weight: 900;
      }

      .notes-item{
        display:block;
        padding: 10px 10px;
        border-radius: 14px;
        text-decoration: none !important;
        color: var(--ink) !important;
        font-weight: 900;
        border: 1px solid rgba(15, 23, 42, 0.08);
        background: rgba(255,255,255,0.98);
        margin-bottom: 8px;
        transition: all .15s ease;
        line-height: 1.25;
      }
      .notes-item:hover{
        transform: translateY(-1px);
        border-color: var(--blue);
        box-shadow: var(--shadow2);
      }
      .notes-item .date{
        display:block;
        margin-top: 4px;
        font-size: 12px;
        font-weight: 800;
        color: #6b7280;
      }

      /* Right content */
      .note-anchor { scroll-margin-top: 92px; }
      .note-h2{
        margin: 0 0 6px 0;
        font-size: 26px;
        font-weight: 950;
        color: var(--ink);
      }
      .note-meta{
        margin: 0 0 12px 0;
        font-size: 12px;
        font-weight: 900;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: .35px;
      }
      .note-text{
        margin: 0 0 14px 0;
        font-size: 15px;
        line-height: 1.62;
        color: var(--ink);
        font-weight: 650;
      }
      hr {
        border: none;
        border-top: 1px solid rgba(15, 23, 42, 0.10);
        margin: 18px 0 18px 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Back button (estable)
# ============================================================
st.markdown("<div class='back-wrap'>", unsafe_allow_html=True)
st.page_link("app.py", label="← Volver", use_container_width=False)
st.markdown("</div>", unsafe_allow_html=True)

# Title
st.markdown("<div class='notes-title'>Notas — Macro</div>", unsafe_allow_html=True)
st.markdown("<div class='notes-sub'>Índice a la izquierda (sticky) + notas completas a la derecha</div>", unsafe_allow_html=True)

# ============================================================
# Layout: derecha más ancha
# ============================================================
left, right = st.columns([1, 5], gap="large")

# Sidebar index (SIN iframe, CSS aplica bien)
with left:
    items_html = []
    for n in NOTAS:
        items_html.append(
            f"""
            <a class="notes-item" href="#{n['id']}">
              {n['titulo']}
              <span class="date">{n['fecha']}</span>
            </a>
            """
        )

    st.markdown(
        f"""
        <div class="notes-sidebar">
          <h4>Índice</h4>
          {''.join(items_html)}
        </div>
        """,
        unsafe_allow_html=True,
    )

# Right content (simple + divider)
with right:
    for i, n in enumerate(NOTAS):
        st.markdown(
            f"""
            <div id="{n['id']}" class="note-anchor">
              <div class="note-h2">{n['titulo']}</div>
              <div class="note-meta">{n['fecha']}</div>
              <div class="note-text">{n['texto']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if i < len(NOTAS) - 1:
            st.markdown("<hr/>", unsafe_allow_html=True)
