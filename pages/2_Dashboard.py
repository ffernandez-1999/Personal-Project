import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import date


st.set_page_config(
    page_title="IPC vs IPCA (ENGHo 2017/18)",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS
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
      }

      h2, h3 { font-weight: 600 !important; }

      .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
      }

      .kpi-card, .controls-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }

      .methodology-card {
        background: linear-gradient(135deg, #f6f8fb 0%, #ffffff 100%);
        border-left: 4px solid #667eea;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      }

      .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# DATA LOADER
# ============================================================
@st.cache_data(ttl=12 * 60 * 60)
def get_ipc():
    url = "https://www.indec.gob.ar/ftp/cuadros/economia/serie_ipc_divisiones.csv"
    df = pd.read_csv(url, sep=";", decimal=",", encoding="latin1")
    df["Codigo"] = df["Codigo"].astype(str).str.strip()
    df["Codigo_num"] = pd.to_numeric(df["Codigo"], errors="coerce")
    df["Periodo"] = pd.to_datetime(df["Periodo"].astype(str), format="%Y%m")
    df["Indice_IPC"] = pd.to_numeric(df["Indice_IPC"], errors="coerce")
    return df.dropna(subset=["Periodo", "Codigo_num", "Indice_IPC"])

df = get_ipc()

# ============================================================
# TITLE
# ============================================================
st.title("IPC vs IPCA (ENGHo 2017/18)")

# ============================================================
# PREP DATA
# ============================================================
df_nac = df[df["Region"] == "Nacional"].copy()

ipc_level = (
    df_nac[df_nac["Codigo_num"] == 0][["Periodo", "Indice_IPC"]]
    .drop_duplicates("Periodo")
    .set_index("Periodo")["Indice_IPC"]
)

DIV_CODES = list(range(1, 13))
div_df = df_nac[df_nac["Codigo_num"].isin(DIV_CODES)][["Periodo", "Codigo_num", "Indice_IPC"]]
div_wide = div_df.pivot_table(index="Periodo", columns="Codigo_num", values="Indice_IPC")

common_idx = ipc_level.index.intersection(div_wide.index)
ipc_level = ipc_level.loc[common_idx]
div_wide = div_wide.loc[common_idx]

months = list(common_idx.sort_values())
months_d = [m.date() for m in months]

# ============================================================
# CONTROLES EN CARD
# ============================================================
st.markdown('<div class="controls-card">', unsafe_allow_html=True)
st.markdown("<div style='font-weight:600; margin-bottom:1rem;'>⚙️ Configuración</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([3, 1.5, 1.5])

with c1:
    start_d, end_d = st.slider(
        "📅 Rango de fechas",
        min_value=months_d[0],
        max_value=months_d[-1],
        value=(months_d[0], months_d[-1]),
        format="MMM-YY",
    )

with c2:
    measure = st.selectbox("📈 Medida", ["Mensual", "Interanual", "Acumulado"])

with c3:
    base_year = st.selectbox("📐 Año base (IPCA)", options=list(range(2017, 2026)))

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# CALC SERIES
# ============================================================
def compute_ipca(div_wide, base_year):
    base_avg = div_wide[div_wide.index.year == base_year].mean()
    ratios = div_wide.divide(base_avg)
    weights = np.repeat(1/12, 12)
    idx = 100 * (ratios.values @ weights)
    return pd.Series(idx, index=div_wide.index)

ipca_level = compute_ipca(div_wide, base_year)

mask = (common_idx >= pd.Timestamp(start_d)) & (common_idx <= pd.Timestamp(end_d))
ipc = ipc_level.loc[mask]
ipca = ipca_level.loc[mask]

if measure == "Mensual":
    ipc = ipc.pct_change() * 100
    ipca = ipca.pct_change() * 100
elif measure == "Interanual":
    ipc = ipc.pct_change(12) * 100
    ipca = ipca.pct_change(12) * 100
else:
    ipc = (ipc / ipc.iloc[0] - 1) * 100
    ipca = (ipca / ipca.iloc[0] - 1) * 100

ipc = ipc.dropna()
ipca = ipca.dropna()

# ============================================================
# LAYOUT
# ============================================================
kpi_col, main_col = st.columns([1, 2.5])

with kpi_col:
    st.markdown("### 📊 Indicadores Clave")

    if not ipc.empty:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-card-label">IPC Nacional</div>
                <div class="kpi-card-value">{ipc.iloc[-1]:.1f}%</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-card-label">IPCA</div>
                <div class="kpi-card-value">{ipca.iloc[-1]:.1f}%</div>
            </div>
        """, unsafe_allow_html=True)

with main_col:
    st.markdown("### 📈 Evolución Temporal")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=ipc.index,
        y=ipc.values,
        mode="lines+markers",
        name="IPC",
        line=dict(width=3, color="#667eea")
    ))

    fig.add_trace(go.Scatter(
        x=ipca.index,
        y=ipca.values,
        mode="lines+markers",
        name="IPCA",
        line=dict(width=3, color="#764ba2")
    ))

    fig.update_layout(
        height=550,
        hovermode="x unified",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    st.plotly_chart(fig, use_container_width=True)

st.caption("💡 Dashboard actualizado automáticamente desde INDEC")
