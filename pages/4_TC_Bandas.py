import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from data.macro_services import get_a3500


# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="TC Mayorista y Bandas",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS - OPCIÓN 1: DARK TECH
# ============================================================

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap');
      
      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 1rem; }

      /* Variables CSS */
      :root {
        --bg-primary: #0a0e17;
        --bg-secondary: #141824;
        --bg-card: #1a1f2e;
        --accent-primary: #00d4aa;
        --accent-secondary: #0099ff;
        --text-primary: #e8eaed;
        --text-secondary: #9ba3af;
        --text-muted: #6b7280;
        --border-color: #2a3041;
      }

      /* Fondo general */
      .stApp {
        background-color: var(--bg-primary);
        background-image: 
          radial-gradient(circle at 20% 50%, rgba(0, 212, 170, 0.03) 0%, transparent 50%),
          radial-gradient(circle at 80% 80%, rgba(0, 153, 255, 0.03) 0%, transparent 50%);
        color: var(--text-primary);
      }

      /* Tipografía global */
      html, body, [class*="css"], p, span, div {
        font-family: 'JetBrains Mono', monospace !important;
        color: var(--text-primary);
      }

      /* Header personalizado */
      .custom-header {
        background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-secondary) 100%);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid var(--border-color);
        margin-bottom: 2rem;
        position: relative;
      }

      .custom-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
      }

      .header-title {
        font-family: 'Syne', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.25rem;
        letter-spacing: -0.02em;
      }

      .header-subtitle {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.875rem;
        color: var(--text-muted);
        letter-spacing: 0.05em;
        text-transform: uppercase;
      }

      /* Título de página */
      h1 {
        font-family: 'Syne', sans-serif !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        margin-bottom: 2rem !important;
        display: flex;
        align-items: center;
        gap: 0.75rem;
      }

      h1::before {
        content: '';
        width: 3px;
        height: 1.5rem;
        background: linear-gradient(180deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
        border-radius: 2px;
      }

      /* KPI Cards */
      .kpi-card {
        background: var(--bg-card);
        padding: 1.75rem;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
      }

      .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, var(--accent-primary) 0%, transparent 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
      }

      .kpi-card:hover {
        border-color: var(--accent-primary);
        transform: translateY(-2px);
      }

      .kpi-card:hover::after {
        opacity: 1;
      }

      .kpi-main {
        font-family: 'Syne', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.02em;
      }

      .kpi-date {
        font-size: 0.75rem;
        color: var(--text-muted);
        margin-left: 0.5rem;
      }

      .kpi-sub {
        font-family: 'Syne', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
      }

      /* Subtítulos de sección */
      h3 {
        font-family: 'Syne', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        color: var(--text-secondary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 1.5rem !important;
      }

      /* Slider personalizado */
      .stSlider {
        padding: 1rem 0;
      }

      .stSlider > div > div > div {
        background-color: var(--bg-card) !important;
      }

      .stSlider > div > div > div > div {
        background-color: var(--accent-primary) !important;
      }

      /* Botón de volver */
      .stButton > button {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-secondary) !important;
        font-family: 'JetBrains Mono', monospace !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.25rem !important;
        transition: all 0.2s ease !important;
        font-size: 0.875rem !important;
      }

      .stButton > button:hover {
        border-color: var(--accent-primary) !important;
        color: var(--accent-primary) !important;
      }

      /* Metodología card */
      .methodology-card {
        background: var(--bg-card);
        border-left: 4px solid var(--accent-primary);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
        border: 1px solid var(--border-color);
      }

      .methodology-card h4 {
        font-family: 'Syne', sans-serif;
        color: var(--text-primary);
        margin-bottom: 1rem;
        font-size: 1.125rem;
      }

      .methodology-card ul {
        color: var(--text-secondary);
        font-size: 0.875rem;
        line-height: 1.6;
      }

      .methodology-card li {
        color: var(--text-secondary);
      }

      /* Gráfico contenedor */
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
    <div class="custom-header">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <div class="header-title">Francisco Fernandez Amato</div>
                <div class="header-subtitle">Macroeconomista</div>
            </div>
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
    "<h1 style='text-align:center;'>TC Mayorista (A3500) y Bandas</h1>",
    unsafe_allow_html=True,
)

# ============================================================
# DATA
# ============================================================

fx = get_a3500().copy()
fx["Date"] = pd.to_datetime(fx["Date"]).dt.normalize()
fx = fx.sort_values("Date").reset_index(drop=True)

# ============================================================
# BANDAS 2025
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

bands = build_bands_2025("2025-04-14", "2026-08-31", 1000, 1400)

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
# KPIs
# ============================================================

kpi_col, main_col = st.columns([1, 2.5], gap="large")

with kpi_col:

    last_row = fx.iloc[-1]
    last_val = int(round(last_row["FX"]))
    last_val_fmt = f"{last_val:,}".replace(",", ".")
    last_date = last_row["Date"].strftime("%d/%m/%Y")

    prev_month = fx[fx["Date"] <= last_row["Date"] - pd.Timedelta(days=30)]
    prev_year = fx[fx["Date"] <= last_row["Date"] - pd.Timedelta(days=365)]

    mm = ((last_val / prev_month.iloc[-1]["FX"]) - 1) * 100 if not prev_month.empty else np.nan
    yy = ((last_val / prev_year.iloc[-1]["FX"]) - 1) * 100 if not prev_year.empty else np.nan

    st.markdown(
        f"""
        <div class="kpi-card">
            <div>
                <span class="kpi-main">{last_val_fmt}</span>
                <span class="kpi-date">{last_date}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="kpi-card">
            <div style="display:flex; gap:2rem;">
                <div>
                    <div class="kpi-sub">{mm:.1f}%</div>
                    <div style="font-size:0.8rem; color:#6b7280;">m/m</div>
                </div>
                <div>
                    <div class="kpi-sub">{yy:.1f}%</div>
                    <div style="font-size:0.8rem; color:#6b7280;">y/y</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# RANGO + GRÁFICO
# ============================================================

with main_col:

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
            line=dict(dash="dash", color="#00d4aa", width=1.5),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_plot["Date"],
            y=df_plot["lower"],
            line=dict(dash="dash", color="#00d4aa", width=1.5),
            fill="tonexty",
            fillcolor="rgba(0, 212, 170, 0.05)",
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_plot["Date"],
            y=df_plot["FX"],
            line=dict(color="#0099ff", width=2.5),
            showlegend=False,
        )
    )

    fig.update_layout(
        height=560,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="#141824",
        paper_bgcolor="#1a1f2e",
        font_color="#e8eaed",
        font_family="JetBrains Mono",
        xaxis=dict(
            gridcolor="#2a3041",
            showgrid=True,
            linecolor="#2a3041",
        ),
        yaxis=dict(
            gridcolor="#2a3041",
            showgrid=True,
            linecolor="#2a3041",
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
            <li>—</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
