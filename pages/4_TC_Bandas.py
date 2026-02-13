# pages/3_TC_Bandas.py

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from data.macro_services import get_a3500, get_rem_last, get_ipc_bcra


st.set_page_config(
    page_title="TC Bandas",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Tipo de Cambio (A3500) y Bandas")

if st.button("← Volver"):
    st.switch_page("app.py")

st.divider()


# =========================
# LOAD DATA
# =========================

with st.spinner("Cargando datos..."):
    fx = get_a3500()
    rem = get_rem_last()
    ipc = get_ipc_bcra()


# ============================================================
# BANDAS 2025
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

    if not m["v_m_REM"].notna().any():
        return pd.DataFrame(columns=["Date", "lower", "upper"])

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

bands = pd.concat([bands_2025, bands_2026], ignore_index=True).sort_values("Date")

df = bands.merge(fx, on="Date", how="left")


# ============================================================
# HEADER SIMPLE
# ============================================================

last_fx = fx["FX"].dropna().iloc[-1]

st.markdown(
    f"<div style='font-size:46px; font-weight:700'>{last_fx:,.0f} ARS/USD</div>",
    unsafe_allow_html=True,
)


# ============================================================
# PLOT
# ============================================================

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=df["Date"], y=df["upper"], name="Banda superior", line=dict(dash="dash"))
)

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["lower"],
        name="Banda inferior",
        line=dict(dash="dash"),
        fill="tonexty",
    )
)

fig.add_trace(go.Scatter(x=df["Date"], y=df["FX"], name="A3500"))

fig.update_layout(hovermode="x unified", height=600)
fig.update_yaxes(title_text="ARS / USD")

st.plotly_chart(fig, use_container_width=True)
