# data/macro_services.py

import pandas as pd
import requests
import streamlit as st


# ============================================================
# MONETARIAS GENERIC
# ============================================================

@st.cache_data(ttl=60 * 60)
def get_monetaria_serie(id_variable: int) -> pd.DataFrame:
    url = f"https://api.bcra.gob.ar/estadisticas/v4.0/Monetarias/{id_variable}"
    r = requests.get(url, timeout=10, verify=False)
    r.raise_for_status()

    data = r.json()["results"][0]["detalle"]

    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df["fecha"], errors="coerce")
    df["value"] = pd.to_numeric(df["valor"], errors="coerce")

    return (
        df[["Date", "value"]]
        .dropna()
        .drop_duplicates("Date")
        .sort_values("Date")
        .reset_index(drop=True)
    )


# ============================================================
# TC MAYORISTA (A3500)
# ============================================================

@st.cache_data(ttl=60 * 60)
def get_a3500() -> pd.DataFrame:

    df = get_monetaria_serie(5)

    if df.empty:
        df = get_monetaria_serie(84)

    if df.empty:
        return pd.DataFrame(columns=["Date", "FX"])

    out = df.rename(columns={"value": "FX"}).copy()

    return (
        out[["Date", "FX"]]
        .dropna()
        .drop_duplicates("Date")
        .sort_values("Date")
        .reset_index(drop=True)
    )


# ============================================================
# REM
# ============================================================

@st.cache_data(ttl=60 * 60)
def get_rem_last() -> pd.DataFrame:

    url = (
        "https://www.bcra.gob.ar/archivos/Pdfs/PublicacionesEstadisticas/"
        "historico-relevamiento-expectativas-mercado.xlsx"
    )

    df = pd.read_excel(url, sheet_name="Base de Datos Completa", skiprows=1)

    rem = df.loc[
        (df["Variable"] == "Precios minoristas (IPC nivel general; INDEC)")
        & (df["Referencia"] == "var. % mensual")
    ].copy()

    latest = rem["Fecha de pronóstico"].max()

    return (
        rem.loc[rem["Fecha de pronóstico"] == latest]
        .sort_values("Período")
        .tail(24)
        .rename(columns={"Período": "Date", "Mediana": "v_m_REM"})
        .assign(Date=lambda x: pd.to_datetime(x["Date"], errors="coerce"))
        .reset_index(drop=True)
    )


# ============================================================
# IPC NACIONAL MENSUAL
# ============================================================

@st.cache_data(ttl=12 * 60 * 60)
def get_ipc_bcra() -> pd.DataFrame:

    url = "https://www.indec.gob.ar/ftp/cuadros/economia/serie_ipc_divisiones.csv"

    try:
        df = pd.read_csv(url, sep=";", decimal=",", encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(url, sep=";", decimal=",", encoding="latin1")

    df["Codigo"] = pd.to_numeric(df["Codigo"], errors="coerce")
    df["Periodo"] = pd.to_datetime(df["Periodo"].astype(str), format="%Y%m", errors="coerce")

    df = df[(df["Codigo"] == 0) & (df["Region"] == "Nacional")]
    df = df.dropna(subset=["v_m_IPC"]).sort_values("Periodo")

    df["Period"] = df["Periodo"].dt.to_period("M")
    df["v_m_CPI"] = df["v_m_IPC"] / 100.0

    return (
        df[["Periodo", "Period", "v_m_CPI"]]
        .rename(columns={"Periodo": "Date"})
        .drop_duplicates("Period")
        .reset_index(drop=True)
    )
