import streamlit as st

st.set_page_config(
    page_title="Francisco Fernandez | Macro & Data",
    layout="wide"
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

    # espacio vertical (el que ya sabíamos que estaba bien)
    st.markdown("<div style='height:90px;'></div>", unsafe_allow_html=True)

    # ---------- CARDS ----------
    c1, c2, c3 = st.columns(3)

    # ---------- CARD 1 ----------
    with c1:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📄 Sobre mí / CV</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Experiencia, formación y áreas de interés.</p>",
                unsafe_allow_html=True
            )

            b1, b2 = st.columns(2)

            with b1:
                with open("assets/cv.pdf", "rb") as f:
                    st.download_button(
                        "Ver CV →",
                        f,
                        file_name="CV_Francisco_Fernandez_Amato.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            with b2:
                with open("assets/TFM_Fernandez.pdf", "rb") as f:
                    st.download_button(
                        "Ver Tesis Maestría →",
                        f,
                        file_name="TFM_Francisco_Fernandez.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

    # ---------- CARD 2 ----------
    with c2:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📊 Dashboard interactivo</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Visualización de datos macroeconómicos.</p>",
                unsafe_allow_html=True
            )

            if st.button("Ver dashboard →", use_container_width=True):
                st.switch_page("pages/2_Dashboard.py")

    # ---------- CARD 3 ----------
    with c3:
        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center;'>📝 Notas macroeconómicas</h4>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p style='text-align:center;'>Análisis y perspectivas actuales.</p>",
                unsafe_allow_html=True
            )

            if st.button("Ver artículos →", use_container_width=True):
                st.switch_page("pages/3_Notes.py")
