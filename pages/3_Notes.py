# pages/3_Notes.py
import streamlit as st
import textwrap

st.set_page_config(
    page_title="Artículos Macro",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CSS - LIGHT THEME + Merriweather/Latof
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
            top: 20px;
            padding: 1.5rem;
            border-radius: 12px;
            background: #e2e8f0  !important;  /* ← ANTES era #ffffff */
            border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
          }

      .notes-sidebar h4 {
        margin: 0 0 1rem 0;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #a0aec0 !important;  /* ← más claro para que se lea sobre oscuro */
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
        text-align: justify;
      }


    .note-image {
      margin: 2rem 0;
      text-align: center;    ← esto NO centra imágenes cuando usás Streamlit
    }

      .note-image img {
        max-width: 50%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
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
# Header
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

if st.button("← Volver"):
    st.switch_page("app.py")

# ============================================================
# NOTAS
# ============================================================

NOTAS = [
{
    "id": "nota-06",
    "titulo": "EMAE en máximos y recaudación en mínimos",
    "fecha": "2026-03-28",
    "tipo": "externo",
    "url": "https://eleconomista.com.ar/economia/la-economia-maximos-recaudacion-minimos-n93676",
    "imagen": "https://raw.githubusercontent.com/ffernandez-1999/Personal-Project/main/data/link_elecon.png",
},
{
    "id": "nota-05",
    "titulo": "El ancla fiscal en 2026",
    "fecha": "2026-03-08",
    "texto_parte1": """
<strong>El ancla fiscal</strong>
<br><br>
El ordenamiento de las cuentas públicas se consolidó como el principal ancla del programa macroeconómico. No quedó en lo discursivo sino que el Gobierno implementó un inaudito ajuste real del gasto cercano al <strong>-30% respecto de 2023</strong>. El recorte fue generalizado: <strong>Obra Pública cayó cerca de -80% real</strong>, mientras que <strong>Subsidios Económicos y Transferencias a Provincias retrocedieron más de -50%</strong>. La única excepción fue la <strong>AUH</strong>, con una expansión real cercana al <strong>+70%</strong>.
<br><br>
Como resultado, el sector público pasó de registrar un <strong>déficit primario de -3,5% del PIB en 2023</strong> a un <strong>superávit primario cercano a +1,5% del PIB en 2024-2025</strong>. Esta corrección permitió reducir la inflación mensual desde niveles superiores al <strong>10% en el segundo semestre de 2023</strong> a aproximadamente <strong>2,5% promedio mensual en 2025</strong>, mientras que el <strong>riesgo país</strong> cayó desde <strong>2.500 pb hacia la zona de 500 pb</strong>.
<br><br>
<strong>Dinámica de la recaudación</strong>
<br><br>
En 2024 la recaudación tributaria cayó cerca de <strong>-6% real</strong>, reflejando el impacto inicial del proceso de estabilización sobre el nivel de actividad. Las bajas de <strong>IVA DGI, Ganancias DGI y Seguridad Social</strong> fueron parcialmente compensadas por mayores ingresos asociados a <strong>Derechos de Exportación</strong> (+30%; base de comparación de sequía), el incremento de la alícuota del <strong>Impuesto PAIS de 7,5% a 17,5%</strong> y recursos extraordinarios vinculados al <strong>blanqueo, bienes personales y la moratoria</strong>.
<br><br>
Durante 2025 la recuperación de la actividad permitió recomponer parcialmente los tributos vinculados al mercado interno y habilitó una <strong>reducción de impuestos cercana a 2% del PIB</strong>, incluyendo la eliminación del <strong>Impuesto PAIS</strong>, la reducción de <strong>Derechos de Exportación</strong> y la baja de <strong>aranceles a importaciones</strong>.
<br><br>
En 2026, sin embargo, la recaudación muestra señales de debilitamiento. Los ingresos acumulan <strong>siete meses consecutivos de caída interanual</strong> y el primer bimestre registró el nivel real más bajo desde 2009 —similar al de 2024—. El deterioro se concentra en los tributos vinculados al comercio exterior (menores DEX por baja de alícuotas —soja de <strong>33% a 24%</strong> y trigo y maíz de <strong>12,5% a 9%</strong>— y por el adelantamiento de exportaciones en sep-25), mientras que el <strong>Impuesto a los Combustibles</strong> cumple un rol compensador. Tal es así que, por primera vez desde 2017, lo recaudado por Combustibles supera a lo recaudado por DEX.
""",
    "imagen1": "data/5.jpg",
    "imagen1_titulo": "Recaudación Nacional (B de $ de feb-26; promedio móvil 3 meses)",
    "texto_parte2": """
<strong>Margen fiscal y outlook</strong>
<br><br>
Dada la caída de los ingresos tributarios, el resultado fiscal de ene-26 muestra menor robustez al registrado en años anteriores. Si bien el resultado es similar al de ene-25, cuando se elimina el ingreso por la privatización de <strong>Centrales Hidroeléctricas ($ 1 B)</strong>, el superávit pasa a ser <strong>-35% menor</strong> (y <strong>-60% menor al de 2024</strong>). De igual modo, el superávit financiero de <strong>$ 1 B</strong> hubiese sido prácticamente nulo.
<br><br>
¿Se puede seguir bajando impuestos en este contexto? Si el objetivo es respetar el equilibrio financiero (esto es, un superávit primario lo suficientemente elevado como para financiar los intereses de la deuda pública), el margen disponible es simplemente el superávit financiero proyectado para 2026: alrededor de <strong>0,3% del PIB ($ 3 B)</strong>. Es decir, el margen es tan bajo que no alcanza a financiar ni dos meses de recaudación del <strong>Impuesto al Cheque</strong>. En este contexto, la baja de impuestos depende necesariamente de nuevas fuentes de financiamiento.
<br><br>
Las partidas que podrían ser recortadas son las no indexadas por IPC, por lo que se descartan Jubilaciones y Pensiones, la AUH y otras prestaciones sociales. También se descarta un nuevo recorte en Transferencias a Universidades, dado que su costo político no justifica su costo fiscal. En consecuencia, las partidas potencialmente ajustables se concentran en Obra Pública, Transferencias a Provincias, Subsidios Económicos y Gastos de Funcionamiento (masa salarial pública y déficit operativo de empresas). El problema es que estas ya han sido fuertemente recortadas: la suma de las mismas pasó de representar 8% del PIB en 2023 a aproximadamente 4% del PIB en la actualidad. De hecho, Obra Pública, Subsidios y Transferencias a Provincias se encuentran en mínimos históricos, lo que limita el margen de ajuste adicional. Por ende, el único espacio potencial aparece en Gastos de Funcionamiento, donde podría existir cierto margen para reducir la partida desde aproximadamente 2,5% del PIB hacia niveles cercanos a 2% del PIB, aunque incluso ese ajuste tendría un impacto fiscal acotado.
<br><br>
En este contexto, el frente externo podría aportar cierto alivio. La escalada del conflicto en Oriente Medio presiona al alza los <strong>precios internacionales de las commodities</strong>: mayores precios implican <strong>mayores bases imponibles para Derechos de Exportación</strong>. A su vez, el avance de la <strong>reforma laboral</strong> podría mejorar gradualmente la formalización del empleo y ampliar la base contributiva, fortaleciendo la recaudación de <strong>Seguridad Social</strong>. Finalmente, el programa de <strong>privatizaciones</strong> también podría aportar recursos extraordinarios. Como referencia, la eventual privatización de <strong>AySA</strong> podría generar ingresos cercanos a <strong>$ 0,7 B</strong>, contribuyendo a ampliar el margen fiscal en el corto plazo.
""",
    },
    {

        "id": "nota-01",
        "titulo": "¿Qué pasó en Jul-25?",
        "fecha": "2025-08-05",
        "texto": """
En los primeros días del mes el Gob desarmó las <strong>LEFIs ($ 15 B; instrumento que garantizaba tasa diaria a los bancos)</strong>. <strong>La medida lucía expansiva.</strong> Se esperaba que los bancos aumenten su exposición al sector privado ("trabajen de bancos"). Lo llamativo es que <strong>eso ya venía ocurriendo</strong>: el crédito al sector privado venía a toda marcha y dado el stock de depósitos había espacio para que continue en esa línea.
<br><br>
Puede argumentarse entonces que el objetivo de la medida era sacar el piso de tasa para pasar a un <strong>esquema limpio de control de agregados</strong> (M2 privado transaccional). Si ese fuese el caso, la pregunta es porque se eligió hacer una vez que terminó la baja transitoria de DEX y que JP Morgan recomendó "tomarse un respiro" de carry argentino.
<br><br>
El Gob <strong>tocó todos los botones del joystick</strong> para bajarle presión al FX: vendió LECAPs, vendió futuros, licitó por fuera del calendario y la frutilla fue la lici del 29/7 donde las TEAs llegaron al 60% y el plazo promedio ponderado fue de 38 días. "<strong>Yo soy monetarista, estructuralista y todo lo que sea necesario para bajar la inflación, y si hay que recurrir a la macumba, también</strong>".
<br><br>
Aun así, el cierre de julio fue <strong>caótico</strong>. Se cerraron las posiciones de futuros y el Tesoro pagó la S31L5 (inyección de liquidez por $ 1 B -neta del aumento de encajes-). Parte de esa liquidez fue a pagar spot y llevó al TCN a $/USD 1.375.
<br><br>
<strong>¿La buena noticia?</strong> El <strong>TCRM ahora se ubica en un valor más alto.</strong> El TCRM saltó +7% en jul-25; la suba mensual más alta para un mes sin elecciones desde 2018. Este nivel está +25%(!) por encima del TCRM de 75 (100=ene-16) alcanzado en abril. Parece que Argentina <strong>aún</strong> no tiene la oferta de dólares necesaria para <strong>flotar sin cepo</strong> a ese precio. Y también que el <strong>pass through</strong> con superávit primario y apertura comercial es <strong>más bajo</strong> -el TCN prom mensual subió +7,3% vs jun-25 y ninguna consultora estima un IPC > 2%-.
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
<strong>La política económica de julio adelanta que los $ 25 B que vencen con el sector privado en agosto serán roleados sin importar el precio (déficit financiero) y sin importar el impacto en el resto de las tasas (actividad y morosidad).</strong>
"""
    },
    {
        "id": "nota-02",
        "titulo": "Nuevo acuerdo con el FMI",
        "fecha": "2025-03-15",
        "texto": """
<strong>¿Por qué un nuevo acuerdo?</strong>
<br><br>
Durante 2024 se utilizó con éxito el ancla cambiaria para bajar la inflación del 20% al 3%. La medida no estuvo exenta de costos: una vez que el blanqueo se quedó sin dinamismo, comenzaron a faltar dólares al TCR elegido.
El nivel de RRII no era compatible con 1,5 M argentinos en Brasil ni con récord de importaciones de bienes de consumo. Las expectativas se desanclaron (RFX, brecha, MLC) y las RIN se vieron fuertemente golpeadas.
<br><br>
<strong>¿Cuántos USD ingresan?</strong>
<br><br>
Más de lo esperado: los desembolsos en 2025 serán de <strong>USD 23 MM</strong>. A junio ya dispondremos de USD 20 MM + cosecha = ¿brutas en USD 50 MM?
Ahora, la pregunta es: ¿son de libre disponibilidad? Sí. Pero buena parte se irá en pagos de deuda externa. De acá a 2027 se le deberá devolver al Fondo USD 12 MM; a eso hay que sumarle BOPREAL (importaciones y la nueva especie de dividendos) y Soberanos (USD 8 MM por año). Por ello, el acceso a los mercados internacionales se vuelve fundamental (¿la salida del cepo colaborará a la baja del riegso país?)
<br><br>
<strong>Nuevo esquema cambiario y salida del cepo</strong>
<br><br>
(El crawl finalmente no irá al 0% y el gobierno se despide de una de sus anclas; tampoco hizo falta BM=BMA o infla < 1% para salir del cepo).
<br><br>
<em>El esquema:</em> unificación a un TC flexible entre [1.000;1.400] con bandas -/+1% mensual. Cuando toque una de las bandas se intervendrá para defender el precio: en el piso se compran dólares (venden pesos) y en el techo se venden (compran).
<br><br>
¿En qué zona se estabilizará? Dado que el TCN abrirá a $1.070 y el CCL cerró en los $1.350, de arranque podrá testear los $1.300. Al no liberarse los stocks a empresas (razonable) se evita un overshooting; cuando se sitúe en los $1.300 los exportadores tendrán incentivos a liquidar (es una mejora del 15% en su competitividad) presionando hacia la baja el TC. La TPM debería subir para resintalar el carry.
¿Será un valor estable? Si el BCRA no interviene entre bandas deberíamos ver bastante volatilidad del TC respondiendo a los shock externos (Trump) y dolarización de carteras previo elecciones. <strong>Para eso es la flexibilidad del TC.</strong>
<br><br>
<strong>¿Cuánta competitividad se gana?</strong>
<br><br>
Si el TCN se va $1.400, el TCR subiría +30% (+5% del nivel de salida de cepo -ene-16-). ¿Es suficiente? Difícil saberlo, pero es una mejora. El problema está en que las bandas se ajustan de forma mensual al 1% con una inflación superior.
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
• RFX ABR-25 cerró a $1.190; tiene espacio para subir; ¿$1.320 será momento para vender?
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
"""
    },
    {
        "id": "nota-04",
        "titulo": "Nueva meta fiscal con el Fondo - 2024",
        "fecha": "2024-02-05",
        "texto_parte1": """
El 31Ene24 se recibió un desembolso por <strong>USD 4.700 M</strong>, USD 3.300 M fueron en concepto de la cuota demorada por el Fondo en Nov23 y USD 1.300 M en concepto de adelantos de desembolsos de este año. La contrapartida del acuerdo fue el compromiso por parte de LLA de alcanzar metas sin precedentes; <strong>i)</strong> un superávit primario de 2% del PBI para conseguir equilibrio financiero; <strong>ii)</strong> el nulo financiamiento monetario al Tesoro (ampliando el concepto y volviéndolo más genuino); <strong>iii)</strong> una recuperación de las RRII netas de USD 10.000 M (vs el stock del 13Dic23).
<br><br>
Para conseguir el superávit primario de 2%, Economía estimó que se necesitará un <strong>ajuste fiscal de 5,2%</strong> vía una tabla publicada en Twitter - ajuste de una magnitud nunca vista en la historia argentina -. La misma tabla presenta un camino mixto entre suba de impuestos y baja del gasto para conseguir el objetivo fiscal. Sin embargo, la estimación incorpora algunos puntos a revisar:
<br><br>
<strong>i)</strong> El déficit financiero terminó siendo mayor al esperado pero la inercia de este resultado será menor para 2024, por lo que la meta se vuelve levemente más accesible;
<br><br>
<strong>ii)</strong> La retirada del capítulo fiscal de la Ley Ómnibus obliga al Tesoro a usar su creatividad para conseguir otras vías de aprobación o medidas fiscales alternativas;
<br><br>
<strong>iii)</strong> La estimación no incorpora la caída de la recaudación como consecuencia de la recesión;
<br><br>
<strong>iv)</strong> La hoja de ruta fiscal de las metas nominales no tiene en cuenta la estacionalidad del resultado primario.
<br><br>
<strong>¿Cuál es la herencia de déficit financiero que recibe LLA?</strong>
<br><br>
Según los datos del MECON-IMG, el 2023 cerró con un déficit fiscal de -2,7% y un déficit financiero de -5,9% del producto en vez del -5,2% estimado. Lo que elevaría en +0,7pp la necesidad de ajuste para conseguir el equilibrio financiero. Sin embargo, para medir el ajuste necesario se requiere observar la inercia del déficit financiero de 2023 para 2024 y no simplemente su resultado. Hay dos operaciones extraordinarias que hacen diferir el resultado financiero de su inercia para 2024.
<br><br>
<em>Ajustes extraordinarios:</em>
<br><br>
<strong>i)</strong> Se deben descontar los ingresos recibidos en Nov23 por la licitación de las bandas de frecuencia 5G ($319.000 M; 0,2% PBI) ya que no forman parte de la naturaleza de la estructura tributaria. De esta forma, caen los ingresos recibidos y el déficit financiero cierra en -6,1% (el ajuste extra necesario se amplía entonces de +0,7pp a +0,9pp).
<br><br>
<strong>ii)</strong> El pago de intereses explotó en Dic23 ($ 3.300.000 M; 1,8% del PBI vs 0,1% promedio 2023) debido a la inclusión de la recompra de deuda del Tesoro al BCRA por 1,5% del PBI. Esto tampoco responde a la verdadera estructura fiscal así que debe ser descontado. En consecuencia, el ajuste requerido cae al -4,6% en vez del -5,0% primeramente estimado.
<br><br>
<strong>Retirada del capítulo fiscal de la Ley Ómnibus</strong>
<br><br>
Dentro de la hoja de ruta fiscal mostrada tanto por el FMI como por el MECON, se estimaba una suba de los ingresos de 2,2% del PBI. El 65% de esa suba dependía de la aprobación del capítulo fiscal por parte del Congreso (suba de DEX -que aportaría 0,5% del PBI-, reversión Ganancias -0,4%- y Moratoria, bienes personales y blanqueo -0,5%-). Asimismo, en la ley se incorporaba el cambio de la fórmula de movilidad de jubilaciones, que habría otorgado 0,4% del producto de recorte en el gasto. Dado que el capítulo fue retirado, Economía perdió -1,8% del PBI de ajuste estimado. Si a esto se le netea la inercia más baja del déficit financiero, deberá buscar un recorte de -6,4% del producto (mayor en +1,4pp al estimado).
<br><br>
<strong>Impacto de la recesión en la recaudación</strong>
<br><br>
Según el Fondo, la actividad económica caerá -2,8% en 2024, una recesión anual no vista desde 2009 (-5,9%; exceptuando 2020). Si se excluye al agro, la caída sería de -5,8%. El informe menciona al proceso de ajuste de precios relativos y al proceso de consolidación fiscal como los principales drivers de la baja de la actividad. Los datos con los que se cuentan hasta ahora son más que ilustrativos. Luego de los primeros ajustes de precios (tipo de cambio, combustibles, prepagas) el IPC registró una suba mensual de +25,5% en Dic23 y en Ene24 se espera algo cerca de +22% (el IPC CABA dio 21,7%-). A su vez, el salario RIPTE creció tan solo +8,3% en Dic23, lo que significa una pérdida de compra real de -13,7%.
<br><br>
Esta baja del salario real tuvo su contraparte en el consumo: la recaudación por IVA DGI de Dic23 y Ene24 mostró un descenso real de -6,7% y -15,9% anual (usando IPC CABA). Si la dinámica de pérdida de salario real, baja del consumo y baja de la recaudación se mantiene a lo largo del año, el ajuste de -6,4% del PBI se quedará corto (además la caída de la demanda tendrá su efecto de segunda ronda en la oferta -derechos de importación, seguridad social, ganancias-). A modo clarificador, en la siguiente tabla se muestra cómo cayó la recaudación en todos los últimos años de recesión:
""",
        "imagen1": "data/1.jpg",
        "texto_parte2": """
En Ene24, las bajas en los tributos relacionados con el mercado interno fueron compensadas por lo recaudado por el impuesto país (+278,5% i.a. real) y por los derechos de exportación (177,3%). De este modo, la recaudación total cayó -4,9% anual. ¿Qué sucede si esta dinámica se repite a lo largo del año? Una baja real de -5% de la recaudación (escenario optimista) significa una baja de los ingresos/producto de -0,4pp, por lo que el ajuste necesario pasa de -6,4% a -6,8% del PBI y el recorte adicional de -1,4pp a -1,8pp (en un escenario pesimista, donde la recaudación cae -10% real, los ingresos/productos bajan -1,2pp). No obstante, la suba de los impuestos a los combustibles se estima que dará recursos adicionales por +0,5% del PBI. Por lo que el bache a compensar queda en torno a los -1,3pp.
<br><br>
Ese bache se cubriría achicando aún más el gasto público: <strong>el ajuste requerido desde el lado del gasto pasa del -3% estimado por el MECON al 5% del PBI</strong>, (con especial foco en subsidios, transferencias a provincias y empresas públicas y obra pública). La relación ajuste ingresos-gastos pasa de 40/60 a 20/80. Para cumplir con este camino, el Tesoro cuenta con un as bajo la manga: dado que no hay presupuesto para 2024, varias partidas se ejecutarán bajo la nominalidad de 2023.
""",
        "imagen2": "data/2.jpg",
        "texto_parte3": """
El Tesoro necesitará que, como ocurrió en Ene24, la baja de la recaudación por merma de la actividad sea compensada de manera significativa por los tributos relacionados con el comercio exterior. Para ello se requiere; <strong>i)</strong> desde el lado de los DEX, que el TCRM se mantenga en niveles atractivos (y que llueva); <strong>ii)</strong> desde el lado del impuesto país que la actividad no caiga para sostener la base imponible. El primer supuesto parece no estar asegurado dada la política cambiaria del BCRA. Si bien la devaluación de Dic23 colocó al TCRM en niveles no vistos desde comienzos de siglo, el crawling peg de 2% acompañado de una inflación promedio de 20% mensual tiene como resultado una constante pérdida de competitividad. Al 30Abr24 se habría perdido un -46% de la ganancia de la devaluación, lo que afectaría los incentivos a liquidar exportaciones golpeando a la recaudación. Por ello, luce inevitable una nueva devaluación/aceleración del crawling peg o nuevas versiones de dólar soja.
<br><br>
<strong>GRÁFICO TCRM ($800=13/12/23)</strong>
""",
        "imagen3": "data/3.jpg",
        "texto_parte4": """
<strong>Estacionalidad del déficit</strong>
<br><br>
Las metas trimestrales publicadas por el Fondo llegan hasta Sep24. Para ese entonces el Tesoro debería contar con un superávit fiscal nominal de $2.887.300 M. El número es muy bajo en relación al 2% de superávit exigido para el año y al PBI implícito por los pronósticos publicados en el informe. Veamos, el Fondo espera una recesión real de -2,8% y un deflactor del PBI de 253,1% = un producto nominal estimado de $660.000.000 M para 2024. Es decir, la meta nominal de Sep24 implica acumular un superávit primario de +0,4% del PBI en los primeros tres trimestres. Y el +1,6% restante (80% de la meta; $10.290.000 M) se debería acumular en el último trimestre. Sin embargo, <strong>el último trimestre es estacionalmente deficitario por lo que esta hoja de ruta fiscal no tiene asidero.</strong>
<br><br>
Suena más lógico que las metas nominales hayan sido expresadas en relación al PBI de 2023 ($192.000.000 M; se obtiene de las mismas estimaciones del informe) y se irán ajustando a medida que se conozcan los datos de precios y actividad (esto no sucedió el año pasado cuando las metas fiscales de 2023 fueron planteadas en relación al PBI pronosticado para ese año). Esta nueva manera de expresar los datos conlleva el problema de que se vuelve más complejo monitorear el cumplimiento de las metas ya que no habrá relación directa con el resultado del IMIG.
<br><br>
De esta forma, la hoja de ruta fiscal entonces sería lineal. Se repartiría el ajuste en partes iguales en cada trimestre (0,5% del PBI), lo que implica que para Sep24 (primeros tres trimestres) el Tesoro tendría que presentar un superávit de 1,5% del producto. No obstante, no es conveniente exigir de la misma manera en el último trimestre ya que es estacionalmente deficitario. Tendría más sentido elevar el ajuste en los trimestres anteriores y dejar algo de margen para los últimos 3 meses del año (la estacionalidad si se tomó en cuenta para la meta de RRII netas, la acumulación fuerte se exige en el primer semestre del año cuando las liquidaciones del agro son altas).
<br><br>
<strong>En el último trimestre del año se acumula en promedio el 60% del déficit fiscal total del año.</strong>
""",
        "imagen4": "data/4.jpg"
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
        # Nota 04 tiene estructura especial con imágenes
        if n["id"] == "nota-04":
            st.markdown(
                f"""
                <div id="{n['id']}" class="note-anchor">
                  <div class="note-h2">{n['titulo']}</div>
                  <div class="note-meta">{n['fecha']}</div>
                  <div class="note-text">{n['texto_parte1']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown('<div class="note-image">', unsafe_allow_html=True)
            st.image(n["imagen1"], output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="note-text">{n["texto_parte2"]}</div>', unsafe_allow_html=True)
            st.markdown('<div class="note-image">', unsafe_allow_html=True)
            st.image(n["imagen2"], output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="note-text">{n["texto_parte3"]}</div>', unsafe_allow_html=True)
            st.markdown('<div class="note-image">', unsafe_allow_html=True)
            st.image(n["imagen1"], output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="note-text">{n["texto_parte4"]}</div>', unsafe_allow_html=True)
            st.markdown('<div class="note-image">', unsafe_allow_html=True)
            st.image(n["imagen1"], output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)

        elif n["id"] == "nota-05":
            st.markdown(
                f"""
                <div id="{n['id']}" class="note-anchor">
                  <div class="note-h2">{n['titulo']}</div>
                  <div class="note-meta">{n['fecha']}</div>
                  <div class="note-text">{n['texto_parte1']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div style="text-align:center;font-size:0.85rem;font-weight:600;'
                f'text-decoration:underline;color:#4a5568;margin-bottom:0.5rem;">'
                f'{n["imagen1_titulo"]}</div>',
                unsafe_allow_html=True,
            )
            st.image(n["imagen1"], output_format="PNG")
            st.markdown(
                f'<div class="note-text">{n["texto_parte2"]}</div>',
                unsafe_allow_html=True,
            )
            if i < len(NOTAS) - 1:
                st.markdown(
                    '<div style="height:1px;background:#e2e8f0;margin:2rem 0;"></div>',
                    unsafe_allow_html=True,
                )

        elif n["id"] == "nota-06":
            import base64, os
            img_path = os.path.join(os.path.dirname(__file__), "..", "data", "link_elecon.png")
            with open(img_path, "rb") as f:
                img_b64 = base64.b64encode(f.read()).decode()
            st.markdown(
                f"""
                <div id="{n['id']}" class="note-anchor">
                  <div class="note-h2">{n['titulo']}</div>
                  <div class="note-meta">{n['fecha']}</div>
                  <a href="{n['url']}" target="_blank" style="text-decoration:none;display:block;max-width:480px;">
                    <div style="border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;cursor:pointer;">
                      <img src="data:image/png;base64,{img_b64}" style="width:100%;display:block;" />
                      <div style="padding:0.75rem 1rem;border-top:1px solid #f0f0f0;background:white;">
                        <div style="font-size:0.75rem;color:#a0aec0;margin-bottom:4px;">eleconomista.com.ar · 28 mar 2026 ↗</div>
                        <div style="font-size:0.95rem;font-weight:600;color:#1a1a1a;line-height:1.4;">La economía en máximos y la recaudación en mínimos</div>
                      </div>
                    </div>
                  </a>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if i < len(NOTAS) - 1:
                st.markdown(
                    '<div style="height:1px;background:#e2e8f0;margin:2rem 0;"></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                textwrap.dedent(f"""
                <div id="{n['id']}" class="note-anchor">
                  <div class="note-h2">{n['titulo']}</div>
                  <div class="note-meta">{n['fecha']}</div>
                  <div class="note-text">{n['texto']}</div>
                </div>
                """),
                unsafe_allow_html=True,
            )
            if i < len(NOTAS) - 1:
                st.markdown(
                    '<div style="height:1px;background:#e2e8f0;margin:2rem 0;"></div>',
                    unsafe_allow_html=True,
                )
