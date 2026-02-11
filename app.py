import streamlit as st

st.set_page_config(
    page_title="Personal Project",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Oculta sidebar + botón/cabecera (para que no aparezca el menú de páginas) ---
st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      /* achica un poco el padding superior */
      section.main > div { padding-top: 1.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- HEADER PRINCIPAL ----------
st.markdown(
    """
    <div style="text-align:center;">
        <h2>Francisco Fernandez Amato</h2>
        <div style="margin-top:8px; font-size:20px;">
            <a href="mailto:franciscofernandezz1999@gmail.com">Email</a>
            &nbsp;·&nbsp;
            <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">LinkedIn</a>
            &nbsp;·&nbsp;
            <a href="https://github.com/ffernandez-1999" target="_blank">GitHub</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- CONTENEDOR ANGOSTO ----------
left, center, right = st.columns([1, 6, 1])

with center:
    st.divider()

    # espacio vertical (mantenemos tu look)
    st.markdown("<div style='height:90px;'></div>", unsafe_allow_html=True)

    # ---------- CARDS (2 columnas) ----------
    c1, c2 = st.columns(2)

    # ---------- CARD 1: Dashboard ----------
    with c1:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📊 Dashboard interactivo</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Comparación IPC oficial vs IPCA (ENGHo 2017/18).</p>",
                unsafe_allow_html=True
            )

            st.page_link("pages/2_Dashboard.py", label="Ver IPC actualizado →", use_container_width=True)


    # ---------- CARD 2: Artículos (Wix) ----------
    with c2:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📝 Notas macroeconómicas</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Artículos y publicaciones.</p>",
                unsafe_allow_html=True
            )

            # Link externo (más confiable que intentar switch_page)
            st.link_button(
                "Ver artículos →",
                "https://franciscofernanc2ozl.wixsite.com/ffecon",
                use_container_width=True,
            )
