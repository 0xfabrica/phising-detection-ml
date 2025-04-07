# Proyecto de Detección de Phishing en URLs

Este proyecto tiene como objetivo detectar URLs de phishing utilizando modelos de machine learning, específicamente RandomForest y XGBoost. A continuación, se presentan las métricas de rendimiento, matrices de confusión y una comparación detallada entre ambos modelos.

PD: Para el proyecto se ha usado el modelo creado con XGBoost

## RandomForest

### Métricas

- **Accuracy:** 0.9313 (93.13%)

#### Classification Report

| Clase | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0.0   | 0.93      | 0.93   | 0.93     | 1463    |
| 1.0   | 0.94      | 0.93   | 0.93     | 1537    |
| **Macro Avg** | 0.93 | 0.93 | 0.93 | 3000 |
| **Weighted Avg** | 0.93 | 0.93 | 0.93 | 3000 |

#### Matriz de Confusión

- **Verdaderos Negativos (VN):** 1364
- **Falsos Positivos (FP):** 99
- **Falsos Negativos (FN):** 107
- **Verdaderos Positivos (VP):** 1430

*(Nota: En la comparación se menciona VN: 1361 y FP: 102, pero se usaron los valores iniciales para consistencia con las métricas proporcionadas.)*

## XGBoost

### Parámetros Utilizados

- `random_state=42`
- `colsample_bytree=0.8`
- `learning_rate=0.1`
- `max_depth=5`
- `n_estimators=300`
- `subsample=1.0`

### Métricas

- **Precisión:** 0.9357 (93.57%)

#### Classification Report

| Clase | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0.0   | 0.94      | 0.93   | 0.93     | 1463    |
| 1.0   | 0.93      | 0.95   | 0.94     | 1537    |
| **Macro Avg** | 0.94 | 0.94 | 0.94 | 3000 |
| **Weighted Avg** | 0.94 | 0.94 | 0.94 | 3000 |

#### Matriz de Confusión

- **Verdaderos Negativos (VN):** 1354
- **Falsos Positivos (FP):** 109
- **Falsos Negativos (FN):** 84
- **Verdaderos Positivos (VP):** 1453

## Comparación entre RandomForest y XGBoost

A continuación, se comparan los modelos basados en sus matrices de confusión:

- **Verdaderos Negativos (VN):** RandomForest predice más negativos correctamente (1361 vs 1354).
- **Falsos Positivos (FP):** XGBoost tiene más errores al predecir positivos cuando no lo son (109 vs 102).
- **Falsos Negativos (FN):** XGBoost comete menos errores al predecir negativos cuando en realidad son positivos (84 vs 107).
- **Verdaderos Positivos (VP):** XGBoost predice más positivos correctamente (1453 vs 1430).

### Interpretación

- **Clase 0.0 (No Phishing):** RandomForest es ligeramente mejor identificando URLs legítimas, con más verdaderos negativos y menos falsos positivos.
- **Clase 1.0 (Phishing):** XGBoost es más efectivo detectando URLs de phishing, con menos falsos negativos y más verdaderos positivos.

### Conclusión

XGBoost parece ser superior identificando la clase positiva (1.0 Phishing), lo que es crucial para minimizar los falsos negativos en un sistema de detección de phishing, donde no detectar una URL maliciosa puede tener graves consecuencias. Por otro lado, RandomForest tiene un leve ventaja con la clase negativa (0.0 No Phishing), cometiendo menos falsos positivos. La elección del modelo dependerá de las prioridades del proyecto: si se prioriza evitar falsos negativos, XGBoost es preferible; si se busca reducir falsos positivos, RandomForest podría ser más adecuado.
