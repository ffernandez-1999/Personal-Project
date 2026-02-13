# pages/3_TC_Bandas.py

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from data.macro_services import load_a3500, load_rem_last, load_ipc_nacional_mensual


st.set_page_config(
    page_title="TC Bandas",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Tipo de Cambio (A3500) y Bandas")

if st.button("← Volver"):
    st.switch_page("app.py")

st.divider()

with st.spinner("Cargando datos..."):
    fx = load_a3500()
    rem = load_rem_last()

    if "ipc_data" not in st.session_state:
        st.session_state.ipc_data = load_ipc_nacional_mensual()

    ipc = st.session_state.ipc_data


# ============================================================
# Bandas 2025
# ============================================================

def build_bands_2025(start, end, lower0, upper0):
    g_up = (1 + 0.01) ** (1 / 30)
    g_dn = (1 - 0.01) ** (1 / 30)

    dates = pd.date_range(start, end, freq="D")
    t = np.arange(len(dates))

    return pd.DataFrame(
        {
            "Date": dates,
            "lower": lower0 * (g_dn**t),
            "upper": upper0 * (g_up**t),
        }
    )


def build_bands_2026(bands_2025, rem, ipc):
    rem_m = rem.assign(Period=rem["Date"].dt.to_period("M"))[["Period", "v_m_REM"]]

    m = ipc.merge(rem_m, on="Period", how="outer").sort_values("Period")
    m["v_m_dec"] = np.where(m["v_m_CPI"].notna(), m["v_m_CPI"], m["v_m_REM"] / 100)

    end_month = m.loc[m["v_m_REM"].notna(), "Period"].max() + 2

    b = pd.DataFrame({"Period": pd.period_range("2026-01", end_month, freq="M")})
    b["ref"] = b["Period"] - 2

    b = b.merge(
        m[["Period", "v_m_dec"]].rename(columns={"Period": "ref"}),
        on="ref",
        how="left",
    )

    lower0 = bands_2025.loc[bands_2025["Date"] == "2025-12-31", "lower"].iloc[0]
    upper0 = bands_2025.loc[bands_2025["Date"] == "2025-12-31", "upper"].iloc[0]

    cal = pd.DataFrame(
        {"Date": pd.date_range("2026-01-01", b["Period"].max().to_timestamp("M"), freq="D")}
    )

    cal["Period"] = cal["Date"].dt.to_period("M")
    cal = cal.merge(b[["Period", "v_m_dec"]], on="Period", how="left")

    r_d = (1 + cal["v_m_dec"]) ** (1 / 30) - 1

    cal["lower"] = lower0 * (1 - r_d).cumprod()
    cal["upper"] = upper0 * (1 + r_d).cumprod()

    return cal[["Date", "lower", "upper"]]


bands_2025 = build_bands_2025("2025-04-14", "2025-12-31", 1000.0, 1400.0)
bands_2026 = build_bands_2026(bands_2025, rem, ipc)

bands = pd.concat([bands_2025, bands_2026]).sort_values("Date")
df = bands.merge(fx, on="Date", how="left")


# ============================================================
# Gráfico
# ============================================================

last_fx = df["FX"].dropna().iloc[-1]

c1, c2 = st.columns([1, 3])

with c1:
    st.markdown(
        f"<div style='font-size:46px; font-weight:700'>{last_fx:,.0f}</div>",
        unsafe_allow_html=True,
    )

with c2:
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df["Date"], y=df["upper"], name="Banda superior", line=dict(dash="dash")))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["lower"], name="Banda inferior", line=dict(dash="dash"), fill="tonexty"))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["FX"], name="A3500"))

    fig.update_layout(hovermode="x unified", height=600)
    fig.update_yaxes(title_text="ARS / USD")
    fig.update_xaxes(title_text="")

    st.plotly_chart(fig, use_container_width=True)
