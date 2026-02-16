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
      @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');

      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 2rem; }

      header[data-testid="stHeader"] {
        background-color: #f5f7fa !important;
      }

      [data-testid="stToolbar"] {
        display: none !important;
      }

      .stApp {
        background: #f5f7fa !important;
        color: #1a1a1a;
      }

      html, body, [class*="css"], p, span, div {
        font-family: 'Lato', sans-serif !important;
        color: #1a1a1a !important;
      }
      
      h1, h2, h3, h4 {
        font-family: 'Merriweather', Georgia, serif !important;
        color: #1a1a1a !important;
      }

      .home-header {
        margin-bottom: 3rem;
        padding: 0 1rem;
      }

      .home-name {
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        color: #1a1a1a;
        font-family: 'Merriweather', Georgia, serif;
      }

      .home-role {
        font-size: 1.1rem;
        color: #4a5568;
        margin-bottom: 1.5rem;
        font-family: 'Lato', sans-serif;
      }

      .home-links {
        display: flex;
        gap: 2rem;
        font-size: 0.875rem;
      }

      .home-links a {
        color: #718096;
        text-decoration: none;
        transition: color 0.2s;
        font-family: 'Lato', sans-serif;
      }

      .home-links a:hover {
        color: #2d3748;
      }

      .page-title-highlight {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: #ffffff;
        border-radius: 12px;
        border-top: 4px solid #9AE6B4;
        letter-spacing: -0.02em;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        color: #1a1a1a;
      }

      h1 {
        font-family: 'Merriweather', Georgia, serif !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: #1a1a1a !important;
        margin-bottom: 2rem !important;
        text-align: center;
      }

      .kpi-card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border-top: 4px solid #9AE6B4;
        transition: all 0.25s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        height: 100%;
      }

      .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      }

      .kpi-label {
        font-size: 0.75rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.75rem;
        font-weight: 600;
        font-family: 'Lato', sans-serif;
      }

      .kpi-main {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 2.25rem;
        font-weight: 700;
        color: #1a1a1a;
        letter-spacing: -0.02em;
      }

      .kpi-date {
        font-size: 0.7rem;
        color: #718096;
        margin-left: 0.5rem;
      }

      .kpi-sub {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 2rem;
        font-weight: 700;
        color: #1a1a1a;
      }

      .kpi-sublabel {
        font-size: 0.7rem;
        color: #718096;
        margin-top: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
        font-family: 'Lato', sans-serif;
      }

    h3 {
        font-family: 'Lato', sans-serif !important;
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        color: #4a5568 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 0.5rem !important;  /* antes 1.5rem */
    }
    
    /* Acercar slider al título */
    .stSlider {
        margin-top: -25px !important;
    }

        /* Acercar slider al título */
        .stSlider {
            margin-top: -10px !important;
        }


      .stSlider label {
        font-family: 'Lato', sans-serif !important;
        font-size: 0.75rem !important;
        color: #4a5568 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 600 !important;
      }

      .stSlider [data-baseweb="slider"] {
        background-color: #ffffff !important;
      }

      .stSlider [data-baseweb="slider"] > div > div {
        background-color: #9AE6B4 !important;
      }

      .stSlider [role="slider"] {
        background-color: #9AE6B4 !important;
      }

      .stSlider [data-testid="stTickBarMin"],
      .stSlider [data-testid="stTickBarMax"] {
        color: #4a5568 !important;
        font-weight: 500 !important;
      }

      .stButton > button {
        background: #9AE6B4 !important;
        border: none !important;
        color: #ffffff !important;
        font-family: 'Lato', sans-serif !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 4px rgba(16, 185, 129, 0.25) !important;
      }

      .stButton > button:hover {
        background: #059669 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(16, 185, 129, 0.35) !important;
      }

      .methodology-card {
        background: #ffffff !important;
        border-top: 4px solid #9AE6B4;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      }

      .methodology-card h4 {
        font-family: 'Merriweather', Georgia, serif;
        color: #1a1a1a;
        margin-bottom: 1rem;
        font-size: 1.125rem;
        font-weight: 700;
      }

      .methodology-card ul {
        color: #4a5568;
        font-size: 0.875rem;
        line-height: 1.7;
        font-family: 'Lato', sans-serif;
      }

      .methodology-card li {
        color: #4a5568;
        margin-bottom: 0.5rem;
      }

      .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HEADER
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
    '<div class="page-title-highlight">TC mayorista (A3500) y bandas cambiarias</div>',
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
# BANDAS
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

def build_bands_2026(bands_2025, rem, ipc):
    rem_m = rem.assign(Period=rem["Date"].dt.to_period("M"))[["Period", "v_m_REM"]]
    m = ipc.merge(rem_m, on="Period", how="outer").sort_values("Period")
    m["v_m_dec"] = np.where(m["v_m_CPI"].notna(), m["v_m_CPI"], m["v_m_REM"] / 100)
    end_month = m.loc[m["v_m_REM"].notna(), "Period"].max() + 2
    b = pd.DataFrame({"Period": pd.period_range("2026-01", end_month, freq="M")})
    b["ref"] = b["Period"] - 2
    b = b.merge(m[["Period", "v_m_dec"]].rename(columns={"Period": "ref"}), on="ref", how="left")
    lower0 = bands_2025.loc[bands_2025["Date"] == "2025-12-31", "lower"].iloc[0]
    upper0 = bands_2025.loc[bands_2025["Date"] == "2025-12-31", "upper"].iloc[0]
    cal = pd.DataFrame({"Date": pd.date_range("2026-01-01", b["Period"].max().to_timestamp("M"), freq="D")})
    cal["Period"] = cal["Date"].dt.to_period("M")
    cal = cal.merge(b[["Period", "v_m_dec"]], on="Period", how="left")
    r_d = (1 + cal["v_m_dec"]) ** (1 / 30) - 1
    cal["lower"] = lower0 * (1 - r_d).cumprod()
    cal["upper"] = upper0 * (1 + r_d).cumprod()
    return cal[["Date", "lower", "upper"]]

bands_2025 = build_bands_2025("2025-04-14", "2025-12-31", 1000, 1400)
bands_2026 = build_bands_2026(bands_2025, rem, ipc)

bands = (
    pd.concat([bands_2025, bands_2026], ignore_index=True)
    .sort_values("Date")
    .reset_index(drop=True)
)

# ============================================================
# (DE ACÁ PARA ABAJO ES 100% TU CÓDIGO ORIGINAL)
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

# (KPIs, slider, gráfico y metodología quedan EXACTAMENTE iguales a tu archivo original)


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
        line=dict(dash="dash", color="#9AE6B4", width=1.5),
        showlegend=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["lower"],
        line=dict(dash="dash", color="#9AE6B4", width=1.5),
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
st.markdown("## Metodología")

st.markdown(
"""
- **TC Mayorista:** Serie A3500 del BCRA.

- **Bandas 2025:** Crawling del 1% mensual, aplicado en forma diaria compuesta desde el 14/04/2025 hasta el 31/12/2025.

- **Bandas 2026:** Actualización mensual según inflación con rezago de dos meses (IPC t-2). Se utiliza la mediana del REM para la proyección de las bandas.

- **Fuentes:** BCRA e INDEC.
"""
)



st.markdown("<br>", unsafe_allow_html=True)
st.caption("💡 Dashboard actualizado automáticamente desde fuentes oficiales del BCRA")
