import papermill as pm

# 1. Nombre exacto de tu archivo Jupyter
notebook_original = 'siniestro_vialF.ipynb' 

# 2. Definimos los 3 escenarios
# (Estos valores van a viajar automáticamente a tu celda "parameters")
escenarios = [
    {"semilla": 42, "estimadores": 50, "profundidad": 5},
    {"semilla": 100, "estimadores": 100, "profundidad": 10},
    {"semilla": 2026, "estimadores": 200, "profundidad": 15}
]

print("Iniciando la automatización de experimentos...")

# 3. El bucle que ejecuta la notebook por cada escenario
for i, escenario in enumerate(escenarios):
    # Genera un nombre nuevo para cada notebook de salida
    notebook_resultado = f'resultado_exp_{i+1}.ipynb'
    
    print(f"--> Ejecutando Experimento {i+1} con parámetros: {escenario}")
    
    try:
        pm.execute_notebook(
            input_path=notebook_original,
            output_path=notebook_resultado,
            parameters=dict(
                SEMILLA=escenario["semilla"],
                N_ESTIMADORES=escenario["estimadores"],
                MAX_PROFUNDIDAD=escenario["profundidad"]
            )
        )
        print(f"    ¡Éxito! Guardado como {notebook_resultado}")
    except Exception as e:
        print(f"    Error en el experimento {i+1}: {e}")

print("¡Proceso de automatización finalizado!")