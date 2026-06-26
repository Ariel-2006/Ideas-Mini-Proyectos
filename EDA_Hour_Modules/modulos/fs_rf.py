# Librerías necesarias
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def feature_selection_rf(X_train_rf, X_test_rf, y_train_rf, y_test_rf):
    """
    Realiza selección de características usando Random Forest y evalúa el modelo resultante.
    Parámetros:
    X_train_rf, X_test_rf: Conjuntos de características para entrenamiento y prueba.
    y_train_rf, y_test_rf: Etiquetas objetivo para entrenamiento y prueba.
    Retorna:
    tuple: (resultado_str)
        resultado_str (str): Resumen de métricas del modelo con características seleccionadas.
    """

    # 1. Definición del número de variables
    # Se aumenta a 10 el número de predictores para capturar más complejidad.
    k = 10

    # 2. Configuración del selector estadístico
    # Inicializa 'SelectKBest' usando la prueba ANOVA (f_classif) para filtrar las variables.
    select_rf = SelectKBest(score_func=f_classif, k=k)

    # 3. Ajuste y reducción del entrenamiento
    # Identifica las 10 mejores variables en el set de entrenamiento y lo transforma.
    X_train_rf_fs = select_rf.fit_transform(X_train_rf, y_train_rf)

    # 4. Transformación del set de prueba
    # Aplica la misma reducción de columnas al conjunto de testeo.
    X_test_rf_fs = select_rf.transform(X_test_rf)

    # 5. Extracción de la máscara booleana
    # Crea un filtro para identificar qué columnas fueron conservadas por el algoritmo.
    mask_rf = select_rf.get_support()

    # 6. Mapeo de nombres de variables
    # Recupera los nombres reales de las columnas seleccionadas desde el DataFrame original.
    features_selec_rf = X_train_rf.columns[mask_rf]

    # 1. Definición del modelo
    # Crea un bosque de 300 árboles de decisión; 'random_state' asegura resultados reproducibles.
    rf_fs = RandomForestClassifier(n_estimators=300, random_state=42)

    # 2. Entrenamiento del modelo
    # El algoritmo entrena usando las 10 mejores variables seleccionadas previamente.
    rf_fs.fit(X_train_rf_fs, y_train_rf)

    # 3. Predicción de resultados
    # Genera las etiquetas de demanda (0 o 1) para el conjunto de prueba.
    y_pred_rf_fs = rf_fs.predict(X_test_rf_fs)

    # 4. Cálculo de exactitud
    # Evalúa qué porcentaje de las predicciones totales fueron correctas.
    acc_rf = accuracy_score(y_test_rf, y_pred_rf_fs)

    # 5. Matriz de Confusión
    # Desglose numérico de aciertos y errores (Verdaderos Positivos vs. Falsos Positivos).
    matriz = confusion_matrix(y_test_rf, y_pred_rf_fs)

    # 6. Reporte de Clasificación
    # Muestra métricas de precisión, recall y F1-score para medir el desempeño por clase.
    report = classification_report(y_test_rf, y_pred_rf_fs)

    return (f"\nSelección de Características con Random Forest (Top {k} features)\n"
            f"Features Seleccionadas: {list(features_selec_rf)}\n"
            f"Accuracy: {acc_rf:.4f}\n"
            f"Matriz de Confusión:\n{matriz}\n"
            f"Reporte de Clasificación:\n{report}")
