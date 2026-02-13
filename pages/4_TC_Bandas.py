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

# ============================================================
# LOAD DATA
# ============================================================

with st.spinner("Cargando datos..."):
    fx = get_a3500().copy()
    fx["Date"] = pd.to_datetime(fx["Date"]).dt.normalize()
    fx = (
        fx.dropna(subset=["Date", "FX"])
        .drop_duplicates("Date")
        .sort_values("Date")
        .reset_index(drop=True)
    )

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

    m["v_m_dec"] = np.where(
        m["v_m_CPI"].notna(),
        m["v_m_CPI"],
        m["v_m_REM"] / 100,
    )

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

    lower0 = bands_2025.loc[
        bands_2025["Date"] == "2025-12-31", "lower"
    ].iloc[0]

    upper0 = bands_2025.loc[
        bands_2025["Date"] == "2025-12-31", "upper"
    ].iloc[0]

    cal = pd.DataFrame(
        {
            "Date": pd.date_range(
                "2026-01-01",
                b["Period"].max().to_timestamp("M"),
                freq="D",
            )
        }
    )

    cal["Period"] = cal["Date"].dt.to_period("M")

    cal = cal.merge(
        b[["Period", "v_m_dec"]],
        on="Period",
        how="left",
    )

    r_d = (1 + cal["v_m_dec"]) ** (1 / 30) - 1

    cal["lower"] = lower0 * (1 - r_d).cumprod()
    cal["upper"] = upper0 * (1 + r_d).cumprod()

    return cal[["Date", "lower", "upper"]]


bands_2025 = build_bands_2025(
    "2025-04-14",
    "2025-12-31",
    1000.0,
    1400.0,
)

bands_2026 = build_bands_2026(bands_2025, rem, ipc)

bands = (
    pd.concat([bands_2025, bands_2026], ignore_index=True)
    .dropna(subset=["Date", "lower", "upper"])
    .sort_values("Date")
    .reset_index(drop=True)
)

bands["Date"] = pd.to_datetime(bands["Date"]).dt.normalize()


# ============================================================
# MASTER CALENDAR (RESPETA MERGE ORIGINAL)
# ============================================================

fx_min = pd.to_datetime(fx["Date"].min())
last_fx_date = pd.to_datetime(fx["Date"].max())
bands_max = pd.to_datetime(bands["Date"].max())

full_end = max(d for d in [last_fx_date, bands_max] if pd.notna(d))

cal = pd.DataFrame(
    {"Date": pd.date_range(fx_min, full_end, freq="D")}
)

df = (
    cal.merge(fx, on="Date", how="left")
       .merge(bands, on="Date", how="left")
       .sort_values("Date")
       .reset_index(drop=True)
)

# Forward fill SOLO dentro del rango real del oficial
df["FX"] = df["FX"].ffill()
df.loc[df["Date"] > last_fx_date, "FX"] = np.nan


# ============================================================
# SLIDER DINÁMICO (COMO TU BLOQUE ORIGINAL)
# ============================================================

mask_any = df[["FX"]].notna().any(axis=1)

s_min = df.loc[mask_any, "Date"].min()
s_max = df["Date"].max()

min_d = s_min.date()
max_d = s_max.date()

default_start = max(min_d, pd.to_datetime("2025-01-01").date())

start_d, end_d = st.slider(
    "Rango de fechas",
    min_value=min_d,
    max_value=max_d,
    value=(default_start, max_d),
)

df_plot = df[
    (df["Date"] >= pd.Timestamp(start_d)) &
    (df["Date"] <= pd.Timestamp(end_d))
]


# ============================================================
# HEADER
# ============================================================

last_fx = fx["FX"].iloc[-1]

st.markdown(
    f"<div style='font-size:46px; font-weight:700'>{last_fx:,.0f} ARS/USD</div>",
    unsafe_allow_html=True,
)


# ============================================================
# PLOT
# ============================================================

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["upper"],
        name="Banda superior",
        line=dict(dash="dash"),
    )
)

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["lower"],
        name="Banda inferior",
        line=dict(dash="dash"),
        fill="tonexty",
    )
)

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["FX"],
        name="TC Mayorista",
        line=dict(color="red"),
    )
)

fig.update_layout(
    hovermode="x unified",
    height=600,
)

fig.update_yaxes(title_text="ARS / USD")
fig.update_xaxes(title_text="")

st.plotly_chart(fig, use_container_width=True)


# ============================================================
# DOWNLOAD
# ============================================================

st.download_button(
    "⬇️ Descargar CSV",
    df_plot.to_csv(index=False).encode("utf-8"),
    file_name="tc_bandas.csv",
    mime="text/csv",
)
