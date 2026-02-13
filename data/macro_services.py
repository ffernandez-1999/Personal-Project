# data/macro_services.py

import pandas as pd
import requests
import streamlit as st


# =========================
# IPC (INDEC)
# =========================

@st.cache_data(ttl=12 * 60 * 60)
def load_ipc_indec():
    url = "https://www.indec.gob.ar/ftp/cuadros/economia/serie_ipc_divisiones.csv"

    try:
        df = pd.read_csv(url, sep=";", decimal=",", encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(url, sep=";", decimal=",", encoding="latin1")

    df["Codigo"] = df["Codigo"].astype(str).str.strip()
    df["Codigo_num"] = pd.to_numeric(df["Codigo"], errors="coerce")
    df["Periodo"] = pd.to_datetime(df["Periodo"].astype(str), format="%Y%m", errors="coerce")

    for c in ["Indice_IPC", "v_m_IPC", "v_i_a_IPC"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df = df.dropna(subset=["Periodo", "Codigo_num"])
    return df.sort_values(["Periodo", "Codigo_num"]).reset_index(drop=True)


# =========================
# Tipo de Cambio (BCRA)
# =========================

@st.cache_data(ttl=6 * 60 * 60)
def load_tc_bcra():
    url = "https://api.bcra.gob.ar/estadisticas/v3.0/Monetarias/5"

    response = requests.get(url, timeout=10)
    data = response.json()

    df = pd.DataFrame(data["results"])

    df["fecha"] = pd.to_datetime(df["fecha"])
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    df = df.sort_values("fecha")
    return df


# =========================
# REM (Expectativas)
# =========================

@st.cache_data(ttl=6 * 60 * 60)
def load_rem():
    url = "https://api.bcra.gob.ar/estadisticas/v3.0/Expectativas/1"

    response = requests.get(url, timeout=10)
    data = response.json()

    df = pd.DataFrame(data["results"])

    df["fecha"] = pd.to_datetime(df["fecha"])
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    df = df.sort_values("fecha")
    return df
