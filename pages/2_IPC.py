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
# CSS - LIGHT THEME + Merriweather/Lato
# ============================================================

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');

      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 2rem; }

      /* Ocultar/aclarar header de Streamlit */
      header[data-testid="stHeader"] {
        background-color: #f5f7fa !important;
      }

      /* Ocultar toolbar arriba */
      [data-testid="stToolbar"] {
        display: none !important;
      }

      /* Fondo claro */
      .stApp {
        background: #f5f7fa !important;
        color: #1a1a1a;
      }

      /* Tipografía global */
      html, body, [class*="css"], p, span, div {
        font-family: 'Lato', sans-serif !important;
        color: #1a1a1a !important;
      }
      
      h1, h2, h3, h4 {
        font-family: 'Merriweather', Georgia, serif !important;
        color: #1a1a1a !important;
      }

      /* Header simple */
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

      /* Título de página */
      .page-title-highlight {
        font-family: 'Merriweather', Georgia, serif;
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: #ffffff;
        border-radius: 12px;
        border-top: 4px solid #10b981;
        letter-spacing: -0.02em;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        color: #1a1a1a;
      }

      /* KPI Cards */
      .kpi-card-compact {
        background: #ffffff;
        padding: 1.25rem;
        border-radius: 12px;
        border-top: 4px solid #10b981;
        transition: all 0.25s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      }
      
      .kpi-card-compact:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      }

    .kpi-label {
        font-family: 'Lato', sans-serif;
        font-size: 0.75rem;
        color: #4a5568;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }

      .kpi-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        column-gap: 1.5rem;
        row-gap: 0.25rem;
        align-items: baseline;
      }

      .kpi-value {
        font-family: 'Lato', sans-serif;
        font-size: 1.8rem;
        font-weight: 400;
        color: #1a1a1a;
        letter-spacing: -0.02em;
        line-height: 1;
      }

      .kpi-sublabel {
        font-size: 0.7rem;
        color: #718096;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 0.25rem;
        font-family: 'Lato', sans-serif;
      }

      /* Selectbox */
      .stSelectbox label {
        font-family: 'Lato', sans-serif !important;
        font-size: 0.75rem !important;
        color: #4a5568 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
      }

      .stSelectbox [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 2px solid #e2e8f0 !important;
        color: #1a1a1a !important;
        cursor: pointer !important;
        border-radius: 8px !important;
        transition: border-color .2s ease, box-shadow .2s ease;
      }

      .stSelectbox [data-baseweb="select"] > div:hover {
        border-color: #10b981 !important;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1) !important;
      }

      .stSelectbox [data-baseweb="select"] > div:focus-within {
        border-color: #10b981 !important;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15) !important;
      }

      .stSelectbox [data-baseweb="select"] span {
        color: #1a1a1a !important;
        font-weight: 600 !important;
      }

      /* Dropdown */
      div[data-baseweb="popover"] > div {
        background: #ffffff !important;
        border: 2px solid #e2e8f0 !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15) !important;
        border-radius: 8px !important;
      }

      ul[role="listbox"] { 
        background: #ffffff !important;
      }
      
      li[role="option"] { 
        background: #ffffff !important;
        color: #1a1a1a !important;
      }
      
      li[role="option"]:hover,
      li[role="option"][aria-selected="true"] {
        background: #f7fafc !important;
      }

      /* Slider */
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
        background-color: #10b981 !important;
      }
      
      .stSlider [role="slider"] {
        background-color: #10b981 !important;
      }

      .stSlider [data-testid="stTickBarMin"],
      .stSlider [data-testid="stTickBarMax"] {
        color: #4a5568 !important;
        font-weight: 500 !important;
      }

      /* Botón volver */
      .stButton > button {
        background: #10b981 !important;
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

      /* Metodología */
      .methodology-card {
        background: #ffffff !important;
        border-top: 4px solid #10b981;
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

      /* Divider */
      hr {
        border-color: #e2e8f0 !important;
        margin: 1.8rem 0 !important;
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
    '<div class="page-title-highlight">IPC vs IPCA (ENGHo 2017/18)</div>',
    unsafe_allow_html=True
)

# ============================================================
# CONFIG
# ============================================================
DIV_CODES = list(range(1, 13))
W_2017 = {
    1: 22.7 / 100, 2: 2.0 / 100, 3: 6.8 / 100, 4: 14.5 / 100,
    5: 5.5 / 100, 6: 6.4 / 100, 7: 14.3 / 100, 8: 5.1 / 100,
    9: 8.6 / 100, 10: 3.1 / 100, 11: 6.6 / 100, 12: 4.4 / 100,
}

# ============================================================
# LOADER INDEC
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
# HELPERS
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
# DATA
# ============================================================
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
# CONTROLES + KPIs (misma zona, misma fila)
# ============================================================

c1, c2, k1, k2 = st.columns([1.35, 1.55, 1.55, 1.55], gap="medium")

with c1:
    measure = st.selectbox("Seleccioná la medida", ["Mensual", "Interanual", "Acumulado"], index=0, key="medida")

with c2:
    base_year = st.selectbox("Seleccioná el año base del IPCA", options=list(range(2017, 2026)), index=8, key="base_ipca")

# Slider (fila 2)
cR = st.columns([1], gap="medium")[0]
with cR:
    start_default_date = next((d for d in months_d if (d.year == 2025 and d.month == 1)), months_d[0])
    start_d, end_d = st.slider(
        "Rango de fechas",
        min_value=months_d[0],
        max_value=months_d[-1],
        value=(start_default_date, months_d[-1]),
        format="MMM-YY",
        key="rango",
    )
    start_m = pd.Timestamp(start_d)
    end_m = pd.Timestamp(end_d)

# ============================================================
# CALCULAR
# ============================================================
ipca_level_full = compute_ipca_level(div_wide, W_2017, base_year)

ipc_full = calc_series(ipc_level, measure)
ipca_full = calc_series(ipca_level_full, measure)

# Después aplicar rango
mask = (ipc_full.index >= start_m) & (ipc_full.index <= end_m)
ipc = ipc_full.loc[mask]
ipca = ipca_full.loc[mask]


common = ipc.index.intersection(ipca.index)
ipc = ipc.loc[common]
ipca = ipca.loc[common]

# KPIs arriba (k1/k2)
with k1:
    if not ipc.empty:
        ipc_monthly = calc_series(ipc_level, "Mensual").loc[ipc.index].dropna().iloc[-1] if len(ipc.index) > 0 else np.nan
        ipc_annual  = calc_series(ipc_level, "Interanual").loc[ipc.index].dropna().iloc[-1] if len(ipc.index) > 0 else np.nan

        st.markdown(
            f"""
            <div class="kpi-card-compact">
                <div class="kpi-label">IPC NACIONAL</div>
                <div class="kpi-grid">
                    <div class="kpi-value">{fmt_pct(ipc_monthly)}</div>
                    <div class="kpi-value">{fmt_pct(ipc_annual)}</div>
                    <div class="kpi-sublabel">m/m</div>
                    <div class="kpi-sublabel">y/y</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown("<div style='height:92px'></div>", unsafe_allow_html=True)


with k2:
    if not ipca.empty:
        ipca_monthly = calc_series(ipca_level_full, "Mensual").loc[ipca.index].dropna().iloc[-1] if len(ipca.index) > 0 else np.nan
        ipca_annual  = calc_series(ipca_level_full, "Interanual").loc[ipca.index].dropna().iloc[-1] if len(ipca.index) > 0 else np.nan

        st.markdown(
            f"""
            <div class="kpi-card-compact">
                <div class="kpi-label">IPCA (ENGHO 2017/18)</div>
                <div class="kpi-grid">
                    <div class="kpi-value">{fmt_pct(ipca_monthly)}</div>
                    <div class="kpi-value">{fmt_pct(ipca_annual)}</div>
                    <div class="kpi-sublabel">m/m</div>
                    <div class="kpi-sublabel">y/y</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown("<div style='height:92px'></div>", unsafe_allow_html=True)


st.divider()

# ============================================================
# GRÁFICO
# ============================================================
fig = go.Figure()

if not common.empty:
    fig.add_trace(
        go.Scatter(
            x=ipc.index,
            y=ipc.values,
            mode="lines+markers",
            marker=dict(size=6, color="#10b981"),
            line=dict(width=2.5, color="#10b981"),
            name="IPC",
            hovertemplate="IPC: %{y:.2f}%<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ipca.index,
            y=ipca.values,
            mode="lines+markers",
            marker=dict(size=6, color="#3b82f6"),
            line=dict(width=2.5, color="#3b82f6"),
            name="IPCA (ENGHo 2017/18)",
            hovertemplate="IPCA: %{y:.2f}%<extra></extra>",
        )
    )

fig.update_layout(
    height=560,
    margin=dict(l=20, r=20, t=40, b=20),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0,
        font=dict(size=12, family="Lato", color="#1a1a1a"),
    ),
    hovermode="x unified",
    plot_bgcolor="#ffffff",
    paper_bgcolor="#ffffff",
    font=dict(family="Lato", color="#1a1a1a"),
    xaxis=dict(gridcolor="#e2e8f0", showgrid=True, linecolor="#cbd5e0"),
    yaxis=dict(
        title="Variación %",
        title_font=dict(size=12, family="Lato"),
        gridcolor="#e2e8f0",
        showgrid=True,
        linecolor="#cbd5e0",
    ),
)

st.plotly_chart(fig, use_container_width=True)

# ============================================================
# METODOLOGÍA
# ============================================================
st.markdown(
    """
    <div class="methodology-card">
        <h4>📖 Metodología</h4>
        <ul>
            <li><b>IPC:</b> Inflación oficial del INDEC (nivel general, nacional)</li>
            <li><b>IPCA:</b> Índice que repondera las 12 divisiones COICOP usando ponderadores de ENGHo 2017/18</li>
            <li><b>Fuente:</b> CSV oficial del INDEC, actualizado automáticamente</li>
            <li><b>Cálculo:</b> Promedio ponderado de índices por división, normalizado a 100 en año base</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("💡 Dashboard actualizado automáticamente desde fuentes oficiales del INDEC")
