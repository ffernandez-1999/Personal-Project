# pages/notas_macro.py
import streamlit as st

# ============================================================
# Notas Macro — Sidebar sticky + contenido scrolleable
# ============================================================

NOTAS = [
    {
        "id": "nota-01",
        "titulo": "📌 Nota 1 — Tasa real y crédito",
        "fecha": "2026-02-12",
        "texto": "Lorem ipsum dolor sit amet: una nota corta para visualizar el layout. "
                 "La idea es que acá vaya tu análisis macro con 1–2 párrafos, gráficos y bullets si querés.",
    },
    {
        "id": "nota-02",
        "titulo": "💱 Nota 2 — Tipo de cambio real y competitividad",
        "fecha": "2026-02-05",
        "texto": "Contenido de ejemplo: discusión breve sobre TCR, pass-through y precios relativos. "
                 "Esto solo sirve para ver cómo queda el scroll y el salto por anclas.",
    },
    {
        "id": "nota-03",
        "titulo": "🏭 Nota 3 — Actividad industrial y EMAE",
        "fecha": "2026-01-28",
        "texto": "Texto de placeholder: un párrafo sobre nivel de actividad, arrastre estadístico y señales "
                 "de la industria. Luego lo reemplazás por tu nota real.",
    },
    {
        "id": "nota-04",
        "titulo": "📊 Nota 4 — Inflación núcleo vs estacionales",
        "fecha": "2026-01-15",
        "texto": "Ejemplo: una nota corta sobre dinámica de inflación núcleo, regulados y estacionales. "
                 "Acá iría tu lectura y riesgos para los próximos meses.",
    },
]


def _inject_css():
    st.markdown(
        """
        <style>
          /* Layout */
          .notes-wrap { max-width: 1200px; margin: 0 auto; padding-top: 6px; }
          .notes-title { font-size: 28px; font-weight: 800; margin: 0 0 6px 0; }
          .notes-subtitle { color: #526484; margin: 0 0 16px 0; font-weight: 600; }

          /* Sidebar sticky */
          .notes-sidebar {
            position: sticky;
            top: 76px; /* ajusta si tenés header fijo */
            padding: 12px 12px 14px 12px;
            border-radius: 14px;
            background: rgba(255,255,255,0.7);
            border: 1px solid rgba(15, 23, 42, 0.08);
            backdrop-filter: blur(8px);
          }
          .notes-sidebar h4{
            margin: 0 0 10px 0;
            font-size: 14px;
            letter-spacing: .2px;
            text-transform: uppercase;
            color: #526484;
          }
          .notes-link{
            display: block;
            padding: 10px 10px;
            border-radius: 12px;
            text-decoration: none;
            color: #0b2b4c;
            font-weight: 700;
            border: 1px solid rgba(15, 23, 42, 0.06);
            background: rgba(255,255,255,0.9);
            margin-bottom: 8px;
            transition: all .15s ease;
          }
          .notes-link:hover{
            transform: translateY(-1px);
            border-color: rgba(37, 99, 235, 0.30);
            box-shadow: 0 6px 16px rgba(2, 6, 23, 0.08);
          }
          .notes-date{
            display: block;
            margin-top: 3px;
            font-size: 12px;
            font-weight: 700;
            color: #6b7280;
          }

          /* Contenido (derecha) */
          .note-card{
            padding: 16px 18px;
            border-radius: 16px;
            background: rgba(255,255,255,0.95);
            border: 1px solid rgba(15, 23, 42, 0.08);
            box-shadow: 0 10px 24px rgba(2,6,23,0.06);
            margin-bottom: 14px;
          }
          .note-h2{
            margin: 0 0 6px 0;
            font-size: 20px;
            font-weight: 900;
            color: #0b2b4c;
          }
          .note-meta{
            margin: 0 0 10px 0;
            font-size: 12px;
            font-weight: 800;
            color: #526484;
            text-transform: uppercase;
            letter-spacing: .3px;
          }
          .note-text{
            margin: 0;
            font-size: 14px;
            line-height: 1.55;
            color: #0b2b4c;
            font-weight: 600;
          }

          /* Anclas: evita que el título quede tapado por header */
          .anchor-offset { scroll-margin-top: 90px; }

          /* Reduce padding default de Streamlit */
          .block-container { padding-top: 1.0rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_notas_macro():
    _inject_css()

    st.markdown("<div class='notes-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='notes-title'>Notas — Macro</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='notes-subtitle'>Índice a la izquierda (sticky) + notas completas a la derecha</div>",
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 3], gap="large")

    # -------------------------
    # Sidebar (sticky)
    # -------------------------
    with left:
        sidebar_html = ["<div class='notes-sidebar'>", "<h4>Índice</h4>"]
        for n in NOTAS:
            sidebar_html.append(
                f"""
                <a class="notes-link" href="#{n['id']}">
                  {n['titulo']}
                  <span class="notes-date">{n['fecha']}</span>
                </a>
                """
            )
        sidebar_html.append("</div>")
        st.markdown("".join(sidebar_html), unsafe_allow_html=True)

    # -------------------------
    # Contenido (scroll)
    # -------------------------
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

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# Si usás multipage automático: Streamlit detecta pages/*.py
# Si lo llamás manual desde app.py, llamá a render_notas_macro()
# ============================================================
render_notas_macro()

