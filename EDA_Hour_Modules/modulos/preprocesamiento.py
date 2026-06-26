# Librerías necesarias
import pandas as pd
import numpy as np
import os

def cargar_y_limpiar(): 
    """
    Carga el dataset desde un archivo CSV, realiza limpieza de datos,
    detección de valores atípicos, normalización y codificación one-hot.
    Retorna dos dataframes: uno procesado y otro original sin modificar.
    Parameters:
    df_procesado: DataFrame procesado listo para modelado.
    df_original: DataFrame original sin modificaciones.
    Returns:
    tuple: (df_procesado, df_original)
    """
    # Carga de datos
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_csv = os.path.join(base_path, "Data", "hour.csv")
    
    # Leer el archivo CSV
    df = pd.read_csv(ruta_csv)
    df_original = df.copy() # Guardamos la copia sin procesar
    
    # Limpieza inicial: Eliminamos columnas irrelevantes
    if 'instant' in df.columns:
        df.drop(['instant'], axis=1, inplace=True) # ID único, no aporta valor predictivo

    print(f"Verificación de valores nulos: \n  {df.isna().sum()}")  # Verificamos valores nulos (si los hay)

    # Detección de valores atípicos usando el método de Tukey
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    # Cálculo de los cuartiles Q1 (25%) y Q3 (75%) para definir el rango intercuartílico
    Q1 = df[numeric_cols].quantile(0.25)
    Q3 = df[numeric_cols].quantile(0.75) 
    IQR = Q3 - Q1

    # Define los límites estadísticos superior e inferior (vallas de Tukey)
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR

    # Cuenta y ordena de forma descendente los valores atípicos detectados por columna
    outliers_por_col = ((df[numeric_cols] < lim_inf) | (df[numeric_cols] > lim_sup)).sum().sort_values(ascending=False)
    
    print(f"\nValores atípicos detectados por columna:\n{outliers_por_col[outliers_por_col > 0]}")
    
    # Normalización de columnas específicas usando Min-Max Scaling
    por_norma = ["season","mnth","hr","weekday","weathersit","casual", "registered","cnt"]
    
    #  Función de normalización Min-Max
    def normalize_column(X):
        """
        Normaliza una columna usando Min-Max Scaling.
        
        :param X: Description
        :return: Normalized column
        """
        return (X - X.min()) / (X.max() - X.min()) # Min-Max Scaling
    
    # Aplicamos la normalización y actualizamos el DataFrame
    df[por_norma] = normalize_column(df[por_norma])
    
    # One-Hot Encoding
    df_procesado = pd.get_dummies(df, columns=['dteday'], drop_first=True,dtype=np.float64)
    
    return df_procesado, df_original # Retornamos ambos dataframes