# pages/3_Notes.py
import streamlit as st
import textwrap

st.set_page_config(
    page_title="Artículos Macro",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CSS - LIGHT THEME + Merriweather/Lato
# ============================================================
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Lato:wght@400;600;700&display=swap');

      /* Ocultar sidebar */
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="stSidebarNav"] { display: none !important; }
      [data-testid="collapsedControl"] { display: none !important; }
      section.main > div { padding-top: 2rem; }

      /* Ocultar/aclarar header de Streamlit */
      header[data-testid="stHeader"] {
        background-color: #f5f7fa !important;
      }

      /* Ocultar toolbar arriba */
      [data-testid="stToolbar"] {
        display: none !important;
      }

      /* Fondo claro */
      .stApp {
        background: #f5f7fa !important;
        color: #1a1a1a;
      }

      /* Tipografía global */
      html, body, [class*="css"], p, span, div {
        font-family: 'Lato', sans-serif !important;
        color: #1a1a1a !important;
      }
      
      h1, h2, h3, h4 {
        font-family: 'Merriweather', Georgia, serif !important;
        color: #1a1a1a !important;
      }

      /* Header simple */
      .home-header {
        margin-bottom: 3rem;
        padding: 0 1rem;
      }

      .home-name {
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        color: #1a1a1a;
        font-family: 'Merriweather', Georgia, serif;
      }

      .home-role {
        font-size: 1.1rem;
        color: #4a5568;
        margin-bottom: 1.5rem;
        font-family: 'Lato', sans-serif;
      }

      .home-links {
        display: flex;
        gap: 2rem;
        font-size: 0.875rem;
      }

      .home-links a {
        color: #718096;
        text-decoration: none;
        transition: color 0.2s;
        font-family: 'Lato', sans-serif;
      }

      .home-links a:hover {
        color: #2d3748;
      }

      /* Botón de volver */
      .stButton > button {
        background: #10b981 !important;
        border: none !important;
        color: #ffffff !important;
        font-family: 'Lato', sans-serif !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 4px rgba(16, 185, 129, 0.25) !important;
      }

      .stButton > button:hover {
        background: #059669 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(16, 185, 129, 0.35) !important;
      }

      /* Contenedor ancho */
      .block-container { max-width: 1450px; }

      /* Título principal */
      .notes-title {
        font-size: 2.5rem;
        font-weight: 900;
        margin: 0 0 2rem 0;
        color: #1a1a1a;
        font-family: 'Merriweather', Georgia, serif;
        text-align: center;
      }

      /* Sidebar de notas */
      .notes-sidebar {
        position: sticky;
        top: 70px;
        padding: 1.5rem;
        border-radius: 12px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      }

      .notes-sidebar h4{
        margin: 0 0 1rem 0;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #718096;
        font-weight: 600;
        font-family: 'Lato', sans-serif;
      }

      .notes-item{
        display:block;
        padding: 1rem;
        border-radius: 8px;
        text-decoration: none !important;
        color: #1a1a1a !important;
        font-weight: 500;
        border: 1px solid #e2e8f0;
        background: white;
        margin-bottom: 0.75rem;
        transition: all .2s ease;
        font-family: 'Lato', sans-serif;
      }

      .notes-item:hover{
        border-color: #10b981;
        background: #f7fafc;
        transform: translateY(-2px);
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.15);
      }

      .notes-item .date{
        display:block;
        margin-top: 0.5rem;
        font-size: 0.75rem;
        font-weight: 400;
        color: #718096;
      }

      .note-anchor { scroll-margin-top: 100px; }

      .note-h2{
        margin: 0 0 0.5rem 0;
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a1a;
        font-family: 'Merriweather', Georgia, serif;
      }

      .note-meta{
        margin: 0 0 1rem 0;
        font-size: 0.75rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-family: 'Lato', sans-serif;
      }

      .note-text{
        margin: 0 0 1.5rem 0;
        font-size: 1rem;
        line-height: 1.7;
        color: #1a1a1a;
        font-family: 'Lato', sans-serif;
      }

      hr {
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 2rem 0;
      }

      @media (max-width: 768px) {
        .home-name {
          font-size: 2rem;
        }
        .home-links {
          flex-direction: column;
          gap: 1rem;
        }
        .notes-title {
          font-size: 2rem;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Header (igual al resto de páginas)
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

# ============================================================
# Botón volver
# ============================================================

if st.button("← Volver"):
    st.switch_page("app.py")

# ============================================================
# Notas (placeholder)
# ============================================================

NOTAS = [
    {
        "id": "nota-01",
        "titulo": "¿Qué pasó en Jul-25?",
        "fecha": "2025-08-05",
        "texto": """
En los primeros días del mes el Gob desarmó las <strong>LEFIs ($ 15 B; instrumento que garantizaba tasa diaria a los bancos)</strong>. <strong>La medida lucía expansiva.</strong> Se esperaba que los bancos aumenten su exposición al sector privado ("trabajen de bancos"). Lo llamativo es que <strong>eso ya venía ocurriendo</strong>: el crédito al sector privado venía a toda marcha y dado el stock de depósitos había espacio para que continue en esa línea.
<br><br>
Puede argumentarse entonces que el objetivo de la medida era sacar el piso de tasa para pasar a un <strong>esquema limpio de control de agregados</strong> (M2 privado transaccional). Si ese fuese el caso, la pregunta es porque se eligió hacer una vez que terminó la baja transitoria de DEX y que JP Morgan recomendó "tomarse un respiro" de carry argentino. Si la respuesta es que el BCRA no mira el nivel de FX, <strong>no se entiende la reacción del Gob.</strong>
<br><br>
El Gob <strong>tocó todos los botones del joystick</strong> para bajarle presión al FX: vendió LECAPs, vendió futuros, licitó por fuera del calendario y la frutilla fue la lici del 29/7 donde las TEAs llegaron al 60% y el plazo promedio ponderado fue de 38 días. "<strong>Yo soy monetarista, estructuralista y todo lo que sea necesario para bajar la inflación, y si hay que recurrir a la macumba, también</strong>".
<br><br>
Aun así, el cierre de julio fue <strong>caótico</strong>. Se cerraron las posiciones de futuros y el Tesoro pagó la S31L5 (inyección de liquidez por $ 1 B -neta del aumento de encajes-). Parte de esa liquidez fue a pagar spot y llevó al TCN a $/USD 1.375.
<br><br>
<strong>¿La buena noticia?</strong> El <strong>TCRM ahora se ubica en un valor razonable.</strong> El TCRM saltó +7% en jul-25; la suba mensual más alta para un mes sin elecciones desde 2018. Este nivel está +25%(!) por encima del TCRM de 75 (100=ene-16) alcanzado en abril. Quedó demostrado que Argentina <strong>aún</strong> no tiene la oferta de dólares necesaria para <strong>flotar sin cepo</strong> a ese precio. También que el <strong>pass through</strong> con superávit primario y apertura comercial es <strong>más bajo</strong> -el TCN prom mensual subió +7,3% vs jun-25 y ninguna consultora estima un IPC > 2%-.
<br><br>
<strong>¿Se va a testear la banda superior?</strong>
<br><br>
<strong>1)</strong> Hay mejores condiciones para <strong>rearmar el carry</strong> (mayor TC y tasa). Las letras de nov tienen rendimiento asegurado en usd por el esquema de bandas.
<br><br>
<strong>2)</strong> El <strong>agro, que se había corrido como oferente del MULC,</strong> tiene ahora mayores incentivos a liquidar dada la baja de permanente de DEX y la suba del TCN. Habrá que ver que remanente de producción queda.
<br><br>
<strong>3)</strong> El BCRA cuenta con más de USD 10.000 M de <strong>poder de fuego</strong> lo que calma expectativas.
<br><br>
<strong>4)</strong> Nuevas medidas que <strong>quitan presión cambiaria</strong>: se aumentan los encajes al 40% y se flexibiliza la meta de RIN con el FMI.
<br><br>
<strong>De julio nos llevamos una certeza: la política económica responde al tipo de cambio. Los $ 25 B que vencen con el sector privado en agosto serán roleados sin importar el precio (déficit financiero) y sin importar el impacto en el resto de las tasas (actividad y morosidad).</strong>
"""
    },
    {
        "id": "nota-02",
        "titulo": "Nuevo acuerdo con el FMI",
        "fecha": "2025-03-15",
        "texto": """
<strong>¿Por qué un nuevo acuerdo?</strong>
<br><br>
Durante 2024 se utilizó (con éxito) el ancla cambiaria para bajar la inflación del 20% al 3%. Pero tuvo un costo grande y predecible; una vez que el blanqueo se quedó sin fuerza, comenzaron a faltar dólares al TCR elegido.
<br><br>
El nivel de RRII no era compatible con 1,5 M argentinos en Brasil ni con récord de importaciones de bienes de consumo. Las expectativas se desanclaron (RFX, brecha, MLC) y las RIN se vieron fuertemente golpeadas.
<br><br>
<strong>¿Cuántos USD ingresan?</strong>
<br><br>
Mucha, más de lo esperado: los desembolsos en 2025 serán de <strong>USD 23 MM</strong>. A junio ya dispondremos de USD 20 MM + cosecha = Brutas en los USD 50 MM (nada mal, no?)
<br><br>
Ahora; ¿son de libre disponibilidad? Sí. Pero buena parte lo vas a gastar en pagos de deuda externa. De acá a 2027 solo al Fondo le vas a pagar USD 12 MM; a eso hay que sumarle BOPREAL (impo y el nuevo de dividendos) y Soberanos. Por ello, el rolleo se vuelve fundamental. La salida del cepo deberá reducir el riesgo país.
<br><br>
<strong>Nuevo esquema cambiario y salida del cepo</strong>
<br><br>
El crawl no irá al 0% y el gobierno se despide de una de sus anclas; tampoco hizo falta BM=BMA o infla < 1% para salir del cepo.
<br><br>
<em>El esquema:</em> unificación a un TC flexible entre [1.000;1.400] con bandas -/+1% mensual. Cuando toque una de las bandas se intervendrá para defender el precio.
<br><br>
¿En qué zona se estabilizará? Dado que abrirá a $1.070 y el CCL cerró en los $1.350, de arranque podrá testear los $1.300. Al no liberarse los stocks a empresas (razonable) se evita un overshooting; cuando se sitúe en los $1.300 los exportadores tendrán incentivos a liquidar (es una mejora del 15%) presionando hacia la baja. La TPM debería subir para subir los incentivos y resintalar el carry.
<br><br>
¿Será un valor estable? Si el BCRA no interviene entre bandas deberíamos ver bastante volatilidad del TC respondiendo a los shock externos (Trump) y dolarización de carteras previo elecciones. <strong>Para eso es la flexibilidad del TC.</strong>
<br><br>
<strong>¿Cuánta competitividad se gana?</strong>
<br><br>
Si el TCN se va $1.400, el TCR subiría +30% (+5% del nivel de salida de cepo -ene-16-). ¿Es suficiente? Difícil saberlo, pero es una mejora. El problema está en que las bandas se ajustan de forma mensual al 1% con una inflación superior ¿deja vú?
<br><br>
A nov-25 estaríamos en el mismo nivel de TCRM. De hecho, si el TC se establece en la banda superior; en términos de TCRM, hubiese sido lo mismo devaluar un +30% y mantener el crawling al 1%. Por ello, <strong>es fundamental que se avance en las reformas tributarias y laborales</strong> (mejora de competitividad por baja de precios en moneda local).
<br><br>
<strong>Metas a cumplir</strong>
<br><br>
<em>Fiscal:</em> FMI exige 1,3% sup prim en 2025 y el Gobierno proyecta 1,6% (en año electoral -aplausos-).
<br><br>
<em>Monetario:</em> la meta cuantitativa exige 0 transferencias al Tesoro y sucederá. El informe explica que se abandona el BMA=$47,7bn para pasar a monitorear trimestralmente el M2.
<br><br>
<em>Cambiaria:</em> se debe finalizar el año con aprox RIN de USD 4.000 M (hoy en < -6.000). Por ello esperamos que el BCRA compre aún dentro de la banda (tirando el precio para arriba).
<br><br>
<em>AIF:</em> AIF = BM - RIN. Se incluye también una meta indicativa de $ máximos sin respaldo.
<br><br>
<strong>Impactos en activos</strong>
<br><br>
• RFX ABR-25 cerró a $1.190; tiene espacio para subir; $1.320 será momento para vender.
<br>
• Merval: la salida del cepo (sorpresiva) + la visita Bessent = recorrido al alza.
<br>
• Lo mismo para Soberanos. Pero todo condicional a Trump.
<br>
• CER debería ser ganador.
<br><br>
<strong>Impactos en precios y actividad</strong>
<br><br>
El FMI se muestra sumamente optimista: PBI +5,5% y IPC [18%-23%]. No obstante, el salto devaluatorio tendrá sus consecuencias:
<br><br>
<em>Precios:</em> el IPC de marzo (3,7%) ya deja arrastre y si TCN se va a $1.200 es un salto de +12%. Abril podría ir al 6/7% (veremos si la baja del petróleo compensa). Si Abril cierra en 6% ya acumularemos 15%; es decir para finalizar en 23%; el prom mensual debería ir en el 0,8% el resto del año... Creo que el IPC cerrará 2025 en 35%-40% (nada mal).
<br><br>
<em>Actividad:</em> más difícil de pronosticar. Sabemos que 2024 dejó buen arrastre (+3pp) y datos de ene/feb sorprendieron positivamente. Ahora; ¿cuál será el impacto del nuevo esquema (lease, devaluación)? La caída del consumo (70% del PBI) dado el impacto en el salario real será parcialmente compensada por mejora de las exportaciones netas. El resultado neto dependerá del grado de traslado a precios.
<br><br>
<strong>Mi opinión: todo costo será temporal y valdrá la pena.</strong>
<br><br>
<strong>¿Cómo es el nuevo cronograma de pagos?</strong>
<br><br>
En una 2da presidencia de Milei, solo con el FMI deberemos pagar por año aprox USD 9 MM. Será fundamental el desarrollo de Vaca Muerta y el acceso a los mercados internacionales; sino nos espera un nuevo EFF…
"""
    },
    {
        "id": "nota-03",
        "titulo": "¿Dólar atrasado o precios adelantados?",
        "fecha": "2025-02-10",
        "texto": """
<strong>Un aporte desde el lado productivo</strong>
<br><br>
Los precios en dólares, como todo ratio, se componen de un numerador (valor en pesos) y un denominador (tipo de cambio). Si Argentina está cara en dólares puede deberse a 2 opciones: <strong>i)</strong> el valor en pesos está por encima de lo que debería: adelantado; <strong>ii)</strong> el tipo de cambio (TC) está por debajo: atrasado.
<br><br>
<strong>¿Cuál está ocurriendo?</strong>
<br><br>
Veamos, el numerador (valor en pesos), determinado por la oferta y la demanda, enfrenta en Argentina múltiples distorsiones: una presión tributaria exorbitante, una baja calidad de la infraestructura y de las instituciones laborales, altos costos de comercialización y un nulo acceso al crédito. Manteniendo todo lo demás constante, cualquier desventaja en estos aspectos encarece en dólares al país. La salida rápida de abrir la economía parece no tener resultado: en el último año se facilitaron las importaciones y aún así los precios en dólares se elevaron.
<br><br>
Allí es donde aparece el denominador (tipo de cambio): el TC corrige esas deficiencias y nivela condiciones de producción entre países. A suerte de <em>second best</em>, el tipo de cambio actúa como paliativo de los déficits estructurales. No es casualidad que: <strong>i)</strong> Balassa-Samuelson demostraron la relación negativa entre tipo de cambio real y nivel de desarrollo económico; <strong>ii)</strong> el propio modelo TNT muestra que la productividad más alta en el sector NT de los desarrollados aprecia su TC (vía salario).
<br><br>
No obstante, la política cambiaria no hace magia: ningún nivel de tipo de cambio hará que Argentina sea competitiva en todos los rubros, tampoco sería deseable. Pero se debe entender que este atraso autogenerado impacta hasta en los sectores más productivos. En el límite, ninguna ventaja comparativa salva por sí sola a un sector, y sino revísese la situación actual del agro. A su vez, la apreciación impide la diversificación de las exportaciones: si usted cree que dadas las capacidades de nuestro suelo, la canasta exportadora debe ser primaria en su totalidad, revise que ocurre con nuestra macroeconomía en los años de sequía.
<br><br>
Si aún no están dadas las condiciones para reducir el numerador (escenario ideal), el TC debería reflejarlo. Ergo, el problema está en el denominador. De hecho, los recortes en educación y en obra pública, sumados al escenario de guerra de aranceles y al fortalecimiento del dólar, elevan el TC de equilibrio. Esta nota no aboga por "salarios africanos" pero tampoco por un tipo de cambio atrasado artificialmente vía controles cambiarios, blend e intervención; una estrategia tan efectiva para reducir la inflación como para generar desempleo y estallar una vez que no puede ser más financiada. <strong>El tipo de cambio debe ser determinado por el mercado y debe reflejar, de manera inversa y genuina, la competitividad de la economía argentina.</strong>
"""
    },
    {
        "id": "nota-04",
        "titulo": "📊 Nota 4 — Inflación núcleo vs estacionales",
        "fecha": "2026-01-15",
        "texto": "Ejemplo: una nota corta sobre dinámica de inflación núcleo, regulados y estacionales."
    },
]


# Layout (izquierda un toque más grande como pediste)
left, right = st.columns([1.5, 4], gap="large")

with left:
    items = []
    for n in NOTAS:
        items.append(
            f'<a class="notes-item" href="#{n["id"]}">{n["titulo"]}<span class="date">{n["fecha"]}</span></a>'
        )

    sidebar_html = (
        '<div class="notes-sidebar">'
        '<h4>Índice</h4>'
        + "".join(items) +
        "</div>"
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)

with right:
    for i, n in enumerate(NOTAS):
        st.markdown(
            textwrap.dedent(f"""
            <div id="{n['id']}" class="note-anchor">
              <div class="note-h2">{n['titulo']}</div>
              <div class="note-meta">{n['fecha']}</div>
              <div class="note-text">{n['texto']}</div>
            </div>
            """).strip(),
            unsafe_allow_html=True,
        )
        if i < len(NOTAS) - 1:
            st.markdown("<hr/>", unsafe_allow_html=True)
