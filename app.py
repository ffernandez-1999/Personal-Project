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
