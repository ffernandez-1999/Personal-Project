import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from data.macro_services import (
    get_a3500,
    get_rem_last,
    get_ipc_bcra,
)

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="TC Mayorista y Bandas",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS - LIGHT THEME + Merriweather/Lato
# ============================================================

st.markdown(
    """
    <style>
    ... (TODO TU CSS EXACTAMENTE IGUAL, SIN CAMBIOS)
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HEADER (IGUAL AL HOME)
# ============================================================

st.markdown(
    """
    <div class="home-header">
        <div class="home-name">Francisco Fernandez Amato</div>
        <div class="home-role">Macroeconomista</div>
        <div class="home-links">
            <a href="mailto:franciscofernandezz1999@gmail.com">Email</a>
            <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">LinkedIn</a>
            <a href="https://github.com/ffernandez-1999" target="_blank">GitHub</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col_btn, _ = st.columns([1, 5])
with col_btn:
    if st.button("← Volver"):
        st.switch_page("app.py")

st.markdown(
    '<div class="page-title-highlight">TC Mayorista (A3500) y Bandas</div>',
    unsafe_allow_html=True,
)

# ============================================================
# DATA
# ============================================================

fx = get_a3500().copy()
fx["Date"] = pd.to_datetime(fx["Date"]).dt.normalize()
fx = fx.sort_values("Date").reset_index(drop=True)

rem = get_rem_last()
ipc = get_ipc_bcra()

# ============================================================
# BANDAS 2025 (1% FIJO)
# ============================================================

def build_bands_2025(start, end, lower0, upper0):
    g_up = (1 + 0.01) ** (1 / 30)
    g_dn = (1 - 0.01) ** (1 / 30)
    dates = pd.date_range(start, end, freq="D")
    t = np.arange(len(dates))
    return pd.DataFrame({
        "Date": dates,
        "lower": lower0 * (g_dn**t),
        "upper": upper0 * (g_up**t),
    })

bands_2025 = build_bands_2025("2025-04-14", "2025-12-31", 1000, 1400)

# ============================================================
# BANDAS 2026 (IPC/REM - REZAGO 2 MESES)
# ============================================================

def build_bands_2026(bands_2025, rem, ipc):

    rem_m = rem.assign(Period=rem["Date"].dt.to_period("M"))[["Period", "v_m_REM"]]

    m = ipc.merge(rem_m, on="Period", how="outer").sort_values("Period")

    m["v_m_dec"] = np.where(
        m["v_m_CPI"].notna(),
        m["v_m_CPI"],
        m["v_m_REM"] / 100
    )

    end_month = m.loc[m["v_m_REM"].notna(), "Period"].max() + 2

    b = pd.DataFrame({
        "Period": pd.period_range("2026-01", end_month, freq="M")
    })

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

    cal = pd.DataFrame({
        "Date": pd.date_range(
            "2026-01-01",
            b["Period"].max().to_timestamp("M"),
            freq="D"
        )
    })

    cal["Period"] = cal["Date"].dt.to_period("M")

    cal = cal.merge(
        b[["Period", "v_m_dec"]],
        on="Period",
        how="left"
    )

    r_d = (1 + cal["v_m_dec"]) ** (1 / 30) - 1

    cal["lower"] = lower0 * (1 - r_d).cumprod()
    cal["upper"] = upper0 * (1 + r_d).cumprod()

    return cal[["Date", "lower", "upper"]]

bands_2026 = build_bands_2026(bands_2025, rem, ipc)

bands = (
    pd.concat([bands_2025, bands_2026], ignore_index=True)
    .sort_values("Date")
    .reset_index(drop=True)
)

# ============================================================
# MASTER MERGE CORRECTO
# ============================================================

fx_min = fx["Date"].min()
bands_max = bands["Date"].max()
last_fx_date = fx["Date"].max()

cal = pd.DataFrame({"Date": pd.date_range(fx_min, bands_max, freq="D")})

df = (
    cal.merge(fx, on="Date", how="left")
       .merge(bands, on="Date", how="left")
       .sort_values("Date")
)

df["FX"] = df["FX"].ffill()
df.loc[df["Date"] > last_fx_date, "FX"] = np.nan



# ============================================================
# KPIs EN FILA (ARRIBA)
# ============================================================

last_row = fx.iloc[-1]
last_val = int(round(last_row["FX"]))
last_val_fmt = f"{last_val:,}".replace(",", ".")
last_date = last_row["Date"].strftime("%d/%m/%Y")

prev_month = fx[fx["Date"] <= last_row["Date"] - pd.Timedelta(days=30)]
prev_year = fx[fx["Date"] <= last_row["Date"] - pd.Timedelta(days=365)]

mm = ((last_val / prev_month.iloc[-1]["FX"]) - 1) * 100 if not prev_month.empty else np.nan
yy = ((last_val / prev_year.iloc[-1]["FX"]) - 1) * 100 if not prev_year.empty else np.nan

# KPIs en 3 columnas
kpi1, kpi2, kpi3 = st.columns(3, gap="large")

with kpi1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Tipo de Cambio Actual</div>
            <div>
                <span class="kpi-main">{last_val_fmt}</span>
                <span class="kpi-date">{last_date}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Variación Mensual</div>
            <div class="kpi-sub">{mm:.1f}%</div>
            <div class="kpi-sublabel">m/m</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Variación Anual</div>
            <div class="kpi-sub">{yy:.1f}%</div>
            <div class="kpi-sublabel">y/y</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# RANGO + GRÁFICO (TODO EL ANCHO)
# ============================================================

st.markdown("### Rango de fechas")

min_d = df["Date"].min().date()
max_d = df["Date"].max().date()

start_d, end_d = st.slider(
    "",
    min_value=min_d,
    max_value=max_d,
    value=(min_d, max_d),
)

df_plot = df[
    (df["Date"] >= pd.Timestamp(start_d)) &
    (df["Date"] <= pd.Timestamp(end_d))
]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["upper"],
        line=dict(dash="dash", color="#10b981", width=1.5),
        showlegend=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["lower"],
        line=dict(dash="dash", color="#10b981", width=1.5),
        fill="tonexty",
        fillcolor="rgba(16, 185, 129, 0.1)",
        showlegend=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["FX"],
        line=dict(color="#3b82f6", width=2.5),
        showlegend=False,
    )
)

fig.update_layout(
    height=560,
    hovermode="x unified",
    margin=dict(l=20, r=20, t=20, b=20),
    plot_bgcolor="#ffffff",
    paper_bgcolor="#ffffff",
    font_color="#1a1a1a",
    font_family="Lato",
    xaxis=dict(
        gridcolor="#e2e8f0",
        showgrid=True,
        linecolor="#cbd5e0",
    ),
    yaxis=dict(
        gridcolor="#e2e8f0",
        showgrid=True,
        linecolor="#cbd5e0",
    ),
)

fig.update_yaxes(title="ARS/USD", title_font=dict(size=12))

st.plotly_chart(fig, use_container_width=True)

# ============================================================
# METODOLOGÍA
# ============================================================

st.markdown(
    """
    <div class="methodology-card">
        <h4>📖 Metodología</h4>
        <ul>
            <li><b>TC Mayorista:</b> Serie A3500 del BCRA (tipo de cambio de referencia)</li>
            <li><b>Bandas:</b> Bandas de fluctuación del 2% mensual proyectadas desde abril 2025</li>
            <li><b>Fuente:</b> Banco Central de la República Argentina (BCRA)</li>
            <li><b>Actualización:</b> Datos actualizados automáticamente desde fuentes oficiales</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("💡 Dashboard actualizado automáticamente desde fuentes oficiales del BCRA")
