from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def ejecutar_modelo_rf(df):
    """
    Entrena y evalúa un modelo de Random Forest para clasificar la demanda de bicicletas.
    Parámetros:
    df (DataFrame): DataFrame preprocesado con características y variable objetivo 'cnt'.
    Retorna:
    tuple: (resultado_str, X_train, X_test, y_train, y_test)
        resultado_str (str): Resumen de métricas del modelo.
        X_train, X_test, y_train, y_test: Splits de datos para entrenamiento y prueba.
    """ 
    # 1. Creamos la variable objetivo categórica basada en la mediana
    # 0 = Baja, 1 = Alta
    mediana = df['cnt'].median()
    df['high_demand'] = (df['cnt'] > mediana).astype(int) 
    
    # 2. Definimos X e y (usamos la nueva columna como target)
    y = df['high_demand']

    # Define las variables predictoras eliminando las columnas que causarían fuga de datos (leakage)
    # Se quitan 'high_demand' (target de clasificación) y 'casual'/'registered' (suman el total de 'cnt')
    X = df.drop(columns=['high_demand', 'cnt', 'casual', 'registered'])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Entrenamos el Clasificador
    m = RandomForestClassifier(n_estimators=50, random_state=42)
    m.fit(X_train, y_train)
    
    # 4. Predicciones y Métricas
    m_pred_rf = m.predict(X_test)
    
    # Calculo del Accuracy (porcentaje de aciertos totales)
    acc = accuracy_score(y_test, m_pred_rf)
    
    # Matriz para ver dónde se confunde el modelo (Falsos Positivos vs Falsos Negativos)
    confmatrix = confusion_matrix(y_test, m_pred_rf)
    
    # El reporte incluye Precisión, Recall y F1-Score para cada categoría
    classreport = classification_report(y_test, m_pred_rf, target_names=['Baja', 'Alta'])
    
    # Se devuelve un string formateado con los resultados y los sets de datos para futuros usos (como FS)
    return (f"\nModelo de Clasificación RandomForestClassifier (Target: Mediana {mediana})\n"
            f"Accuracy: {acc:.4f}\n\n"
            f"Matriz de Confusión:\n{confmatrix}\n\n"
            f"Reporte de Clasificación:\n{classreport}", X_train, X_test, y_train, y_test)