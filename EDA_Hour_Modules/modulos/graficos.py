# Librerías necesarias
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def hacer_grafico(df):
    """
    Genera una cuadrícula de histogramas para analizar la distribución de las variables numéricas del dataset.
    
    :param df: Description

    :return: fig - Objeto de figura de Matplotlib con los histogramas generados.
    """
    #Genera una cuadrícula de histogramas para analizar la distribución de las variables numéricas del dataset.
    
    # Definición de las columnas de interés (variables temporales, climáticas y conteos)
    num_cols = ["season", "mnth", "hr", "weekday", "holiday", "weathersit", "windspeed", "casual", "registered", "cnt"]
    
    # Creamos una malla de 5 filas y 2 columnas (10 gráficos en total)
    fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(16, 40))
    # Aplanamos la matriz de axes para iterar sobre ella fácilmente con un solo índice
    axes = axes.flatten()

    for i, col in enumerate(num_cols):
        # Histograma con KDE (curva de estimación de densidad de kernel) para ver la forma de la distribución
        sns.histplot(df[col], kde=True, ax=axes[i], color='skyblue', edgecolor='black')
        
        # Configuración estética del título de cada subgráfico
        axes[i].set_title(f"Distribución de {col}", 
                          fontsize=18, 
                          fontweight='bold', 
                          loc='center', 
                          y=1.1) 
    
    # Ajuste manual de espacios para evitar que los títulos se encimen con los ejes
    plt.subplots_adjust(left=0.1,
                        right=0.9, 
                        top=0.96, 
                        bottom=0.04, 
                        hspace=1.5, # Espacio vertical entre gráficos
                        wspace=0.4) 
    
    return fig

def grafico_matriz_confusion(y_real, y_predicho, clases=None, titulo="Matriz de confusión Regresión Logística"):
    """
    Genera una representación visual de la matriz de confusión para evaluar la precisión de la clasificación.
    :param y_real: Valores reales del conjunto de prueba.
    :param y_predicho: Predicciones del modelo.
    :param clases: Lista de nombres de las clases para etiquetar los ejes.
    :param titulo: Título del gráfico.
    :return: disp - Objeto de visualización de la matriz de confusión.
    """
    #Crea una representación visual de la matriz de confusión para evaluar la precisión de la clasificación.
    # Cálculo de la matriz comparando valores reales vs. predicciones
    cm = confusion_matrix(y_real, y_predicho)
    
    # Usamos el objeto de scikit-learn que facilita la visualización
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clases)
    
    # Renderizado con mapa de colores azul
    disp.plot(cmap="Blues")
    
    # Personalización del título
    plt.title(titulo, fontsize=16, fontweight='bold')

    return disp