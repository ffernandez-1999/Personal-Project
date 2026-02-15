# ============================================================
# METODOLOGÍA
# ============================================================

st.markdown(
    f"""
<div style="background:#ffffff;
            padding:2rem;
            border-radius:14px;
            border-top:4px solid #10b981;
            box-shadow:0 2px 8px rgba(0,0,0,0.08);">

<h3 style="font-family:Merriweather, serif;
           margin-bottom:1rem;
           color:#1a1a1a;">
📖 Metodología — IPCA (ENGHo 2017/18)
</h3>

<p style="font-size:0.95rem; line-height:1.7; color:#374151;">
El IPCA reconstruye el índice de precios al consumidor utilizando la
estructura de gasto observada en la Encuesta Nacional de Gastos de los
Hogares 2017/18 (ENGHo 2017/18).
</p>

<p style="font-size:0.95rem; line-height:1.7; color:#374151;">
Mantiene las variaciones oficiales por división publicadas por el INDEC,
pero modifica su incidencia agregada aplicando ponderaciones actualizadas
de consumo.
</p>

<hr style="margin:1.5rem 0; border-color:#e5e7eb;">

<h4 style="margin-bottom:0.75rem;">Especificación formal</h4>

<div style="text-align:center;
            font-size:1.1rem;
            margin:1rem 0;
            padding:1rem;
            background:#f9fafb;
            border-radius:8px;">
<b>
IPCA<sub>t</sub> =
100 · Σ<sub>i=1..12</sub>
w<sub>i</sub>
· ( I<sub>i,t</sub> / Ȳ<sub>i,base</sub> )
</b>
</div>

<p style="font-size:0.9rem; line-height:1.6;">
<b>w<sub>i</sub></b>: ponderadores fijos de la ENGHo 2017/18<br>
<b>I<sub>i,t</sub></b>: índice oficial INDEC por división (base 2004=100)<br>
<b>Ȳ<sub>i,base</sub></b>: promedio del índice en el año base seleccionado ({base_year})
</p>

<p style="font-size:0.9rem; line-height:1.6;">
El año base define el período en el cual el índice toma valor 100.
Las variaciones mensuales e interanuales se calculan a partir del nivel así construido.
</p>

<hr style="margin:1.5rem 0; border-color:#e5e7eb;">

<h4 style="margin-bottom:0.75rem;">Ponderaciones ENGHo 2017/18</h4>

<div style="columns:2; font-size:0.9rem; line-height:1.6;">
Alimentos y bebidas no alcohólicas — 22,7%<br>
Bebidas alcohólicas y tabaco — 2,0%<br>
Prendas de vestir y calzado — 6,8%<br>
Vivienda, agua y electricidad — 14,5%<br>
Equipamiento del hogar — 5,5%<br>
Salud — 6,4%<br>
Transporte — 14,3%<br>
Comunicaciones — 5,1%<br>
Recreación y cultura — 8,6%<br>
Educación — 3,1%<br>
Restaurantes y hoteles — 6,6%<br>
Bienes y servicios varios — 4,4%
</div>

<hr style="margin:1.5rem 0; border-color:#e5e7eb;">

<p style="font-size:0.85rem; color:#6b7280;">
Fuente: INDEC — Serie "Índice de precios al consumidor por divisiones".
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>")
st.caption("💡 Dashboard actualizado automáticamente desde fuentes oficiales del INDEC")
