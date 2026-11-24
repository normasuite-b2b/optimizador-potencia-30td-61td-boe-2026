# Tarifas Oficiales 3.0TD y 6.1TD BOE 2026 · Optimizador CSV Datadis

> **Calculadora Web 100% en Navegador (0 RGPD, 0 subida de CSV) + Informe PDF Marca Blanca:** [Abrir Optimizador 3.0TD / 6.1TD →](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/)

Dataset oficial estructurado de **peajes (`BOE-A-2025-26348`)**, **cargos (`Orden TED/1524/2025`)**, **excesos de potencia (`Circular 3/2020 mod. Circular 1/2025`)** e **IEE (`5,11269632 %`)** vigentes en España en **2026** para tarifas de acceso **3.0TD** (`> 15 kW` BT) y **6.1TD** (`AT 1–30 kV`), acompañado de un inspector Python sin dependencias y de la calculadora web completa sobre CSV cuartohorario/horario de Datadis.

## Valores Oficiales BOE 2026 (`tariffs_2026.json`)

| Periodo | `3.0TD` Fijo (`€/kW·año`) | `3.0TD` Excesos Tipo 4–5 (`€/kW·día`) | `3.0TD` Excesos Tipo 1–3 (`€/kW`) | `6.1TD` Fijo (`€/kW·año`) | `6.1TD` Excesos Tipo 1–3 (`€/kW`) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **P1** | `20,376927` | `0,171373` | `3,325715` | `29,595368` | `3,431797` |
| **P2** | `10,617621` | `0,090584` | `1,757877` | `15,514709` | `1,818277` |
| **P3** | `4,481534` | `0,028721` | `0,557353` | `6,801881` | `0,680379` |
| **P4** | `3,886333` | `0,021891` | `0,424794` | `5,393829` | `0,478581` |
| **P5** | `2,513851` | `0,006142` | `0,119179` | `2,125113` | `0,010172` |
| **P6** | `1,442287` | `0,006142` | `0,119179` | `1,004181` | `0,008984` |

## Guías Técnicas BOE 2026 y Herramienta Online

- Calculadora completa CSV Datadis → potencias óptimas `P1 ≤ … ≤ P6` + PDF Marca Blanca: **[https://normasuite-b2b.normasuite-b2b.workers.dev/30td/](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/)**
- [Cómo optimizar potencia 3.0TD en 2026](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/guia/optimizar-potencia-30td-boe-2026.html)
- [Excesos de potencia Tipo 4–5 vs Tipo 1–3](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/guia/excesos-potencia-tipo-4-vs-tipo-3.html)
- [Optimizar potencia 6.1TD en industria](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/guia/optimizar-potencia-61td-industria.html)
- [Preparar CSV Datadis cuartohorario vs horario](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/guia/csv-datadis-cuartohorario-vs-horario.html)
- [Calendario peninsular P1–P6 Circular 3/2020](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/guia/calendario-horarios-p1-p6-espana.html)
- [Informes Marca Blanca para asesorías energéticas](https://normasuite-b2b.normasuite-b2b.workers.dev/30td/guia/informe-marca-blanca-asesorias-energeticas.html)

## Inspección rápida en Python

```bash
python inspect_tariffs_boe_2026.py
```
