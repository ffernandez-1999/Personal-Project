import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Notes — Macro", layout="wide", initial_sidebar_state="collapsed")

# --- OCULTA el sidebar multipage + nav (hay que hacerlo en CADA page) ---
st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      /* botón colapsar sidebar (a veces aparece igual) */
      [data-testid="collapsedControl"] { display: none !important; }

      section.main > div { padding-top: 1.2rem; }
      .block-container { max-width: 1200px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# DATA (placeholder)
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
# CSS (look)
# ============================================================
st.markdown(
    """
    <style>
      .notes-title { font-size: 34px; font-weight: 900; margin: 0 0 6px 0; color: #0b2b4c; }
      .notes-sub { color: #526484; margin: 0 0 18px 0; font-weight: 650; }

      /* Sidebar (índice) */
      .notes-sidebar {
        position: sticky;
        top: 76px;
        padding: 12px 12px 14px 12px;
        border-radius: 14px;
        background: rgba(255,255,255,0.85);
        border: 1px solid rgba(15, 23, 42, 0.10);
        backdrop-filter: blur(8px);
      }
      .notes-sidebar h4{
        margin: 0 0 10px 0;
        font-size: 13px;
        letter-spacing: .2px;
        text-transform: uppercase;
        color: #526484;
        font-weight: 800;
      }
      .notes-link{
        display: block;
        padding: 10px 10px;
        border-radius: 12px;
        text-decoration: none;
        color: #0b2b4c;
        font-weight: 800;
        border: 1px solid rgba(15, 23, 42, 0.08);
        background: rgba(255,255,255,0.95);
        margin-bottom: 8px;
        transition: all .15s ease;
      }
      .notes-link:hover{
        transform: translateY(-1px);
        border-color: rgba(37, 99, 235, 0.35);
        box-shadow: 0 6px 16px rgba(2, 6, 23, 0.08);
      }
      .notes-date{
        display: block;
        margin-top: 3px;
        font-size: 12px;
        font-weight: 750;
        color: #6b7280;
      }

      /* Contenido */
      .note-card{
        padding: 16px 18px;
        border-radius: 16px;
        background: rgba(255,255,255,0.98);
        border: 1px solid rgba(15, 23, 42, 0.10);
        box-shadow: 0 10px 24px rgba(2,6,23,0.06);
        margin-bottom: 14px;
      }
      .note-h2{
        margin: 0 0 6px 0;
        font-size: 22px;
        font-weight: 950;
        color: #0b2b4c;
      }
      .note-meta{
        margin: 0 0 10px 0;
        font-size: 12px;
        font-weight: 850;
        color: #526484;
        text-transform: uppercase;
        letter-spacing: .3px;
      }
      .note-text{
        margin: 0;
        font-size: 15px;
        line-height: 1.55;
        color: #0b2b4c;
        font-weight: 650;
      }

      /* Para que al saltar no quede tapado */
      .anchor-offset { scroll-margin-top: 90px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# UI
# ============================================================
st.markdown("<div class='notes-title'>Notas — Macro</div>", unsafe_allow_html=True)
st.markdown("<div class='notes-sub'>Índice a la izquierda (sticky) + notas completas a la derecha</div>", unsafe_allow_html=True)

left, right = st.columns([1, 3], gap="large")

# ----- Sidebar índice (RENDER SEGURO con components.html) -----
with left:
    items = []
    for n in NOTAS:
        items.append(
            f"""
            <a class="notes-link" href="#{n['id']}">
              {n['titulo']}
              <span class="notes-date">{n['fecha']}</span>
            </a>
            """
        )

    sidebar_html = f"""
    <div class="notes-sidebar">
      <h4>Índice</h4>
      {''.join(items)}
    </div>
    """

    # 👇 Esto evita que Streamlit lo muestre como texto
    components.html(sidebar_html, height=520, scrolling=False)

# ----- Contenido -----
with right:
    for n in NOTAS:
        st.markdown(
            f"""
            <div id="{n['id']}" class="note-card anchor-offset">
              <div class="note-h2">{n['titulo']}</div>
              <div class="note-meta">{n['fecha']}</div>
              <p class="note-text">{n['texto']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
