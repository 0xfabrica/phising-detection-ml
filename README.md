# Proyecto de Detección de URLs Maliciosas con Machine Learning

Este proyecto tiene como objetivo desarrollar un modelo de machine learning para detectar URLs maliciosas (spam o phishing), utilizando un dataset  ('dataa.csv'). Se implementan dos modelos: RandomForestClassifier y XGBoost, para ofrecer una solución robusta y precisa.


## Descripción del Proyecto

El sistema está diseñado para identificar posibles URLs maliciosas analizando múltiples características, como:
- Nivel del subdominio.
- Longitud de la URL.
- Presencia de ciertos caracteres, como '@', '~', '_', '%'.
- Uso de iframes o frames.
- Títulos faltantes en la página.
- Entre otras.


## Dataset

Se utiliza un conjunto de datos ('dataa.csv') que contiene características de URLs. La columna 'CLASS_LABEL' indica si una URL es maliciosa (1.0) o benigna (0.0).


## Algoritmos y Resultados

Se implementan dos modelos de Machine Learning para la clasificación:

1. **RandomForest Classifier:** Un modelo de conjunto basado en árboles de decisión.
2. **XGBoost:** Un algoritmo de boosting de gradiente conocido por su alto rendimiento.

**Resultados:**

*   **RandomForest:** Obtiene una precisión aceptable, pero XGBoost muestra un rendimiento ligeramente superior, especialmente en la detección de URLs maliciosas (clase 1.0).
*   **XGBoost:** Se guarda el modelo entrenado en un archivo 'modelo_xgboost.json' para su uso posterior.

**Métricas:**

Se evalúan los modelos utilizando métricas como la precisión (accuracy), la matriz de confusión y el informe de clasificación. Puedes consultar el código para ver los resultados detallados de cada modelo.

**Matriz de confusión (Ejemplo - XGBoost):**
  - Verdaderos Negativos (VN): 1354
  - Verdaderos Positivos (VP): 1453
  - Falsos Positivos (FP): 109
  - Falsos Negativos (FN): 84

Asegúrate de tener instalado lo siguiente en tu entorno:

- Python 3.8 o superior
- Librerías: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn.

Puedes instalar las librerías necesarias ejecutando el siguiente comando en tu entorno de Colab:
```
bash !pip install pandas numpy scikit-learn xgboost matplotlib seaborn
```
