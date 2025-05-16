# 📈 Flujo de Datos – Pipeline de KPIs de Mantenimiento

Este documento describe el flujo de datos completo del proyecto `Plant Maintenance KPI Pipeline`, desde la ingesta inicial hasta la visualización de los indicadores clave (KPIs).

---

## 🔄 Etapas del flujo

### 1. Ingesta de Datos (CSV → GCS → BigQuery)
- Archivos simulados (`ordenes_mantenimiento.csv`, `backlog.csv`) cargados a GCS manualmente o vía Cloud Function.
- Cargados luego a BigQuery como tablas externas o definitivas.

### 2. Modelado con Dataform
- Se construyen tres modelos principales:
  - `ordenes`: transforma las órdenes de mantenimiento.
  - `backlog`: procesa el backlog pendiente.
  - `kpis`: calcula métricas agregadas por tipo de mantenimiento.
- Validación con assertion `validar_ordenes.assertion.sqlx` para garantizar calidad de datos.

### 3. Orquestación con Airflow
- DAG `mantenimiento_kpis_dag` ejecuta:
  - Inicio del pipeline
  - Comando `dataform run`
  - Validación de assertions
  - Registro de éxito

### 4. Visualización
- Dashboard creado en Power BI o Looker Studio utilizando:
  - `maintenance_kpis.kpis`
  - `maintenance_kpis.ordenes`
  - `maintenance_kpis.backlog`

---

## 📊 KPIs calculados

| Indicador                            | Descripción                                      |
|-------------------------------------|--------------------------------------------------|
| % órdenes preventivas/correctivas   | Proporción de tipos de mantenimiento             |
| Tiempo promedio por tipo            | Tiempo promedio invertido por orden              |
| Backlog pendiente                   | Órdenes no finalizadas, con días acumulados      |
| Órdenes por equipo                  | Cantidad de intervenciones por equipo técnico    |
| Equipos más intervenidos            | Ranking de los equipos con más intervenciones    |

---

## 🧪 Validaciones

- `tiempo_hrs > 0`
- `fecha_creacion IS NOT NULL`
- `fecha_finalizacion IS NOT NULL`

---