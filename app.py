import streamlit as st

st.set_page_config(
    page_title="Personal Project",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 1.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

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

left, center, right = st.columns([1, 6, 1])

with center:
    st.divider()
    st.markdown("<div style='height:90px;'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📊 Dashboard interactivo</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Indicadores macroeconómicos.</p>",
                unsafe_allow_html=True
            )

            col_a, col_b = st.columns(2)

            with col_a:
                st.page_link("pages/2_IPC.py", label="Ver IPC →", use_container_width=True)

            with col_b:
                st.page_link("pages/4_TC_Bandas.py", label="Ver TC y Bandas →", use_container_width=True)

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

            st.page_link("pages/3_Notes.py", label="Ver artículos →", use_container_width=True)
