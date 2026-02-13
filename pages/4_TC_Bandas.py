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
# CSS (IGUAL IPC)
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

      .custom-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2.5rem;
        color: white;
        box-shadow: 0 8px 24px rgba(102,126,234,0.3);
      }

      .header-title { font-size: 2rem; font-weight: 700; }
      .header-subtitle { font-size: 1.1rem; opacity: 0.95; }

      .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
      }

      .kpi-main {
        font-size: 2.7rem;
        font-weight: 700;
        color: #667eea;
      }

      .kpi-date {
        font-size: 0.9rem;
        color: rgba(0,0,0,0.5);
        margin-left: 0.5rem;
      }

      .kpi-sub {
        font-size: 2rem;
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
                    <div style="font-size:0.8rem; color:gray;">m/m</div>
                </div>
                <div>
                    <div class="kpi-sub">{yy:.1f}%</div>
                    <div style="font-size:0.8rem; color:gray;">y/y</div>
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
            line=dict(dash="dash"),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_plot["Date"],
            y=df_plot["lower"],
            line=dict(dash="dash"),
            fill="tonexty",
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_plot["Date"],
            y=df_plot["FX"],
            line=dict(color="red"),
            showlegend=False,
        )
    )

    fig.update_layout(
        height=560,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=20, b=20),
    )

    fig.update_yaxes(title="ARS/USD")

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
