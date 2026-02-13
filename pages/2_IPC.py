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

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

/* ========== VARIABLES ========== */
:root {
  --bg-primary: #f8fafc;
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

/* ========== BASE ========== */
.stApp { background-color: var(--bg-primary); color: var(--text-primary); }
html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

header[data-testid="stHeader"] { background-color: #1a1a1a !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }

/* ========== HEADER ========== */
.home-header { margin-bottom: 3rem; padding: 0 1rem; }
.home-name { font-size: 2.5rem; font-weight: 800; margin-bottom: .5rem; }
.home-role { font-size: .95rem; color: var(--text-muted); margin-bottom: 1.5rem; }
.home-links { display:flex; gap:2rem; font-size:.875rem; }
.home-links a { color: var(--text-muted); text-decoration:none; }
.home-links a:hover { color:#fff; }

/* ========== TÍTULO ========== */
.page-title-highlight {
  font-size: 2rem;
  font-weight: 800;
  text-align:center;
  margin-bottom:2.5rem;
  padding:1rem;
  background:var(--bg-card);
  border-top:4px solid var(--accent-primary);
}

/* ========== KPI ========== */
.kpi-card {
  background: var(--bg-card);
  padding: 1rem 1.2rem;
  border:1px solid var(--border-color);
  border-top:4px solid var(--accent-primary);
}

.kpi-title {
  font-size:.7rem;
  color:var(--text-muted);
  text-transform:uppercase;
  letter-spacing:.1em;
  margin-bottom:.7rem;
}

.kpi-grid {
  display:grid;
  grid-template-columns:1fr 1fr;
  column-gap:2rem;
  row-gap:.2rem;
}

.kpi-value {
  font-size:2rem;
  font-weight:600;   /* sin negrita pesada */
  letter-spacing:-.02em;
}

.kpi-label {
  font-size:.7rem;
  color:var(--text-muted);
  text-transform:uppercase;
}

/* ========== SELECTORES ========== */

.stSelectbox label {
  font-size:.75rem !important;
  text-transform:uppercase !important;
  color:var(--text-secondary) !important;
  letter-spacing:.05em !important;
}

.stSelectbox [data-baseweb="select"] > div {
  background-color: var(--bg-secondary) !important;
  border:1px solid var(--border-color) !important;
  transition: all .15s ease;
}

/* Hover real */
.stSelectbox [data-baseweb="select"] > div:hover {
  border-color: var(--accent-primary) !important;
  box-shadow: 0 0 0 2px rgba(0,255,136,.12) !important;
}

/* Focus real */
.stSelectbox [data-baseweb="select"] > div:focus-within {
  border-color: var(--accent-primary) !important;
  box-shadow: 0 0 0 3px rgba(0,255,136,.18) !important;
}

/* Flecha */
.stSelectbox [data-baseweb="select"] svg {
  transform: scale(1.15);
  opacity:.9;
}

/* ========== SLIDER ========== */
.stSlider [data-baseweb="slider"] > div > div,
.stSlider [role="slider"] {
  background-color: var(--accent-primary) !important;
}

/* ========== BOTÓN ========== */
.stButton > button {
  background:transparent !important;
  border:1px solid var(--border-color) !important;
  color:var(--text-primary) !important;
  font-weight:600 !important;
}
.stButton > button:hover {
  border-color:var(--accent-primary) !important;
  background:rgba(0,255,136,.05) !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="home-header">
  <div class="home-name">Francisco Fernandez Amato</div>
  <div class="home-role">Macroeconomista</div>
  <div class="home-links">
    <a href="#">Email</a>
    <a href="#">LinkedIn</a>
    <a href="#">GitHub</a>
  </div>
</div>
""", unsafe_allow_html=True)

col_btn,_ = st.columns([1,5])
with col_btn:
    if st.button("← Volver"):
        st.switch_page("app.py")

st.markdown('<div class="page-title-highlight">IPC vs IPCA (ENGHo 2017/18)</div>', unsafe_allow_html=True)

# ============================================================
# CONTROLES
# ============================================================

c1,c2,c3 = st.columns([1.5,1.5,3])

with c1:
    measure = st.selectbox("Seleccioná la medida", ["Mensual","Interanual","Acumulado"])

with c2:
    base_year = st.selectbox("Seleccioná el año base del IPCA", list(range(2017,2026)))

with c3:
    start,end = st.slider("Rango de fechas",
                          min_value=date(2017,1,1),
                          max_value=date(2026,1,1),
                          value=(date(2025,1,1),date(2026,1,1)))

st.divider()

# ============================================================
# KPIs (demo valores)
# ============================================================

k1,k2 = st.columns(2)

with k1:
    st.markdown("""
    <div class="kpi-card">
      <div class="kpi-title">IPC NACIONAL</div>
      <div class="kpi-grid">
        <div class="kpi-value">2,9%</div>
        <div class="kpi-value">32,4%</div>
        <div class="kpi-label">m/m</div>
        <div class="kpi-label">y/y</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="kpi-card">
      <div class="kpi-title">IPCA (ENGHo 2017/18)</div>
      <div class="kpi-grid">
        <div class="kpi-value">2,7%</div>
        <div class="kpi-value">32,9%</div>
        <div class="kpi-label">m/m</div>
        <div class="kpi-label">y/y</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
