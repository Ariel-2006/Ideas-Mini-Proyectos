# Librerías necesarias
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def ejecutar_modelo_lr(df):
    """
    Entrena y evalúa un modelo de Regresión Logística para clasificar la demanda de bicicletas.
    Parámetros:
    df (DataFrame): DataFrame preprocesado con características y variable objetivo 'cnt'.
    Retorna:
    tuple: (resultado_str, y_test, m_pred)
        resultado_str (str): Resumen de métricas del modelo.
        y_test (Series): Valores reales del conjunto de prueba.
        m_pred (ndarray): Predicciones del modelo sobre el conjunto de prueba.
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
    
    # Dividimos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Entrenamos el Clasificador
    m = LogisticRegression(max_iter=1000,solver='liblinear')
    m.fit(X_train, y_train)
    
    # 4. Predicciones y Métricas
    m_pred = m.predict(X_test)
    
    # Cálculo de métricas
    acc = accuracy_score(y_test, m_pred)
    confmatrix = confusion_matrix(y_test, m_pred)
    classreport = classification_report(y_test, m_pred, target_names=['Baja', 'Alta'])
    
    return (f"\nModelo de Clasificación Regresión Logística (Target: Mediana {mediana})\n"
            f"Accuracy: {acc:.4f}\n\n"
            f"Matriz de Confusión:\n{confmatrix}\n\n"
            f"Reporte de Clasificación:\n{classreport}", y_test, m_pred)