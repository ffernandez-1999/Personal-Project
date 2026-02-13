# pages/3_TC_Bandas.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from data.macro_services import load_tc_bcra, load_rem, load_ipc_indec


st.set_page_config(
    page_title="TC Bandas",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================
# HEADER SIMPLE
# =========================

st.title("Tipo de Cambio y Bandas")

col_btn, _ = st.columns([1, 10])
with col_btn:
    if st.button("← Volver"):
        st.switch_page("app.py")


st.divider()


# =========================
# CARGA DE DATOS
# =========================

df_tc = load_tc_bcra()
df_rem = load_rem()

# Si querés usar IPC ya cargado en otra page
if "ipc_data" not in st.session_state:
    st.session_state.ipc_data = load_ipc_indec()

df_ipc = st.session_state.ipc_data


# =========================
# EJEMPLO SIMPLE DE BANDA
# =========================

# Último TC
last_tc = df_tc["valor"].iloc[-1]

# Banda ejemplo ±10%
upper_band = last_tc * 1.10
lower_band = last_tc * 0.90


# =========================
# GRÁFICO
# =========================

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df_tc["fecha"],
        y=df_tc["valor"],
        mode="lines",
        name="Tipo de Cambio",
    )
)

fig.add_hline(y=upper_band, line_dash="dash", name="Banda Superior")
fig.add_hline(y=lower_band, line_dash="dash", name="Banda Inferior")

fig.update_layout(
    height=600,
    yaxis_title="Pesos por dólar",
    hovermode="x unified",
)

st.plotly_chart(fig, use_container_width=True)
