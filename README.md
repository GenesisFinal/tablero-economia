# Tablero de Indicadores Económicos • La Segunda Seguros

Tablero interactivo y auto-actualizable de indicadores macroeconómicos y financieros de Argentina.

## Despliegue en Vivo
🚀 **URL Pública:** [https://GenesisFinal.github.io/tablero-economia/](https://GenesisFinal.github.io/tablero-economia/)

---

## Características Principales
- **12 Categorías Macroeconómicas y 88 Indicadores:**
  - Precios y Costo de Vida (IPC, Canastas CBA/CBT, UVA)
  - Agregados Monetarios (Base Monetaria, B1, B2, B3, Billetes en circulación)
  - Sector Fiscal (Recaudación IVA, Seg. Social, Resultado Primario y Financiero)
  - Comercio Internacional (Exportaciones FOB, MOI, Importaciones CIF, Balanza)
  - Reservas y Deuda (Reservas BCRA, Deuda Pública Total, Externa, FMI, Riesgo País)
  - Empleo y Salarios (Empleo Privado, Total, RIPTE, SMVM, Salarios)
  - Datos Demográficos (Actividad, Desocupación, Pobreza, Indigencia, Población)
  - Jubilaciones y Social (Mínima, Máxima, Promedio en ARS, USD MEP y Moneda Constante)
  - Actividad y Consumo (EMAE, PBI corriente, constante y en USD MEP, Supermercados)
  - Industria y Energía (Gas, Petróleo, IPI)
  - Campo y Bioeconomía (EMAE Agro, Exportaciones MOA y Primarios)
  - Construcción e Inmobiliario (Cemento, ISAC, Costo Construcción ICC, Asfalto)

- **Métricas y Análisis en Cada Tarjeta:**
  - Valor actualizado con formato de moneda/unidad
  - Variación mensual ($m/m$) o trimestral ($t/t$)
  - Variación interanual ($i.a.$ / YoY)
  - Mini-gráfico Sparkline integrado
  - Modal interactivo con **Recta de Regresión / Tendencia Lineal** ($y = mx + b$)
  - Selectores de período: 1A, 2A, 3A, 5A e Histórico Completo

---

## Actualización Diaria Automática
El repositorio cuenta con un flujo de trabajo de **GitHub Actions** (`.github/workflows/daily_update.yml`) configurado para ejecutarse diariamente de forma automática (a las 06:00 y 18:00 ART):
1. Extrae y audita los datos de fuentes oficiales (ArgentinaDatos, BCRA, INDEC).
2. Valida la integridad de las 88 series temporales y recalcula variaciones y regresiones.
3. Compila y publica la nueva versión del tablero automáticamente en GitHub Pages.

---

## Identidad de Marca y Brandbook
- **Tipografía:** *Sora* y *JetBrains Mono* (Google Fonts)
- **Paleta Institucional:** Rojo La Segunda (`#E20039`), Dark Navy (`#0B1120`, `#0F172A`, `#1E293B`) y Light Theme.
