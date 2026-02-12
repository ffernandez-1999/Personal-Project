# pages/3_Notes.py
import streamlit as st
import textwrap

st.set_page_config(
    page_title="Notas — Macro",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Oculta sidebar multipage de Streamlit (en esta page también) ---
st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      [data-testid="collapsedControl"] { display: none !important; }

      .block-container { max-width: 1400px; padding-top: 1.2rem; }
      section.main > div { padding-top: 1.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# --- CSS UI ---
st.markdown(
    """
    <style>
      :root{
        --ink:#0b2b4c;
        --muted:#526484;
        --line: rgba(15, 23, 42, 0.10);
        --card: rgba(255,255,255,0.92);
        --shadow: 0 10px 24px rgba(2,6,23,0.06);
        --shadow2: 0 6px 16px rgba(2,6,23,0.08);
        --blue: rgba(37, 99, 235, 0.35);
      }

      .notes-title { font-size: 38px; font-weight: 950; margin: 0; color: var(--ink); }
      .notes-sub   { color: var(--muted); margin: 6px 0 18px 0; font-weight: 700; font-size: 15px; }

      .notes-sidebar {
        position: sticky;
        top: 70px;
        padding: 12px;
        border-radius: 16px;
        background: var(--card);
        border: 1px solid var(--line);
        box-shadow: 0 6px 18px rgba(2,6,23,0.05);
        backdrop-filter: blur(10px);
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

# --- Volver ---
st.page_link("app.py", label="← Volver", use_container_width=False)

st.markdown("<div class='notes-title'>Notas — Macro</div>", unsafe_allow_html=True)
st.markdown("<div class='notes-sub'>Índice a la izquierda (sticky) + notas completas a la derecha</div>", unsafe_allow_html=True)

# Layout (derecha más ancha)
left, right = st.columns([1, 5], gap="large")

with left:
    # ⚠️ IMPORTANTE: SIN INDENTACIÓN para que Markdown no lo convierta en code block
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
