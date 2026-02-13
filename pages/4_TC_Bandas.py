import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go


from data.macro_services import get_a3500, get_rem_last, get_ipc_bcra


# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="TC Mayorista y Bandas",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS (MISMO QUE IPC)
# ============================================================

st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 1rem; }

      html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      }

      h1 {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
      }

      .custom-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2.5rem;
        color: white;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
      }

      .header-title { font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; }
      .header-subtitle { font-size: 1.1rem; opacity: 0.95; font-weight: 500; }

      .header-links a {
        color: white !important;
        text-decoration: none;
        margin: 0 0.5rem;
        font-weight: 500;
      }

      .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
      }

      .kpi-card-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: rgba(0,0,0,0.5);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
      }

      .kpi-card-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
      }

      .methodology-card {
        background: linear-gradient(135deg, #f6f8fb 0%, #ffffff 100%);
        border-left: 4px solid #667eea;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HEADER PERSONALIZADO
# ============================================================

st.markdown(
    """
    <div class="custom-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div class="header-title">Francisco Fernandez Amato</div>
                <div class="header-subtitle">Macroeconomista</div>
            </div>
            <div class="header-links">
                <a href="mailto:franciscofernandezz1999@gmail.com">📧 Email</a>
                <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">💼 LinkedIn</a>
                <a href="https://github.com/ffernandez-1999" target="_blank">🔗 GitHub</a>
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

# ============================================================
# TÍTULO
# ============================================================

st.markdown(
    "<h1 style='text-align: center;'>TC Mayorista (A3500) y Bandas</h1>",
    unsafe_allow_html=True,
)

# ============================================================
# DATA
# ============================================================

with st.spinner("Cargando datos..."):
    fx = get_a3500().copy()
    fx["Date"] = pd.to_datetime(fx["Date"]).dt.normalize()

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


bands_2025 = build_bands_2025("2025-04-14", "2025-12-31", 1000.0, 1400.0)

bands = bands_2025.copy()

# ============================================================
# MASTER MERGE CORRECTO
# ============================================================

fx_min = fx["Date"].min()
last_fx_date = fx["Date"].max()
bands_max = bands["Date"].max()

cal = pd.DataFrame({
    "Date": pd.date_range(fx_min, bands_max, freq="D")
})

df = (
    cal.merge(fx, on="Date", how="left")
       .merge(bands, on="Date", how="left")
       .sort_values("Date")
)

df["FX"] = df["FX"].ffill()
df.loc[df["Date"] > last_fx_date, "FX"] = np.nan

# ============================================================
# LAYOUT KPIs + CHART
# ============================================================

kpi_col, main_col = st.columns([1, 2.5], gap="large")

with kpi_col:
    st.markdown("### 📊 Indicadores")

    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-card-label">Último TC</div>
            <div class="kpi-card-value">—</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-card-label">Variación mensual</div>
            <div class="kpi-card-value">—</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with main_col:
    st.markdown("### 📈 Evolución Temporal")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["upper"],
            name="Banda superior",
            line=dict(dash="dash"),
        )
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

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["FX"],
            name="TC Mayorista",
            line=dict(color="red"),
        )
    )

    fig.update_layout(
        height=560,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=40, b=20),
    )

    fig.update_yaxes(title="ARS/USD")

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# METODOLOGÍA (VACÍA POR AHORA)
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
