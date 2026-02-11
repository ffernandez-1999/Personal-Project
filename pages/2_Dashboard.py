import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="IPC vs IPCA (ENGHo 2017/18)",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Oculta sidebar también en esta página ---
st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      section.main > div { padding-top: 1.0rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Top row: botón volver + mini header derecha
# ============================================================
top_left, top_right = st.columns([1, 3], gap="large")

with top_left:
    if st.button("← Volver al Home"):
        st.switch_page("app.py")

with top_right:
    st.markdown(
        """
        <div style="text-align:right; line-height:1.2;">
            <div style="font-size:22px; font-weight:700;">
                Francisco Fernandez Amato
            </div>
            <div style="margin-top:6px; font-size:14px;">
                <a href="mailto:franciscofernandezz1999@gmail.com">Email</a>
                &nbsp;·&nbsp;
                <a href="https://www.linkedin.com/in/francisco-fernandez-amato-7725ba241/" target="_blank">LinkedIn</a>
                &nbsp;·&nbsp;
                <a href="https://github.com/ffernandez-1999" target="_blank">GitHub</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

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

# ============================================================
# Controles (arriba, alineados con el panel derecho)
# ============================================================
_, ctrl_col = st.columns([1, 3], gap="large")
with ctrl_col:
    c1, c2, c3 = st.columns([2.2, 1.2, 1.2], gap="medium")

    with c1:
        start_default_date = next(
            (m for m in months if (m.year == 2025 and m.month == 1)),
            months[0]
        )
        
        start_m, end_m = st.slider(
            "Rango de fechas",
            min_value=months[0],
            max_value=months[-1],
            value=(start_default_date, months[-1]),
            format="MMM-YY",   # ← clave
        )

        st.caption(f"{start_m.strftime('%b-%Y')} → {end_m.strftime('%b-%Y')}")


    with c2:
        measure = st.selectbox("Medida", ["Mensual", "Interanual", "Acumulado"], index=0)

    with c3:
        base_year = st.selectbox("Año base (IPCA)", options=list(range(2017, 2026)), index=8)

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
kpi_col, main_col = st.columns([1, 3], gap="large")

with kpi_col:
    st.subheader("📌 KPIs")

    if common.empty:
        st.warning("No hay datos en el rango seleccionado.")
    else:
        last_date = common.max()
        st.caption(f"Último dato: {pd.to_datetime(last_date).strftime('%b-%Y')}")
        st.metric("IPC", fmt_pct(ipc.iloc[-1]))
        st.metric("IPCA (ENGHo 2017/18)", fmt_pct(ipca.iloc[-1]))

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    st.divider()

    st.markdown("**📌 Metodología**")
    st.markdown(
        """
<div style="font-size:13px; line-height:1.35; color: rgba(0,0,0,0.75);">
<ul style="margin-top:6px;">
  <li><b>IPC:</b> inflación oficial del INDEC (Nivel general, Nacional), tomada del CSV publicado por el organismo.</li>
  <li><b>IPCA (ENGHo 2017/18):</b> índice sintético que repondera las <b>12 divisiones COICOP</b> usando la estructura de gasto de la <b>ENGHo 2017/18</b>.
      Se agregan los <b>índices por división</b> mediante un <b>promedio ponderado</b> y se normaliza a 100 por el año base elegido.</li>
  <li><b>Actualización automática:</b> el dashboard descarga el CSV oficial y recalcula IPC/IPCA (con caché para performance).</li>
</ul>
</div>
""",
        unsafe_allow_html=True,
    )

with main_col:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=ipc.index,
            y=ipc.values,
            mode="lines+markers",
            marker=dict(size=6),
            name="IPC",
            hovertemplate="%{x|%b-%Y}<br>IPC: %{y:.2f}%<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=ipca.index,
            y=ipca.values,
            mode="lines+markers",
            marker=dict(size=6),
            name="IPCA (ENGHo 2017/18)",
            hovertemplate="%{x|%b-%Y}<br>IPCA: %{y:.2f}%<extra></extra>",
        )
    )

    fig.update_layout(
        height=560,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=15),
        ),
        hovermode="x",
    )
    fig.update_yaxes(title="%")

    # Streamlit nuevo: reemplaza use_container_width
    st.plotly_chart(fig, width="stretch")
