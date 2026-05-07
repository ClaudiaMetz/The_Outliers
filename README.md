**Equipo:** The Outliers 📊 

Integrantes:
* Claudia Metz
* Marianela Pi

# **Proyecto:** Trabajo Final Integrador - Modelos Predictivos  

## 🎯 Objetivo del Proyecto
El objetivo principal de este proyecto es desarrollar y comparar modelos de Machine Learning (Regresión Lineal Múltiple y Random Forest) capaces de predecir la cantidad diaria de siniestros viales en base a factores ambientales y temporales.

Se busca identificar qué variables externas inciden con mayor peso en la frecuencia de accidentes para generar un modelo predictivo robusto, cuyas métricas de rendimiento (RMSE, MAE, R²) serán registradas en una base de datos documental (MongoDB Atlas) para su auditoría y comparación.

## 2. Hipótesis Iniciales
Antes de la fase de modelado, establecemos las siguientes hipótesis rectoras que serán evaluadas empíricamente:

* **Hipótesis 1 (Factor Climático):** Las precipitaciones (lluvia) tienen una correlación positiva fuerte con el aumento de la cantidad diaria de siniestros, debido a la reducción de visibilidad y adherencia en la calzada.
* **Hipótesis 2 (Efecto Calendario):** Existe una marcada estacionalidad semanal. La volumetría de siniestros durante los fines de semana y feriados difiere significativamente de los días laborables debido a los cambios en la dinámica de movilidad urbana.
* **Hipótesis 3 (Rendimiento Algorítmico):** Dada la probable existencia de relaciones no lineales entre las variables (ej. el efecto combinado de lluvia durante un fin de semana), se espera que el modelo de ensamble basado en árboles (*Random Forest*) supere al modelo paramétrico (*Regresión Lineal*) en las métricas de evaluación.

* **Extracción de Datos Externa:** API de Open-Meteo (Datos climáticos históricos).
* **Análisis y Manipulación de Datos:** Pandas, NumPy, Holidays (Argentina).
* **Machine Learning:** Scikit-Learn (Pipelines, ColumnTransformer, StandardScaler, OneHotEncoder).
* **Base de Datos NoSQL:** MongoDB Atlas (Cloud) mediante PyMongo.
* **Visualización e Interfaz:** Streamlit (Presentación interactiva), Matplotlib, Seaborn.
* **Control de Versiones:** Git / GitHub.

## 🏗️ Ingeniería de Características (Feature Engineering)
Para optimizar la capacidad predictiva del modelo, se transformó la variable temporal original para capturar patrones de comportamiento:
* **Variables Climáticas:** Temperatura media diaria y acumulado de precipitaciones (API).
* **Variables de Calendario:** Extracción de mes y día de la semana.
* **Variables Binarias:** Detección automática de feriados nacionales (Argentina) y fines de semana para evaluar el impacto de la movilidad urbana.

## 🗄️ Almacenamiento NoSQL (Cloud Architecture)
Se implementó un clúster en la nube con **MongoDB Atlas**, permitiendo la persistencia centralizada y el acceso global (IP 0.0.0.0/0) para la colaboración del equipo. El esquema documental se organiza en:
* `datos_entrada`: Dataset consolidado diario con clima y siniestros.
* `resultados_modelo`: Log de métricas RMSE, MAE y R² por ejecución.
* `configuracion`: Parámetros técnicos de los modelos entrenados.

## 📂 Estructura del Repositorio
```text
├── data/
│   ├── siniestros_limpios.csv      # Dataset preprocesado
├── notebooks/
│   ├── 01_ETL_y_EDA.ipynb          # Extracción, limpieza y exploración
│   ├── 02_Modelos_Machine_Learning.ipynb # Entrenamiento y evaluación
├── scripts/
│   ├── db_connection.py            # Script de conexión y carga a MongoDB
├── app.py                          # Aplicación interactiva de Streamlit
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Documentación



