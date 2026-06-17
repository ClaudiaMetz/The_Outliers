# 🚦 Análisis y Predicción de Siniestralidad Vial (CABA)
**Proyecto Final - Programación Avanzada en Ciencia de Datos | The Outliers**

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Dash](https://img.shields.io/badge/Dash_Plotly-0F1117?style=for-the-badge&logo=plotly&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)

## 📖 Resumen Ejecutivo
Este proyecto desarrolla un pipeline analítico end-to-end para evaluar y predecir la probabilidad de víctimas fatales en siniestros viales en la Ciudad Autónoma de Buenos Aires (2019-2024). 

Mediante la integración de datos gubernamentales con variables meteorológicas y cronológicas, se construyó un ecosistema de datos que culmina en un modelo de Machine Learning y una interfaz de Business Intelligence para la toma de decisiones basada en evidencia.

---

## 🎯 El Desafío Analítico
La siniestralidad vial es un fenómeno complejo y multifactorial. El objetivo de este proyecto fue aislar y cuantificar el impacto de variables exógenas en la letalidad de un accidente. 

**Hipótesis de investigación evaluadas:**
1. **Factor Climático:** La precipitación y la temperatura alteran significativamente el riesgo.
2. **Efecto Calendario:** La dinámica de movilidad en días de descanso (feriados/fines de semana) incrementa la fatalidad.
3. **Complejidad Algorítmica:** Un modelo de ensamble (Random Forest) capturará mejor la no linealidad del fenómeno frente a un modelo paramétrico (Regresión Lineal).

---

## 📊 Interfaz de Visualización (Dashboard BI)
Se desarrolló una aplicación interactiva para la exploración multidimensional del dataset y la auditoría de los modelos predictivos.

> ![Dashboard Resumen](https://github.com/Marian2057/The_Outliers/blob/main/Material_Sustentacion/Dashboard/Pantalla-1.JPG)
> *Vista general: Evolución histórica y perfil de vulnerabilidad.*
>
> ![Dashboard Resumen](https://github.com/Marian2057/The_Outliers/blob/main/Material_Sustentacion/Dashboard/Pantalla-2.JPG)
> *Clima y Calendario: Probabilidad de fatalidad promedio: Laborales vs Fines de Semanas vs Feriados.*

> ![Dashboard Métricas](https://github.com/Marian2057/The_Outliers/blob/main/Material_Sustentacion/Dashboard/Pantalla-3.JPG)
> *Evaluación algorítmica: Comparación de rendimiento RMSE/MAE y análisis Real vs. Predicho.*

---

## 🛠 Metodología y Pipeline de Datos

El flujo de trabajo se estructuró combinando paradigmas de Programación Orientada a Objetos, Funcional e Imperativo:

1. **Extracción y Enriquecimiento (ETL):** - Procesamiento de **54.064** registros únicos (Dataset GCBA).
   - Ingesta de variables climáticas históricas mediante la API de **Open-Meteo**.
   - Integración de matriz de feriados nacionales (`holidays.AR`).
2. **Preprocesamiento Seguro:** Implementación de `ColumnTransformer` (StandardScaler y OneHotEncoder) integrado en `Pipelines` de scikit-learn para evitar fuga de datos (data leakage).
3. **Experimentación Automatizada:** Uso de `Papermill` para la ejecución sistemática de escenarios, iterando sobre hiperparámetros y semillas de validación.
4. **Persistencia Cloud:** Escritura automatizada de datos limpios, resultados predictivos y metadatos de configuración en colecciones NoSQL de **MongoDB Atlas**.

---

## 💡 Insights y Conclusiones Clave

* 🌦️ **El clima domina la predicción:** Las variables meteorológicas concentran el **62.7%** de la importancia relativa en la toma de decisiones del algoritmo.
* 📅 **Estacionalidad del Riesgo:** Se confirmó un aumento estadísticamente significativo de la letalidad durante domingos y feriados, sugiriendo cambios en el perfil de conducción y vigilancia en días de descanso.
* 🤖 **Refutación Algorítmica (Overfitting):** El modelo Random Forest ($R^2$ = -0.1227) sufrió de un sobreajuste severo frente a los datos de prueba, penalizado por el extremo desbalance de clases (98.3% de eventos no fatales). La **Regresión Lineal** demostró ser el algoritmo superior al mantener la estabilidad paramétrica y la capacidad de generalización ($R^2$ = 0.0158).

---

## 🚀 Reproducibilidad del Entorno

### Requisitos previos
* Python 3.9+
* Cuenta de MongoDB Atlas (Configurar URI en el archivo `.env` o directamente en la notebook).

## Declaración de Uso de Herramientas de IA 
En cumplimiento con los lineamientos de la asignatura, el equipo declara que se utilizaron asistentes de Inteligencia Artificial (Claude, Gemini) exclusivamente como herramienta de apoyo para la generación de boilerplate de código y asistencia en la redacción y estructuración de este documento. Todo el diseño experimental, la toma de decisiones técnicas, el análisis de las métricas y la justificación de las hipótesis presentadas son de autoría propia y exclusiva del equipo "The Outliers"


## 📂 Estructura del Repositorio
Siguiendo las mejores prácticas de ingeniería de software para Ciencia de Datos, este repositorio se estructura de la siguiente manera:

```text
Material_Sustentacion/
├── data/                        # Datos del proyecto
│   ├── datos/                   # Dataset original de accidentes
│   └── external/                # Datos climáticos extraídos de la API de Open-Meteo
├── notebooks/                   # Jupyter Notebooks de análisis y modelado
│   └── siniestro_vialF.ipynb    # Notebook principal con todo el flujo de ML
├── Automatizaciones/            # Scripts para automatización con Papermill
│   ├── resultado_exp_1          # Resultado de la automatización 1
│   └── resultado_exp_2          # Resultado de la automatización 2
│   └── resultado_exp_3          # Resultado de la automatización 3
├── .gitignore                   # Archivos excluidos del control de versiones (ej. claves, .env)
├── requirements.txt             # Listado de dependencias del proyecto
├── Dashboard/                   # Capturas de las pantallas del dashboard
├── Informe/                     # Documentación
│   └── Informe del proyecto     # Informe del preoyecto
│   └── presentacion             # Presentación
README.md                        # Documentación técnica y de uso


