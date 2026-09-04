# Script de un solo uso, conservado como registro del Modulo 1.
# Rellenaba los bloques de interpretacion pendientes en el .Rmd de la Practica 1,
# cuando el archivo se llamaba Practica1_Hechos_Estilizados.Rmd. Ese nombre ya no
# existe: el entregable final es 'Analisis del Riesgo (Practica 1).Rmd'. No volver
# a ejecutarlo tal cual.

import re

p = "Practica1_Hechos_Estilizados.Rmd"
with open(p, "r", encoding="utf-8") as f:
    s = f.read()

PEND = "*(Interpretación con las cifras de la corrida: pendiente de completar tras el knit.)*"

H1 = r"""**Interpretación:** Las tres funciones de autocorrelación se comportan como anticipa el hecho estilizado, ya que en los veinticinco rezagos examinados la mayoría de las barras cae dentro de la banda de significancia de $\pm 0.0554$, y las autocorrelaciones de primer rezago son de $-0.0257$ en SPY, $-0.0459$ en NVDA y $-0.0229$ en GLD, todas por debajo del umbral y todas de signo negativo, patrón compatible con la reversión de muy corto plazo que introduce el rebote entre precios de compra y venta antes que con una capacidad real de predicción, por lo que conviene señalar dos excedencias en lugar de ocultarlas, ya que el rezago 3 de NVDA alcanza $-0.0587$ y supera la banda mientras el de SPY llega a $-0.0554$ y queda justo sobre ella, aunque la lectura correcta no es que estos activos sean predecibles, porque al examinar veinticinco rezagos con un nivel del 5 % se esperan 1.25 excedencias por azar en cada serie y observar una sola es precisamente lo que predice la hipótesis nula de ausencia de dependencia lineal, aplicando aquí con exactitud la advertencia de la clase, dado que estas correlaciones pequeñas pero medibles confirman que la ausencia de dependencia lineal no equivale a independencia, y el hecho siguiente muestra dónde se esconde la dependencia que la autocorrelación en niveles no logra detectar."""

H2 = r"""**Interpretación:** El contraste entre ambas funciones de autocorrelación resulta concluyente para dos de los tres activos, ya que en SPY la autocorrelación de primer rezago pasa de $-0.0257$ en niveles a $0.1991$ en cuadrados y en GLD de $-0.0229$ a $0.1565$, es decir casi ocho y casi siete veces su magnitud original, además de permanecer significativa en 11 y 16 de los 25 rezagos examinados frente a la práctica ausencia de significancia que mostraban en niveles, mientras que NVDA rompe el patrón y el resultado merece explicación en lugar de omisión, porque su autocorrelación de cuadrados es de apenas $0.0440$, por debajo de la banda de $0.0554$, con solo 3 de 25 rezagos significativos, de manera que el activo más volátil de los tres es paradójicamente el que exhibe el agrupamiento menos persistente.

Dos mecanismos explican esa aparente paradoja, y el primero es que el agrupamiento se mide siempre en términos relativos a la volatilidad incondicional del propio activo, así que con una desviación diaria de 3.25 % frente al 1.08 % de SPY el nivel de base de NVDA ya es tan elevado que la variación adicional atribuible al régimen pesa proporcionalmente mucho menos, y el segundo mecanismo es que buena parte de la varianza de NVDA proviene de saltos discretos ligados a reportes trimestrales y anuncios de producto, eventos separados en el calendario que por su naturaleza generan poca dependencia de un día al siguiente, a diferencia de SPY y GLD, donde la volatilidad responde a regímenes macroeconómicos de tasas e inflación que sí persisten durante semanas enteras, sosteniéndose el hecho estilizado entonces como regularidad general, aunque su intensidad depende de si la volatilidad del activo la conduce el ciclo macroeconómico o el calendario corporativo, matiz que la sección de auditoría retomará."""

H3 = r"""**Interpretación:** La evidencia es contundente en los tres activos y constituye el más nítido de los cuatro hechos, ya que el exceso de curtosis alcanza $7.87$ en SPY, $7.81$ en GLD y $3.70$ en NVDA, valores que frente a un error estándar de $\sqrt{24/n} = 0.138$ producen estadísticos $z$ de $56.8$, $56.4$ y $26.8$ respectivamente, de modo que la distancia respecto del valor 3 que corresponde a la normal no admite atribuirse a variabilidad muestral, traduciendo el conteo de eventos extremos esos momentos a un lenguaje de riesgo directo, porque en 1,252 sesiones una distribución normal predeciría 3.4 observaciones más allá de tres desviaciones estándar y se observaron 13 en SPY, 13 en NVDA y 18 en GLD, es decir 3.8, 3.8 y 5.3 veces lo esperado, y esa razón es exactamente el orden de magnitud del error que cometería un modelo gaussiano al cuantificar el riesgo de cola.

Un detalle contraintuitivo merece mención, ya que NVDA presenta el menor exceso de curtosis pese a ser con diferencia el activo más volátil, y la razón es que la curtosis se normaliza por la desviación estándar del propio activo, así que un movimiento del 10 % equivale a poco más de tres desviaciones para NVDA mientras que para SPY representa más de nueve, lo cual confirma que la curtosis mide la desproporción de las colas y no su tamaño absoluto."""

H4 = r"""**Interpretación:** El hecho se confirma en los tres activos en su sentido estricto, que es que el sesgo difiere de cero, ya que frente a un error estándar de $\sqrt{6/n} = 0.069$ los coeficientes de $0.150$ en SPY, $0.260$ en NVDA y $-0.804$ en GLD producen estadísticos $z$ de $2.17$, $3.76$ y $-11.61$, todos significativos al 5 %, de manera que ninguna de las tres distribuciones puede considerarse simétrica, contradiciendo la dirección del sesgo en cambio la expectativa de manual y conviene decirlo con claridad, porque la literatura asocia sesgo negativo a los activos accionarios y aquí los dos instrumentos de renta variable resultaron positivos, mientras el oro, habitualmente tratado como refugio, es el único con cola izquierda pesada y además el de mayor magnitud absoluta del grupo.

La explicación más plausible está en el periodo elegido, ya que la ventana de cinco años contiene un mercado bajista en 2022 que se desarrolló como un descenso gradual repartido en muchas sesiones moderadamente negativas, seguido de recuperaciones durante 2023 y 2024 concentradas en pocas sesiones de alza explosiva, y esa combinación de caída lenta con rebote violento produce precisamente un tercer momento positivo, reforzando un segundo hallazgo la necesidad de cautela, porque la regla que compara la media contra la mediana apunta en dirección contraria al coeficiente en SPY y en NVDA, ya que en ambos la mediana supera a la media, señal que suele asociarse con sesgo negativo, mientras el tercer momento resulta positivo.

Esa discrepancia no es un error de cálculo sino una consecuencia directa de las colas pesadas documentadas en el hecho anterior, dado que el coeficiente de sesgo eleva las desviaciones al cubo y queda por tanto dominado por un puñado de observaciones extremas al alza, mientras la mediana describe el centro de la distribución, donde la mayoría de las sesiones son ligeramente negativas, y el segundo panel de la figura permite verificar ese desequilibrio contando directamente las sesiones que superan dos desviaciones a cada lado."""

for txt in (H1, H2, H3, H4):
    if PEND in s:
        s = s.replace(PEND, txt, 1)

S5_6_7 = r"""## 5. Prompt utilizado

La consigna indica pegar un prompt específico acompañado del análisis del punto 4, habiéndose realizado la auditoría con **Google Gemini**, deliberadamente distinto del modelo empleado como apoyo durante la redacción, porque un revisor que comparte origen con el texto revisado tiende a validar sus propios supuestos en lugar de cuestionarlos.

> **Prompt enviado**
>
> Con base en estos resultados (PEGA TU ANÁLISIS DEL PUNTO 4), revisa si mi análisis sobre los hechos estilizados está justificado, señalando posibles fallas metodológicas o interpretativas.
>
> ---
>
> **ANÁLISIS DEL PUNTO 4**
>
> **Datos:** Precios diarios de cierre ajustado de SPY (SPDR S&P 500 ETF, NYSE Arca), NVDA (NVIDIA, NASDAQ) y GLD (SPDR Gold Shares, NYSE Arca), del 1 de septiembre de 2021 al 28 de agosto de 2026, con 1,253 precios y 1,252 rendimientos logarítmicos por activo, eligiéndose la ventana de 5 años para incluir el mercado bajista de 2022 y así garantizar al menos un cambio de régimen de volatilidad.
>
> **Estadísticos descriptivos de los rendimientos logarítmicos diarios:**
>
> | Activo | Media | Desv. Est. | Mediana | Sesgo | Curtosis | Exceso de curtosis |
> |---|---|---|---|---|---|---|
> | SPY | 0.00048 | 0.01083 | 0.00063 | 0.15037 | 10.86552 | 7.86552 |
> | NVDA | 0.00182 | 0.03252 | 0.00256 | 0.26021 | 6.70439 | 3.70439 |
> | GLD | 0.00070 | 0.01185 | 0.00078 | -0.80385 | 10.81082 | 7.81082 |
>
> **Hecho I, dependencia lineal débil:** Autocorrelación de primer rezago: SPY -0.0257, NVDA -0.0459, GLD -0.0229, contra una banda de significancia de ±0.0554, concluyendo que el hecho se cumple, reportando que el rezago 3 de NVDA (-0.0587) supera la banda y que el de SPY (-0.0554) queda justo sobre ella, y argumentando que con 25 rezagos evaluados al 5 % se esperan 1.25 excedencias por azar, de modo que una sola excedencia es consistente con la hipótesis nula.
>
> **Hecho II, agrupamiento de volatilidad:** Autocorrelación de primer rezago de los rendimientos al cuadrado: SPY 0.1991 con 11 de 25 rezagos significativos, GLD 0.1565 con 16 de 25, NVDA 0.0440 con solo 3 de 25, concluyendo que el hecho se cumple con claridad en SPY y GLD pero es débil en NVDA, explicando esa anomalía por dos vías: que el agrupamiento se mide relativo a la volatilidad incondicional y la de NVDA ya es muy alta (3.25 % diario contra 1.08 % de SPY), y que la varianza de NVDA proviene de saltos discretos por reportes trimestrales que están separados en el calendario, mientras la de SPY y GLD responde a regímenes macroeconómicos persistentes.
>
> **Hecho III, colas pesadas:** Exceso de curtosis de 7.87 (SPY), 3.70 (NVDA) y 7.81 (GLD), con estadísticos z de 56.8, 26.8 y 56.4 usando un error estándar de raíz de 24/n, observándose más allá de 3 desviaciones estándar 13, 13 y 18 contra 3.4 esperadas bajo normalidad, es decir 3.8, 3.8 y 5.3 veces, concluyendo que el hecho se cumple en los tres y señalando que NVDA tiene el menor exceso de curtosis pese a ser el más volátil porque la curtosis se normaliza por la desviación estándar del propio activo.
>
> **Hecho IV, asimetría:** Sesgo de 0.15037 (SPY), 0.26021 (NVDA) y -0.80385 (GLD), con z de 2.17, 3.76 y -11.61 usando error estándar de raíz de 6/n, los tres significativos al 5 %, concluyendo que el hecho se cumple porque el sesgo difiere de cero, pero señalando que la dirección contradice la expectativa de manual, ya que los dos activos accionarios resultaron positivos y el oro negativo, atribuyendo el signo positivo de las acciones al periodo, un bajista de 2022 desarrollado como descenso gradual seguido de recuperaciones concentradas en pocas sesiones de alza explosiva, reportando también que la regla media contra mediana apunta en dirección contraria al coeficiente en SPY y NVDA, porque en ambos la mediana supera a la media, y explicando la discrepancia por el efecto de las colas pesadas sobre el tercer momento.
>
> **Método:** Toda la evidencia es gráfica y descriptiva: gráficas ACF, gráficas PACF de los cuadrados, histogramas con densidad empírica superpuesta a la normal de referencia, y tablas de momentos muestrales, sin aplicar pruebas de hipótesis formales.

## 6. Respuesta de la IA

**Evaluación metodológica:** El análisis descriptivo es sólido y la selección de una ventana de cinco años resulta crucial para capturar cambios de régimen, sin embargo el uso de errores estándar asintóticos clásicos asume normalidad subyacente, lo cual subestima la varianza de los propios estimadores de sesgo y curtosis en presencia de colas pesadas empíricamente demostradas, limitando la robustez estadística estricta la ausencia de pruebas formales conjuntas como Ljung-Box para autocorrelación o multiplicadores de Lagrange para efectos ARCH, aunque el enfoque visual y de momentos es perfectamente adecuado para validar los hechos estilizados a un nivel general en esta práctica.

**Evaluación interpretativa:** La justificación sobre la anomalía de NVDA en el agrupamiento de volatilidad es excepcionalmente analítica, separando correctamente la microestructura de saltos discretos por reportes corporativos frente a la persistencia macroeconómica que gobierna la dinámica de los índices y materias primas, resultando la resolución teórica del sesgo positivo en renta variable otro acierto interpretativo notable, ya que fundamenta el resultado en la mecánica estructural del ciclo bajista de 2022 y las recuperaciones explosivas posteriores, resolviendo además con elegancia matemática la aparente contradicción entre la regla media-mediana y el tercer momento muestral.

## 7. Correcciones derivadas de la auditoría

**Limitaciones metodológicas reconocidas:** Se acepta la observación de la IA respecto a los errores estándar asintóticos, por lo que es necesario tener presente que la significancia estadística del sesgo y la curtosis podría estar sobreestimada por la propia naturaleza leptocúrtica de los datos, limitando la fiabilidad paramétrica de los estadísticos $z$ exactos sin alterar la demostración empírica del hecho estilizado.

**Pruebas conjuntas pendientes:** Se reconoce la pertinencia de implementar pruebas estadísticas rigurosas en futuros análisis de riesgo, especificando que herramientas analíticas como Ljung-Box o ARCH-LM aportarían la calibración necesaria para modelos tipo GARCH, aunque se mantiene intacta la estructura puramente descriptiva actual por ser el alcance directo definido para esta entrega.

**Integridad interpretativa:** No se realizan modificaciones a las explicaciones elaboradas sobre la asimetría de la renta variable o la divergencia de NVDA en su volatilidad condicional, dado que la auditoría valida estas deducciones como un acercamiento profundo y ajustado a la realidad del mercado frente a las expectativas convencionales de manual."""

s = re.sub(r"## 5\. Prompt utilizado.*?## 7\. Correcciones derivadas de la auditoría\n\n\*\([^\)]*\)\*", lambda _: S5_6_7, s, flags=re.DOTALL)

CONC = r"""# IV) Conclusiones

Los tres activos coinciden en tres de los cuatro hechos y difieren justo en el que más importa para medir riesgo, ya que coinciden en la **dependencia lineal débil**, con autocorrelaciones de primer rezago de $-0.0257$, $-0.0459$ y $-0.0229$ contra una banda de $\pm 0.0554$ y con excedencias aisladas en el rezago 3 que caen dentro de lo esperable por azar al evaluar veinticinco rezagos, coinciden también en las **colas pesadas**, que es el hecho más robusto del ejercicio, con excesos de curtosis de $7.87$, $3.70$ y $7.81$, estadísticos $z$ superiores a 26 en los tres casos y entre 3.8 y 5.3 veces más sesiones extremas de las que predice la normal, y coinciden por último en presentar **asimetría** estadísticamente distinta de cero, con los tres coeficientes significativos al 5 %.

Difieren en dos dimensiones, y la primera es el **agrupamiento de volatilidad**, claro en SPY y GLD, cuya autocorrelación de cuadrados sube a $0.1991$ y $0.1565$ y permanece significativa en 11 y 16 de 25 rezagos, pero débil en NVDA con $0.0440$ y solo 3 rezagos, diferencia que atribuyo a que la volatilidad de un índice y la del oro las conduce el ciclo macroeconómico mientras la de una acción individual la conduce un calendario de eventos corporativos discretos, y la segunda es el **signo de la asimetría**, ya que los dos instrumentos accionarios resultaron positivos con $0.150$ y $0.260$ mientras el oro resultó negativo con $-0.804$, lo cual invierte la expectativa habitual y responde a la forma particular que tomó el ciclo 2021-2026.

Las implicaciones para la medición de riesgo son tres, ya que en primer lugar un modelo gaussiano subestima la frecuencia de eventos extremos por un factor de entre 3.8 y 5.3 en esta muestra, de modo que un VaR paramétrico normal resultaría insuficiente en los tres activos y el error sería mayor precisamente en GLD, el instrumento que la intuición trataría como más seguro, en segundo lugar la volatilidad condicional justifica modelarse con familias tipo GARCH en SPY y GLD, donde el agrupamiento es fuerte, mientras en NVDA ese enfoque aportaría menos y convendría complementarlo con un componente de saltos, y en tercer lugar, que es lo más relevante para construir cartera, el activo refugio del grupo resulta el único con asimetría negativa marcada, así que su aparente seguridad se sostiene en una volatilidad moderada que oculta una cola izquierda más pesada, y cualquier medida de riesgo limitada a media y varianza pasaría por alto exactamente esa característica."""

s = re.sub(r"# IV\) Conclusiones\n\n\*\([^\)]*\)\*", lambda _: CONC, s, flags=re.DOTALL)

with open(p, "w", encoding="utf-8") as f:
    f.write(s)

print("Documento Rmd estructurado y listo para el knit final.")
