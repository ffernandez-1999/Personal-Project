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
# CSS Mejorado (realista para Streamlit)
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

      /* ✅ NUEVO: Card para controles */
      .controls-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem 1.5rem 0.8rem 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
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
# Config
# ============================================================
DIV_CODES = list(range(1, 13))
W_2017 = {
    1: 22.7 / 100, 2: 2.0 / 100, 3: 6.8 / 100, 4: 14.5 / 100,
    5: 5.5 / 100, 6: 6.4 / 100, 7: 14.3 / 100, 8: 5.1 / 100,
    9: 8.6 / 100, 10: 3.1 / 100, 11: 6.6 / 100, 12: 4.4 / 100,
}

# ============================================================
# Loader INDEC
# ============================================================
@st.cache_data(ttl=12 * 60 * 60, show_spinner=False)
def get_ipc_indec_full() -> pd.DataFrame:
    url = "https://www.indec.gob.ar/ftp/cuadros/economia/serie_ipc_divisiones.csv"
    try:
        df = pd.read_csv(url, sep=";", decimal=",", encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(url, sep=";", decimal=",", encoding="latin1")

    df["Codigo"] = df["Codigo"].astype(str).str.strip()
    df["Codigo_num"] = pd.to_numeric(df["Codigo"], errors="coerce")
    df["Periodo"] = pd.to_datetime(df["Periodo"].astype(str), format="%Y%m", errors="coerce")

    for c in ["Descripcion", "Clasificador", "Region"]:
        df[c] = df[c].astype(str).str.strip()

    for c in ["Indice_IPC", "v_m_IPC", "v_i_a_IPC"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df = df.dropna(subset=["Periodo", "Codigo_num", "Indice_IPC"])
    return df.sort_values(["Periodo", "Codigo_num"]).reset_index(drop=True)

# ============================================================
# Helpers
# ============================================================
def fmt_pct(x):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    return f"{x:,.1f}%".replace(",", "X").replace(".", ",").replace("X", ".")

def compute_ipca_level(div_wide: pd.DataFrame, weights: dict, base_year: int) -> pd.Series:
    base_mask = div_wide.index.year == base_year
    base_avg = div_wide.loc[base_mask, DIV_CODES].mean(axis=0)
    if base_avg.isna().any():
        base_avg = div_wide[DIV_CODES].mean(axis=0)

    ratios = div_wide[DIV_CODES].divide(base_avg, axis=1)
    wvec = np.array([weights[c] for c in DIV_CODES], dtype=float)
    idx = 100.0 * (ratios.values @ wvec)
    return pd.Series(idx, index=div_wide.index, name="ipca")

def calc_series(level: pd.Series, measure: str) -> pd.Series:
    level = level.sort_index()
    if measure == "Mensual":
        return level.pct_change(1) * 100
    if measure == "Interanual":
        return level.pct_change(12) * 100
    if measure == "Acumulado":
        base = level.dropna().iloc[0] if not level.dropna().empty else np.nan
        return (level / base - 1) * 100
    raise ValueError("Medida inválida")

# ============================================================
# Data
# ============================================================
st.title("IPC vs IPCA (ENGHo 2017/18)")

df = get_ipc_indec_full()
df_nac = df[(df["Region"] == "Nacional") & (df["Clasificador"].str.contains("divisiones", case=False, na=False))].copy()

ipc_level = (
    df_nac[df_nac["Codigo_num"] == 0][["Periodo", "Indice_IPC"]]
    .drop_duplicates("Periodo")
    .sort_values("Periodo")
    .set_index("Periodo")["Indice_IPC"]
)

div_df = df_nac[df_nac["Codigo_num"].isin(DIV_CODES)][["Periodo", "Codigo_num", "Indice_IPC"]].copy()
div_wide = (
    div_df.pivot_table(index="Periodo", columns="Codigo_num", values="Indice_IPC", aggfunc="last")
    .sort_index()
)

common_idx = ipc_level.index.intersection(div_wide.index)
ipc_level = ipc_level.loc[common_idx]
div_wide = div_wide.loc[common_idx]
months = list(common_idx.sort_values())
months_d = [m.date() for m in months]

# ============================================================
# ✅ CONTROLES EN CARD (ÚNICO CAMBIO REAL)
# ============================================================
st.markdown('<div class="controls-card">', unsafe_allow_html=True)

c1, c2, c3 = st.columns([3, 1.5, 1.5], gap="medium")

with c1:
    start_default_date = next(
        (d for d in months_d if (d.year == 2025 and d.month == 1)),
        months_d[0]
    )

    start_d, end_d = st.slider(
        "📅 Rango de fechas",
        min_value=months_d[0],
        max_value=months_d[-1],
        value=(start_default_date, months_d[-1]),
        format="MMM-YY",
    )

    start_m = pd.Timestamp(start_d)
    end_m = pd.Timestamp(end_d)

    st.caption(f"📊 Período: {start_m.strftime('%b-%Y')} → {end_m.strftime('%b-%Y')}")

with c2:
    measure = st.selectbox("📈 Medida", ["Mensual", "Interanual", "Acumulado"], index=0)

with c3:
    base_year = st.selectbox("📐 Año base (IPCA)", options=list(range(2017, 2026)), index=8)

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ============================================================
# Range + series
# ============================================================
mask = (common_idx >= start_m) & (common_idx <= end_m)
ipc_level_rng = ipc_level.loc[mask]
div_wide_rng = div_wide.loc[mask]

ipca_level_rng = compute_ipca_level(div_wide_rng, W_2017, base_year)

ipc = calc_series(ipc_level_rng, measure).dropna()
ipca = calc_series(ipca_level_rng, measure).dropna()

common = ipc.index.intersection(ipca.index)
ipc = ipc.loc[common]
ipca = ipca.loc[common]

# ============================================================
# Layout: KPIs + Chart
# ============================================================
kpi_col, main_col = st.columns([1, 2.5], gap="large")

with kpi_col:
    st.markdown("### 📊 Indicadores Clave")

    if common.empty:
        st.warning("⚠️ No hay datos en el rango seleccionado.")
    else:
        last_date = common.max()
        st.caption(f"🕐 Último dato disponible: **{pd.to_datetime(last_date).strftime('%B %Y')}**")

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-card-label">IPC Nacional</div>
                <div class="kpi-card-value">{fmt_pct(ipc.iloc[-1])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-card-label">IPCA (ENGHo 2017/18)</div>
                <div class="kpi-card-value">{fmt_pct(ipca.iloc[-1])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with main_col:
    st.markdown("### 📈 Evolución Temporal")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=ipc.index,
            y=ipc.values,
            mode="lines+markers",
            marker=dict(size=7, color='#667eea'),
            line=dict(width=3, color='#667eea'),
            name="IPC",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ipca.index,
            y=ipca.values,
            mode="lines+markers",
            marker=dict(size=7, color='#764ba2'),
            line=dict(width=3, color='#764ba2'),
            name="IPCA (ENGHo 2017/18)",
        )
    )

    fig.update_layout(
        height=560,
        hovermode="x unified",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )

    st.plotly_chart(fig, use_container_width=True)

st.caption("💡 Dashboard actualizado automáticamente desde fuentes oficiales del INDEC")
