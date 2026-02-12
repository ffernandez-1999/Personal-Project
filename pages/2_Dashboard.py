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
      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      
      /* Reducir padding superior */
      section.main > div { padding-top: 1rem; }
      
      /* Tipografía general */
      html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      }
      
      /* Headers más bonitos */
      h1 {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
      }
      
      h2, h3 {
        font-weight: 600 !important;
      }
      
      /* Métricas mejoradas */
      [data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
      }
      
      [data-testid="stMetricLabel"] {
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        color: rgba(0,0,0,0.6) !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
      }
      
      /* Botones con mejor estilo */
      .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3) !important;
      }
      
      .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4) !important;
      }
      
      /* Selectbox y Slider más modernos */
      .stSelectbox > div > div {
        border-radius: 8px !important;
        border: 1px solid #e2e8f0 !important;
      }
      
      /* Slider con color azul oscuro */
      .stSlider > div > div > div > div {
        background-color: #1e3a8a !important;
      }
      
      .stSlider > div > div > div {
        background-color: #1e3a8a !important;
      }
      
      [data-baseweb="slider"] [role="slider"] {
        background-color: #1e3a8a !important;
      }
      
      [data-baseweb="slider"] > div > div {
        background-color: rgba(30, 58, 138, 0.2) !important;
      }
      
      [data-baseweb="slider"] [data-testid="stTickBar"] > div {
        background-color: #1e3a8a !important;
      }
      
      /* Ocultar labels de slider y cambiar colores */
      [data-baseweb="slider"] [data-testid="stTickBar"] {
        display: none !important;
      }
      
      .stSlider [data-testid="stTickBarMin"],
      .stSlider [data-testid="stTickBarMax"] {
        color: #1e3a8a !important;
      }
      
      /* Divider más sutil */
      hr {
        margin: 1.5rem 0 !important;
        border-color: #e2e8f0 !important;
      }
      
      /* Caption mejorado */
      .stCaption {
        color: rgba(0,0,0,0.5) !important;
        font-size: 0.875rem !important;
      }
      
      /* Card personalizada para metodología */
      .methodology-card {
        background: linear-gradient(135deg, #f6f8fb 0%, #ffffff 100%);
        border-left: 4px solid #667eea;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      }
      
      .methodology-card ul {
        margin-top: 0.5rem;
        padding-left: 1.2rem;
      }
      
      .methodology-card li {
        margin-bottom: 0.75rem;
        line-height: 1.6;
      }
      
      /* Header personalizado */
      .custom-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2.5rem;
        color: white;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
      }
      
      .header-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
      }
      
      .header-subtitle {
        font-size: 1.1rem;
        opacity: 0.95;
        font-weight: 500;
      }
      
      .header-links {
        font-size: 0.95rem;
        opacity: 0.95;
        margin-top: 0.5rem;
      }
      
      .header-links a {
        color: white !important;
        text-decoration: none;
        margin: 0 0.5rem;
        font-weight: 500;
      }
      
      .header-links a:hover {
        text-decoration: underline;
      }
      
      /* KPI cards personalizadas */
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
        background-clip: text;
        margin-bottom: 0.25rem;
      }
      
      /* Plotly container */
      .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      }
    </style>
    """,
    unsafe_allow_html=True,
    /* ================================
       SLIDER: ocultar puntas + labels
       ================================ */
    
    /* Oculta min/max (las "puntas" tipo Dec-16 / Jan-26) */
    [data-testid="stSlider"] [data-testid="stTickBarMin"],
    [data-testid="stSlider"] [data-testid="stTickBarMax"]{
      display: none !important;
    }
    
    /* Oculta los value labels (tipo Jan-25 / Jan-26 arriba) */
    [data-testid="stSlider"] [data-baseweb="slider"] [data-baseweb="tooltip"]{
      display: none !important;
    }
      
)

# ============================================================
# Header personalizado (reemplaza el top row)
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

# Botón volver (más chico y elegante)
col_btn, _ = st.columns([1, 5])
with col_btn:
    if st.button("← Volver"):
        st.switch_page("app.py")

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

def month_label(ts: pd.Timestamp) -> str:
    return ts.strftime("%Y-%m")

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
st.markdown("<h1 style='text-align: center;'>IPC vs IPCA (ENGHo 2017/18)</h1>", unsafe_allow_html=True)

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
# Controles (inline compactos sin título)
# ============================================================
c1, c2, c3 = st.columns([3, 1.5, 1.5], gap="medium")

with c1:
    start_default_date = next(
        (d for d in months_d if (d.year == 2025 and d.month == 1)),
        months_d[0]
    )

    # (A) Slider
    start_d, end_d = st.slider(
        "📅 Rango de fechas",
        min_value=months_d[0],
        max_value=months_d[-1],
        value=(start_default_date, months_d[-1]),
        format="MMM-YY",
    )

    # (B) Rango mostrado en azul (lo que vos querías ver)
    st.markdown(
        f"<div style='color:#1e3a8a; font-weight:700; margin-top:-6px;'>"
        f"{pd.Timestamp(start_d).strftime('%b-%y')} — {pd.Timestamp(end_d).strftime('%b-%y')}"
        f"</div>",
        unsafe_allow_html=True,
    )

    start_m = pd.Timestamp(start_d)
    end_m = pd.Timestamp(end_d)


with c2:
    measure = st.selectbox("📈 Medida", ["Mensual", "Interanual", "Acumulado"], index=0)

with c3:
    base_year = st.selectbox("📐 Año base (IPCA)", options=list(range(2017, 2026)), index=8)

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
# Layout: KPIs (izq) + Chart (der)
# ============================================================
kpi_col, main_col = st.columns([1, 2.5], gap="large")

with kpi_col:
    st.markdown("### 📊 Indicadores")

    if common.empty:
        st.warning("⚠️ No hay datos en el rango seleccionado.")
    else:
        last_date = common.max()
        st.caption(f"🕐 Último dato disponible: **{pd.to_datetime(last_date).strftime('%B %Y')}**")
        
        # Calculate monthly and annual variations
        ipc_monthly = ipc.iloc[-1] if len(ipc) > 0 else np.nan
        ipc_annual = calc_series(ipc_level_rng, "Interanual").iloc[-1] if len(ipc_level_rng) > 12 else np.nan
        
        ipca_monthly = ipca.iloc[-1] if len(ipca) > 0 else np.nan
        ipca_annual = calc_series(ipca_level_rng, "Interanual").iloc[-1] if len(ipca_level_rng) > 12 else np.nan
        
        # KPI IPC con variaciones
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-card-label">IPC Nacional</div>
                <div style="display: flex; align-items: baseline; gap: 1.5rem; margin-bottom: 0.5rem;">
                    <div class="kpi-card-value">{fmt_pct(ipc_monthly)}</div>
                    <div class="kpi-card-value" style="opacity: 0.4;">{fmt_pct(ipc_annual)}</div>
                </div>
                <div style="font-size: 0.75rem; color: rgba(0,0,0,0.5); font-weight: 600;">
                    <span>m/m</span>
                    <span style="margin-left: 6.5rem;">y/y</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        # KPI IPCA con variaciones
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-card-label">IPCA (ENGHo 2017/18)</div>
                <div style="display: flex; align-items: baseline; gap: 1.5rem; margin-bottom: 0.5rem;">
                    <div class="kpi-card-value">{fmt_pct(ipca_monthly)}</div>
                    <div class="kpi-card-value" style="opacity: 0.4;">{fmt_pct(ipca_annual)}</div>
                </div>
                <div style="font-size: 0.75rem; color: rgba(0,0,0,0.5); font-weight: 600;">
                    <span>m/m</span>
                    <span style="margin-left: 6.5rem;">y/y</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

with main_col:
    st.markdown("### 📈 Evolución Temporal")
    
    fig = go.Figure()

    # IPC
    fig.add_trace(
        go.Scatter(
            x=ipc.index,
            y=ipc.values,
            mode="lines+markers",
            marker=dict(size=7, color='#667eea'),
            line=dict(width=3, color='#667eea'),
            name="IPC",
            hovertemplate="IPC: %{y:.2f}%<extra></extra>",
        )
    )

    # IPCA
    fig.add_trace(
        go.Scatter(
            x=ipca.index,
            y=ipca.values,
            mode="lines+markers",
            marker=dict(size=7, color='#764ba2'),
            line=dict(width=3, color='#764ba2'),
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
            font=dict(size=14),
        ),
        hovermode="x unified",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(0,0,0,0.05)',
        showline=True,
        linewidth=1,
        linecolor='rgba(0,0,0,0.1)',
    )
    
    fig.update_yaxes(
        title="Variación %",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(0,0,0,0.05)',
        showline=True,
        linewidth=1,
        linecolor='rgba(0,0,0,0.1)',
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# Metodología (full width debajo del gráfico)
# ============================================================
st.markdown(
    """
    <div class="methodology-card">
        <h4 style="margin-top: 0; margin-bottom: 1rem; font-size: 1rem;">📖 Metodología</h4>
        <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.875rem; line-height: 1.6;">
            <li><b>IPC:</b> Inflación oficial del INDEC (nivel general, nacional)</li>
            <li><b>IPCA:</b> Índice que repondera las 12 divisiones COICOP usando ponderadores de ENGHo 2017/18</li>
            <li><b>Fuente:</b> CSV oficial del INDEC, actualizado automáticamente</li>
            <li><b>Cálculo:</b> Promedio ponderado de índices por división, normalizado a 100 en año base</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Footer
# ============================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("💡 Dashboard actualizado automáticamente desde fuentes oficiales del INDEC")
