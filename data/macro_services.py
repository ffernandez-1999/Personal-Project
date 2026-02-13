# data/macro_services.py

import pandas as pd
import requests
import streamlit as st


# ============================================================
# A3500 – BCRA API (v4.0)
# ============================================================

@st.cache_data(ttl=60 * 60)
def load_a3500() -> pd.DataFrame:
    url = "https://api.bcra.gob.ar/estadisticas/v4.0/Monetarias/84"
    params = {"Limit": 1000, "Offset": 0}
    data = []

    while True:
        r = requests.get(url, params=params, timeout=10, verify=False)
        r.raise_for_status()
        payload = r.json()

        results = payload.get("results", [])
        if not results:
            break

        detalle = results[0].get("detalle", [])
        if not detalle:
            break

        data.extend(detalle)

        meta = payload["metadata"]["resultset"]
        params["Offset"] += params["Limit"]

        if params["Offset"] >= meta["count"]:
            break

    if not data:
        return pd.DataFrame(columns=["Date", "FX"])

    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df["fecha"], errors="coerce")
    df["FX"] = pd.to_numeric(df["valor"], errors="coerce")

    return (
        df[["Date", "FX"]]
        .dropna()
        .drop_duplicates("Date")
        .sort_values("Date")
        .reset_index(drop=True)
    )


# ============================================================
# REM – última publicación
# ============================================================

@st.cache_data(ttl=60 * 60)
def load_rem_last():
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

    rem = (
        rem.loc[rem["Fecha de pronóstico"] == latest]
        .sort_values("Período")
        .tail(24)
        .rename(columns={"Período": "Date", "Mediana": "v_m_REM"})
        .assign(Date=lambda x: pd.to_datetime(x["Date"], errors="coerce"))
        .reset_index(drop=True)
    )

    return rem[["Date", "v_m_REM"]]


# ============================================================
# IPC – INDEC
# ============================================================

@st.cache_data(ttl=12 * 60 * 60)
def load_ipc_nacional_mensual():

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
