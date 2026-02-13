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
# CSS - DARK TECH (IGUAL QUE TC MAYORISTA)
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
        --bg-chart: #1e2433;
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

      .header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
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

      .header-links {
        display: flex;
        gap: 1.5rem;
        align-items: center;
      }

      .header-links a {
        color: var(--text-secondary);
        text-decoration: none;
        font-size: 0.875rem;
        transition: color 0.2s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
      }

      .header-links a:hover {
        color: var(--accent-primary);
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
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        height: 100%;
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

      .kpi-label {
        font-size: 0.75rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.75rem;
        font-weight: 500;
      }

      .kpi-main {
        font-family: 'Syne', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.02em;
      }

      .kpi-sub {
        font-family: 'Syne', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        opacity: 0.4;
      }

      .kpi-sublabel {
        font-size: 0.75rem;
        color: var(--text-muted);
        font-weight: 500;
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

      /* Selectbox */
      .stSelectbox label {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.75rem !important;
        color: var(--text-muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 500 !important;
      }

      .stSelectbox > div > div {
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
      }

      .stSelectbox [data-baseweb="select"] > div {
        background-color: var(--bg-secondary) !important;
        border-color: var(--border-color) !important;
        color: var(--text-primary) !important;
      }

      /* Slider personalizado */
      .stSlider label {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.75rem !important;
        color: var(--text-muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 500 !important;
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

      /* Caption */
      .stCaption {
        color: var(--text-muted) !important;
        font-size: 0.75rem !important;
      }

      /* Divider */
      hr {
        border-color: var(--border-color) !important;
        margin: 1.5rem 0 !important;
      }

      /* Responsive */
      @media (max-width: 768px) {
        .header-content {
          flex-direction: column;
          align-items: flex-start;
          gap: 1rem;
        }

        .header-links {
          flex-direction: column;
          align-items: flex-start;
          gap: 0.75rem;
        }
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
        <div class="header-content">
            <div>
                <div class="header-title">Francisco Fernandez Amato</div>
                <div class="header-subtitle">Macroeconomista</div>
            </div>
            <div class="header-links">
                <a href="mailto:franciscofernandezz1999@gmail.com">
                    <span>Gmail</span>
                </a>
                <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">
                    <span>LinkedIn</span>
                </a>
                <a href="https://github.com/ffernandez-1999" target="_blank">
                    <span>GitHub</span>
                </a>
            </div>
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

st.markdown("<h1 style='text-align: center;'>IPC vs IPCA (ENGHo 2017/18)</h1>", unsafe_allow_html=True)

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
# KPIs ARRIBA (2 CARDS CON 2 DATOS CADA UNO)
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
            <div class="kpi-card">
                <div class="kpi-label">IPC Nacional</div>
                <div style="display: flex; align-items: baseline; gap: 2rem; margin-bottom: 0.5rem;">
                    <div class="kpi-main">{fmt_pct(ipc_monthly)}</div>
                    <div class="kpi-sub">{fmt_pct(ipc_annual)}</div>
                </div>
                <div style="display: flex; gap: 7rem;">
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
            <div class="kpi-card">
                <div class="kpi-label">IPCA (ENGHo 2017/18)</div>
                <div style="display: flex; align-items: baseline; gap: 2rem; margin-bottom: 0.5rem;">
                    <div class="kpi-main">{fmt_pct(ipca_monthly)}</div>
                    <div class="kpi-sub">{fmt_pct(ipca_annual)}</div>
                </div>
                <div style="display: flex; gap: 7rem;">
                    <div class="kpi-sublabel">m/m</div>
                    <div class="kpi-sublabel">y/y</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.warning("⚠️ No hay datos en el rango seleccionado.")

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
            marker=dict(size=6, color='#0099ff'),
            line=dict(width=2.5, color='#0099ff'),
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
            marker=dict(size=6, color='#00d4aa'),
            line=dict(width=2.5, color='#00d4aa'),
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
        font=dict(size=12, family="JetBrains Mono", color="#e8eaed"),
    ),
    hovermode="x unified",
    plot_bgcolor='#1e2433',
    paper_bgcolor='#1a1f2e',
    font=dict(family="JetBrains Mono", color="#e8eaed"),
    xaxis=dict(
        gridcolor='#2a3041',
        showgrid=True,
        linecolor='#2a3041',
    ),
    yaxis=dict(
        title="Variación %",
        title_font=dict(size=12),
        gridcolor='#2a3041',
        showgrid=True,
        linecolor='#2a3041',
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
