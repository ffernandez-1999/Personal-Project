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
# CSS - MISMO ESTILO QUE HOME E IPC
# ============================================================

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
      
      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 1rem; }
      
      /* Ocultar/oscurecer header de Streamlit */
      header[data-testid="stHeader"] {
        background-color: #1a1a1a !important;
      }
      
      /* Ocultar toolbar arriba */
      [data-testid="stToolbar"] {
        display: none !important;
      }

      /* Variables CSS - PANELES MÁS CLAROS */
      :root {
        --bg-primary: #1a1a1a;
        --bg-secondary: #242424;
        --bg-card: #2a2a2a;
        --bg-chart: #2f2f2f;
        --accent-primary: #00ff88;
        --accent-secondary: #ff0088;
        --text-primary: #fff;
        --text-secondary: #aaa;
        --text-muted: #888;
        --border-color: #333;
      }

      /* Fondo general */
      .stApp {
        background-color: var(--bg-primary) !important;
        color: var(--text-primary);
      }

      /* Tipografía global - INTER */
      html, body, [class*="css"], p, span, div, h1, h2, h3, h4 {
        font-family: 'Inter', sans-serif !important;
        color: var(--text-primary) !important;
      }

      /* Header igual al home */
      .home-header {
        margin-bottom: 3rem;
        padding: 0 1rem;
      }

      .home-name {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        color: #fff;
      }

      .home-role {
        font-size: 0.95rem;
        color: var(--text-muted);
        margin-bottom: 1.5rem;
      }

      .home-links {
        display: flex;
        gap: 2rem;
        font-size: 0.875rem;
      }

      .home-links a {
        color: var(--text-muted);
        text-decoration: none;
        transition: color 0.2s;
      }

      .home-links a:hover {
        color: #fff;
      }

      /* Título de página */
      .page-title-highlight {
        font-family: 'Inter', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 2.5rem;
        padding: 1rem;
        background: var(--bg-card);
        border-radius: 0;
        border-top: 4px solid var(--accent-primary);
        letter-spacing: -0.02em;
      }

      h1 {
        font-family: 'Inter', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        color: var(--text-primary) !important;
        margin-bottom: 2rem !important;
        text-align: center;
      }

      /* KPI Cards */
      .kpi-card {
        background: var(--bg-card);
        padding: 1.5rem;
        border-radius: 0;
        border: 1px solid var(--border-color);
        border-top: 4px solid var(--accent-primary);
        transition: all 0.3s ease;
        height: 100%;
      }

      .kpi-card:hover {
        transform: scale(1.02);
      }

      .kpi-label {
        font-size: 0.7rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.75rem;
        font-weight: 600;
      }

      .kpi-main {
        font-family: 'Inter', sans-serif;
        font-size: 2.25rem;
        font-weight: 800;
        color: var(--text-primary);
        letter-spacing: -0.02em;
      }

      .kpi-date {
        font-size: 0.7rem;
        color: var(--text-muted);
        margin-left: 0.5rem;
      }

      .kpi-sub {
        font-family: 'Inter', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        color: var(--text-primary);
      }

      .kpi-sublabel {
        font-size: 0.7rem;
        color: var(--text-muted);
        margin-top: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
      }

      /* Subtítulos de sección */
      h3 {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        color: var(--text-secondary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 1.5rem !important;
      }

      /* Slider personalizado */
      .stSlider label {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.75rem !important;
        color: var(--text-secondary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 600 !important;
      }

      .stSlider [data-baseweb="slider"] {
        background-color: var(--bg-card) !important;
      }

      .stSlider [data-baseweb="slider"] > div > div {
        background-color: var(--accent-primary) !important;
      }

      .stSlider [role="slider"] {
        background-color: var(--accent-primary) !important;
      }

      .stSlider [data-testid="stTickBarMin"],
      .stSlider [data-testid="stTickBarMax"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
      }

      /* Botón de volver */
      .stButton > button {
        background: transparent !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        border-radius: 0 !important;
        padding: 0.75rem 1.25rem !important;
        transition: all 0.2s ease !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
      }

      .stButton > button:hover {
        border-color: var(--accent-primary) !important;
        background: rgba(0, 255, 136, 0.05) !important;
      }

      /* Metodología card */
      .methodology-card {
        background: var(--bg-card);
        border-top: 4px solid var(--accent-primary);
        border-radius: 0;
        padding: 1.5rem;
        margin-top: 2rem;
        border: 1px solid var(--border-color);
      }

      .methodology-card h4 {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
        margin-bottom: 1rem;
        font-size: 1.125rem;
        font-weight: 800;
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
        border-radius: 0;
        overflow: hidden;
      }

      @media (max-width: 768px) {
        .home-name {
          font-size: 2rem;
        }

        .home-links {
          flex-direction: column;
          gap: 1rem;
        }
      }
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
        line=dict(dash="dash", color="#00ff88", width=1.5),
        showlegend=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["lower"],
        line=dict(dash="dash", color="#00ff88", width=1.5),
        fill="tonexty",
        fillcolor="rgba(0, 255, 136, 0.05)",
        showlegend=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=df_plot["Date"],
        y=df_plot["FX"],
        line=dict(color="#ff0088", width=2.5),
        showlegend=False,
    )
)

fig.update_layout(
    height=560,
    hovermode="x unified",
    margin=dict(l=20, r=20, t=20, b=20),
    plot_bgcolor="#2f2f2f",
    paper_bgcolor="#2a2a2a",
    font_color="#fff",
    font_family="Inter",
    xaxis=dict(
        gridcolor="#333",
        showgrid=True,
        linecolor="#333",
    ),
    yaxis=dict(
        gridcolor="#333",
        showgrid=True,
        linecolor="#333",
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
