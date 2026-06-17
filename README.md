# 🚗 Predicción de Siniestralidad Vial y Gravedad de Accidentes en Argentina

**Equipo:** The Outliers  
**Asignatura:** Programación Avanzada en Ciencia de Datos  

## 🎯 Objetivo del Proyecto
El objetivo principal de este proyecto es construir un modelo predictivo en Python que determine la **probabilidad de que un accidente de tránsito tenga víctimas fatales**. 

A través de este análisis, buscamos identificar el peso de distintas variables externas (como las condiciones climáticas y el efecto calendario) sobre la letalidad de los accidentes, comparando el rendimiento de modelos paramétricos y de ensamble.

## 🛠️ Stack Tecnológico y Técnicas Aplicadas
* **Lenguaje:** Python 3
* **Manipulación y Limpieza**: Pandas, NumPy.
* **Enriquecimiento de Datos:** Consumo de la API de Open-Meteo (clima) y librería holidays (feriados).
* **Machine Learning:** scikit-learn (Pipelines, ColumnTransformer, StandardScaler, OneHotEncoder).
* **Modelos Evaluados:** Regresión Lineal Múltiple y Random Forest Regressor.
* **Persistencia de Datos:** MongoDB Atlas (NoSQL).
* **Visualización:** Matplotlib y Seaborn.
* **Enfoque Multiparadigma:** El código fue diseñado combinando la Programación Orientada a Objetos (POO) para el modelado predictivo (instanciando clases de scikit-learn como Pipeline y RandomForestRegressor), junto con los paradigmas imperativo y funcional para la manipulación estructurada y limpieza de datos mediante pandas.

## 📊 Metodología y Resultados Obtenidos
El flujo de trabajo incluyó la limpieza de más de 1 millón de registros, aislando 62.076 siniestros válidos y la creación de una variable continua (probabilidad_fatalidad). Los modelos fueron evaluados sobre un 20% de datos de prueba (Test) arrojando los siguientes resultados:
Modelo
RMSE
MAE
R²
Regresión Lineal
0.0253
0.0171
0.0158
Random Forest
0.0270
0.0178
-0.1223
**Interpretación de Métricas:** Aunque los errores absolutos (MAE) son bajos, el coeficiente de determinación (R²) cercano a 0 en la Regresión Lineal y negativo en el Random Forest indica que las variables estrictamente temporales y climáticas no son suficientes para explicar la varianza en la letalidad de los accidentes. La gravedad de un siniestro está fuertemente dictada por la dinámica del choque (velocidad, uso de casco, tipo de vehículo), variables que escapan al alcance de las features actuales.

## 💡 Conclusiones y Evaluación de Hipótesis
* **Hipótesis 1 (Factor Climático)** - VALIDADA PARCIALMENTE: El análisis de importancia de variables (Feature Importance) extraído del modelo de ensamble confirmó que la temp_media y la precipitacion son las dos variables externas con mayor peso predictivo dentro del dataset.
* **Hipótesis 2 (Efecto Calendario)** - VALIDADA: El análisis exploratorio y los resultados del modelo confirmaron una marcada estacionalidad semanal. Los días Domingo y Sábado presentan los picos máximos en la probabilidad media de fatalidad, confirmando que la dinámica de movilidad del fin de semana incrementa el riesgo de letalidad.
* **Hipótesis 3 (Rendimiento Algorítmico)** - REFUTADA: Contrario a la expectativa inicial, el modelo paramétrico simple (Regresión Lineal) superó al modelo de ensamble (Random Forest). El Random Forest arrojó un R² negativo (-0.1223), indicando una incapacidad de generalización frente a datos invisibles para este conjunto de features específicas, mientras que la Regresión Lineal logró un comportamiento marginalmente más estable.

## 🚀 Posibles Mejoras (Next Steps)
Para futuras iteraciones y con el fin de incrementar significativamente el R², se propone:
Incorporar variables intrínsecas del siniestro al modelo predictivo (ej. modo_desplazamiento_victima, rol_victima).
Formular el problema como una Clasificación Binaria en lugar de Regresión, prediciendo directamente la clase (Fatal / No Fatal) utilizando algoritmos como Logistic Regression o XGBoost combinados con técnicas de balanceo de clases (ej. SMOTE).
Optimizar la profundidad y los hiperparámetros del Random Forest mediante GridSearchCV.

## ⚙️ Instrucciones de Uso y Reproducibilidad
Clonar el repositorio:
Crear y activar un entorno virtual:
Instalar las dependencias requeridas:
Configurar Base de Datos: Crear un archivo .env en el directorio raíz o definir la variable de entorno MONGO_URI con la cadena de conexión real de MongoDB Atlas. Por seguridad, las credenciales nunca deben subirse al repositorio público.
Ejecución: Abrir e iterar sobre el notebook principal (notebooks/siniestro_vialC.ipynb) o ejecutar los scripts automatizados según sea necesario.

## 📂 Estructura del Repositorio
Siguiendo las mejores prácticas de ingeniería de software para Ciencia de Datos, este repositorio se estructura de la siguiente manera:

```text
Material_Sustentacion/
├── data/                  # Datos del proyecto
│   ├── raw/               # Dataset original de accidentes
│   └── external/          # Datos climáticos extraídos de la API de Open-Meteo
├── notebooks/             # Jupyter Notebooks de análisis y modelado
│   └── siniestro_vialF.ipynb  # Notebook principal con todo el flujo de ML
├── scripts/               # Scripts para automatización (ej. ejecución con Papermill)
├── .gitignore             # Archivos excluidos del control de versiones (ej. claves, .env)
├── requirements.txt       # Listado de dependencias del proyecto
README.md                  # Documentación técnica y de uso


