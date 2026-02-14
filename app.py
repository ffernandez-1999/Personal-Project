import streamlit as st

st.set_page_config(
    page_title="Francisco Fernandez Amato",
    layout="wide",
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');

/* Fondo */
.stApp {
    background: #f5f7fa;
}

/* Header superior */
header[data-testid="stHeader"] {
    background: #f5f7fa;
}

/* Tipografía */
html, body {
    font-family: 'Lato', sans-serif;
    color: #1a1a1a;
}

h1, h2, h3 {
    font-family: 'Merriweather', serif;
}

/* Header */
.home-header {
    margin-bottom: 4rem;
}

.home-name {
    font-size: 2.6rem;
    font-weight: 900;
}

.home-role {
    font-size: 1.1rem;
    color: #475569;
    margin-bottom: 1.5rem;
}

.home-links {
    display: flex;
    gap: 2rem;
}

.home-links a {
    color: #64748b;
    text-decoration: none;
}

.home-links a:hover {
    color: #0f172a;
}

/* CARD LINK WRAPPER */
.card-link {
    text-decoration: none;
    color: inherit;
    display: block;
}

/* Cards */
.card {
    background: white;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    cursor: pointer;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(0,0,0,0.15);
}

.card-accent-green {
    height: 6px;
    background: #10b981;
}

.card-accent-blue {
    height: 6px;
    background: #3b82f6;
}

.card-content {
    padding: 2rem;
}

.card-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.8rem;
}

.card-desc {
    color: #475569;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="home-header">
    <div class="home-name">Francisco Fernandez Amato</div>
    <div class="home-role">Macroeconomista</div>
    <div class="home-links">
        <a href="mailto:franciscofernandezz1999@gmail.com">Email</a>
        <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">LinkedIn</a>
        <a href="https://github.com/ffernandez-1999" target="_blank">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CARDS (CLICKABLE COMPLETAS CON SWITCH_PAGE)
# ============================================================

left, center, right = st.columns([0.5, 10, 0.5])

with center:
    col1, col2 = st.columns(2, gap="large")

    # CARD IPC
    with col1:
        if st.button("IPC Canasta 2017/18", key="ipc_card", use_container_width=True):
            st.switch_page("pages/2_IPC.py")

        st.markdown("""
        <style>
        div[data-testid="stButton"][key="ipc_card"] > button {
            height: 170px;
            border-radius: 14px;
            background: white;
            border: none;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
            font-size: 1.3rem;
            font-weight: 700;
            text-align: left;
            padding-left: 2rem;
            position: relative;
        }

        div[data-testid="stButton"][key="ipc_card"] > button:hover {
            transform: translateY(-6px);
            box-shadow: 0 18px 40px rgba(0,0,0,0.15);
        }
        </style>
        """, unsafe_allow_html=True)

    # CARD NOTES
    with col2:
        if st.button("Notas", key="notes_card", use_container_width=True):
            st.switch_page("pages/3_Notes.py")

        st.markdown("""
        <style>
        div[data-testid="stButton"][key="notes_card"] > button {
            height: 170px;
            border-radius: 14px;
            background: white;
            border: none;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
            font-size: 1.3rem;
            font-weight: 700;
            text-align: left;
            padding-left: 2rem;
        }

        div[data-testid="stButton"][key="notes_card"] > button:hover {
            transform: translateY(-6px);
            box-shadow: 0 18px 40px rgba(0,0,0,0.15);
        }
        </style>
        """, unsafe_allow_html=True)
