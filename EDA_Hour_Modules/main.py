import matplotlib.pyplot as plt
from modulos import preprocesamiento
from modulos import graficos
from modulos import model_lr, model_rf, fs_rf

def ejecutar():  
    """
    Integrantes: Ariel Jiménez, Sebastián León, Jhanela Llivipuma, Fiorella Marín, Camilo Morocho, 
    Leandre Luzuriaga, Santiago Morales, Sebastián Guijarro
    Fecha: 30 de enero de 2026
    Carrera: Ciencia de Datos 
    Periodo académico: 2025-2S
    Semestre: Segundo semestre C

    Función principal que orquesta el flujo de trabajo:
    Carga, procesamiento, entrenamiento, selección de variables y visualización.
    """
    print("--- Iniciando el trabajo ---") 
    
    # --- FASE 1: Preparación de datos ---
    # Se obtienen dos versiones: la procesada (numérica/escalada para modelos) 
    # y la original para análisis visuales exploratorio
    print("\nCargando y limpiando datos...")
    df_procesado, df_original = preprocesamiento.cargar_y_limpiar()

    # --- FASE 2: Modelado ---
    print("\nModelos entrenándose...")

    # Entrenamiento de Regresión Logística (LR)
    # Retorna métricas, valores reales de prueba y las predicciones
    resultado_lr, y_test, m_pred = model_lr.ejecutar_modelo_lr(df_procesado)

    # Entrenamiento de Random Forest (RF)
    # Además del resultado, devuelve los splits de datos (X/y train/test) para reusarlos
    resultado_rf, X_train_rf, X_test_rf, y_train_rf, y_test_rf = model_rf.ejecutar_modelo_rf(df_procesado)

    # --- FASE 3: Optimización / Feature Selection ---
    # Identifica qué variables son las más importantes usando la lógica de Random Forest
    resultado_fs_rf = fs_rf.feature_selection_rf(X_train_rf, X_test_rf, y_train_rf, y_test_rf) 

    # --- FASE 4: Visualización de resultados ---
    print("\nMostrando gráficos...")
 
    # Generación de la Matriz de Confusión para evaluar errores de clasificación
    confusion_plot = graficos.grafico_matriz_confusion(
        y_test, 
        m_pred, 
        clases=['Baja', 'Alta'], 
        titulo="Matriz de Confusión - Regresión Logística"
    )

    # Generación de gráfico exploratorio basado en el dataframe original
    plot_fig = graficos.hacer_grafico(df_original)
    
    # --- FASE 5: Reporte por consola ---
    print(resultado_lr)
    print(resultado_rf)

    print("\nResultados de selección de características con Random Forest:")
    print(resultado_fs_rf)

    # Impresión de visualizaciones generadas
    print(plot_fig)
    print(confusion_plot)

    # Renderizado final de todas las ventanas de Matplotlib
    plt.show()

    print("--- ¡Todo salió bien! ---")

# Punto de entrada estándar de Python para evitar ejecuciones accidentales al importar
if __name__ == "__main__":
    ejecutar()