# Análisis de Riesgos — ITESO

Trabajo del curso **Análisis de Riesgos** de la carrera de Ingeniería Financiera en el
ITESO, Universidad Jesuita de Guadalajara.

**Alumno:** Francisco Uriel Ledezma Chávez
**Profesora:** María del Rosario Ruiz Hernández
**Periodo:** Otoño 2026 · 5.º semestre

Este repositorio reúne las entregas de los cuatro módulos del curso. El proyecto
semestral, que atraviesa los cuatro módulos y desemboca en el artículo científico del
examen final, vive en su propio repositorio y aquí aparece como submódulo en
[`Proyecto-GAPB/`](#proyecto-semestral).

---

## Módulos

| Módulo | Tema | Entregables | Estado |
|---|---|---|---|
| **1** | Hechos estilizados del comportamiento del precio y del rendimiento de los activos | Práctica 1 (`.Rmd` + `.html`), Tarea 1 (referencias bibliográficas) | Entregado |
| **2** | — | — | Pendiente |
| **3** | — | — | Pendiente |
| **4** | — | — | Pendiente |

### Módulo 1

La práctica pone a prueba los cuatro hechos estilizados de los rendimientos financieros
—ausencia de autocorrelación lineal, agrupamiento de volatilidad, colas pesadas y
asimetría— sobre tres activos que cotizan fuera de la BMV, elegidos para representar
fuentes de riesgo deliberadamente distintas:

| Ticker | Instrumento | Bolsa | Papel en el análisis |
|---|---|---|---|
| **SPY** | SPDR S&P 500 ETF Trust | NYSE Arca | Referencia diversificada del mercado accionario |
| **NVDA** | NVIDIA Corporation | NASDAQ | Acción individual de alta volatilidad |
| **GLD** | SPDR Gold Shares | NYSE Arca | Clase de activo distinta, tradicionalmente refugio |

El análisis se escribió en R Markdown y se compila a HTML autocontenido. Para
reproducirlo hace falta R ≥ 4.2 con los paquetes `quantmod` y `moments`.

---

## Proyecto semestral

[`Proyecto-GAPB/`](https://github.com/Urielledezma/GAPB-Risk-Analysis) es un **submódulo
de Git** que apunta al repositorio del proyecto del curso: un marco de análisis de riesgo
de mercado en R aplicado a **Grupo Aeroportuario del Pacífico, Serie B (BMV: GAPB)** y, en
la etapa de portafolio, a una canasta de seis emisoras mexicanas. Cubre la
caracterización del emisor, la atribución de eventos sobre la trayectoria del precio, la
distribución de rendimientos y el movimiento browniano geométrico, los modelos de varianza
condicional (MA, EWMA, ARCH/GARCH) y el Valor en Riesgo con Expected Shortfall y
backtesting.

- **Repositorio:** <https://github.com/Urielledezma/GAPB-Risk-Analysis>
- **Reportes publicados:** <https://urielledezma.github.io/GAPB-Risk-Analysis/>

Al ser un submódulo, la carpeta se ve vacía si el repositorio se clona de la forma
habitual. Para traerla completa:

```bash
git clone --recurse-submodules https://github.com/Urielledezma/Analisis-de-Riesgo.git
```

Si el repositorio ya está clonado sin el submódulo:

```bash
git submodule update --init --recursive
```

---

## Estructura del repositorio

```text
.
├── Modulo-1/           # Práctica 1 y Tarea 1 — hechos estilizados
├── Modulo-2/           # Pendiente
├── Modulo-3/           # Pendiente
├── Modulo-4/           # Pendiente
├── docs/               # Material del curso: lineamientos del examen final
├── Proyecto-GAPB/      # Submódulo → Urielledezma/GAPB-Risk-Analysis
└── Analisis-de-Riesgo.Rproj
```

`docs/` guarda documentación del curso —los lineamientos del artículo científico del
examen final—, no un sitio web renderizado. Este repositorio no publica GitHub Pages; el
sitio de reportes pertenece al proyecto semestral y se sirve desde su propio repositorio.

---

## Licencia

Código y análisis bajo [licencia MIT](LICENSE). El material didáctico del curso incluido
en `docs/` conserva los derechos de sus autores y se reproduce aquí únicamente como
referencia del trabajo entregado.
