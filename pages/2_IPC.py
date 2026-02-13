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
# CSS - DARK TECH (CORREGIDO)
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

      /* KPI Cards MÁS CLAROS */
      .kpi-card-compact {
        background: var(--bg-card);
        padding: 1.5rem;
        border-radius: 0;
        border: 1px solid var(--border-color);
        border-top: 4px solid var(--accent-primary);
        transition: all 0.3s ease;
      }

      .kpi-card-compact:hover {
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

      .kpi-values {
        display: flex;
        align-items: baseline;
        gap: 1.5rem;
      }

      .kpi-main {
        font-family: 'Inter', sans-serif;
        font-size: 2.25rem;
        font-weight: 800;
        color: var(--text-primary);
        letter-spacing: -0.02em;
        line-height: 1;
      }

      .kpi-secondary {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
        color: var(--text-secondary);
        opacity: 0.5;
        line-height: 1;
      }

      .kpi-labels {
        display: flex;
        gap: 3.5rem;
        margin-top: 0.5rem;
      }

      .kpi-sublabel {
        font-size: 0.7rem;
        color: var(--text-muted);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
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

      /* Selectbox */
      .stSelectbox label {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.75rem !important;
        color: var(--text-secondary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 600 !important;
      }

      .stSelectbox [data-baseweb="select"] {
        background-color: var(--bg-secondary) !important;
      }

      .stSelectbox [data-baseweb="select"] > div {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-primary) !important;
        font-weight: 500 !important;
      }

      .stSelectbox [data-baseweb="select"] span {
        color: var(--text-primary) !important;
      }

      /* Dropdown menu */
      [data-baseweb="popover"] {
        background-color: var(--bg-secondary) !important;
      }

      [role="listbox"] {
        background-color: var(--bg-secondary) !important;
      }

      [role="option"] {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
      }

      [role="option"]:hover {
        background-color: var(--bg-card) !important;
      }

      /* Slider */
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

      /* Caption */
      .stCaption {
        color: var(--text-muted) !important;
        font-size: 0.75rem !important;
      }

      /* Divider */
      hr {
        border-color: var(--border-color) !important;
        margin: 2rem 0 !important;
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

# Botón volver
col_btn, _ = st.columns([1, 5])
with col_btn:
    if st.button("← Volver"):
        st.switch_page("app.py")

# TÍTULO MÁS DESTACADO
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
# CONTROLES: Selectores a la izquierda, Rango a la derecha
# ============================================================

c1, c2, c3 = st.columns([1.5, 1.5, 3], gap="medium")

with c1:
    measure = st.selectbox("📈 Medida", ["Mensual", "Interanual", "Acumulado"], index=0)

with c2:
    base_year = st.selectbox("📐 Año base (IPCA)", options=list(range(2017, 2026)), index=8)

with c3:
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

st.divider()

# ============================================================
# CALCULAR DATOS
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
# KPIs COMPACTOS ARRIBA
# ============================================================

if not common.empty:
    last_date = common.max()
    
    # Calcular variaciones mensuales y anuales
    ipc_monthly = ipc.iloc[-1] if len(ipc) > 0 else np.nan
    ipc_annual = calc_series(ipc_level_rng, "Interanual").iloc[-1] if len(ipc_level_rng) > 12 else np.nan
    
    ipca_monthly = ipca.iloc[-1] if len(ipca) > 0 else np.nan
    ipca_annual = calc_series(ipca_level_rng, "Interanual").iloc[-1] if len(ipca_level_rng) > 12 else np.nan
    
    # 2 columnas para los 2 KPIs
    kpi1, kpi2 = st.columns(2, gap="large")
    
    with kpi1:
        st.markdown(
            f"""
            <div class="kpi-card-compact">
                <div class="kpi-label">IPC NACIONAL</div>
                <div class="kpi-values">
                    <div class="kpi-main">{fmt_pct(ipc_monthly)}</div>
                    <div class="kpi-secondary">{fmt_pct(ipc_annual)}</div>
                </div>
                <div class="kpi-labels">
                    <div class="kpi-sublabel">m/m</div>
                    <div class="kpi-sublabel">y/y</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with kpi2:
        st.markdown(
            f"""
            <div class="kpi-card-compact">
                <div class="kpi-label">IPCA (ENGHO 2017/18)</div>
                <div class="kpi-values">
                    <div class="kpi-main">{fmt_pct(ipca_monthly)}</div>
                    <div class="kpi-secondary">{fmt_pct(ipca_annual)}</div>
                </div>
                <div class="kpi-labels">
                    <div class="kpi-sublabel">m/m</div>
                    <div class="kpi-sublabel">y/y</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.warning("⚠️ No hay datos en el rango seleccionado.")

# ESPACIO ENTRE KPIs Y GRÁFICO
st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

# ============================================================
# GRÁFICO (TODO EL ANCHO)
# ============================================================

fig = go.Figure()

if not common.empty:
    # IPC
    fig.add_trace(
        go.Scatter(
            x=ipc.index,
            y=ipc.values,
            mode="lines+markers",
            marker=dict(size=6, color='#00ff88'),
            line=dict(width=2.5, color='#00ff88'),
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
            marker=dict(size=6, color='#ff0088'),
            line=dict(width=2.5, color='#ff0088'),
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
        font=dict(size=12, family="Inter", color="#fff"),
    ),
    hovermode="x unified",
    plot_bgcolor='#2f2f2f',
    paper_bgcolor='#2a2a2a',
    font=dict(family="Inter", color="#fff"),
    xaxis=dict(
        gridcolor='#333',
        showgrid=True,
        linecolor='#333',
    ),
    yaxis=dict(
        title="Variación %",
        title_font=dict(size=12),
        gridcolor='#333',
        showgrid=True,
        linecolor='#333',
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

# ============================================================
# FOOTER
# ============================================================
st.markdown("<br>", unsafe_allow_html=True)
st.caption("💡 Dashboard actualizado automáticamente desde fuentes oficiales del INDEC")
