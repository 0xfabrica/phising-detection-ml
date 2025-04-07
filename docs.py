import streamlit as st
import importlib

def mostrar_explicacion_inputs():
    # Add padding using empty space
    st.empty()
    st.write("")  # This adds a blank line
    
    # Título principal
    st.title("📊 Detección de Phishing en URLs")

    # Índice interactivo
    st.sidebar.header("Índice")
    st.sidebar.markdown("""
    - [Introducción](#introduccion)
    - [Explicación de Inputs](#explicacion-de-inputs)
    - [Algoritmo Usado](#algoritmo-usado)
    - [Precisión del Modelo](#precision-del-modelo)
    - [Informe del Modelo](#informe-del-modelo)
    """)

    # Secciones del documento
    st.container()
    with st.container():
        st.header("🚀 Introducción", anchor="introduccion")
        st.write("""
        Este documento detalla el desarrollo de un sistema de detección de phishing en URLs utilizando un modelo de machine learning basado en **XGBoost**. 
        El objetivo es identificar si una URL es potencialmente maliciosa (phishing) o legítima, analizando diversas características extraídas de la URL y su estructura. 
        Este sistema ha sido implementado en **Streamlit** para facilitar su uso mediante una interfaz interactiva. A continuación, se explican las características utilizadas, 
        el modelo entrenado, sus métricas de rendimiento y una interpretación de los resultados.
        """)

    st.container()
    with st.container():
        st.header("🛠 Explicación de Inputs (Características Utilizadas)", anchor="explicacion-de-inputs")
        st.write("""
        El modelo fue entrenado con un conjunto de 19 características extraídas de las URLs, seleccionadas cuidadosamente para capturar patrones asociados con phishing. 
        A continuación, se describe cada una de ellas:
        
        - **NumDots**: Número de puntos (`.`) en la URL. Las URLs de phishing suelen tener más subdominios o puntos para parecer legítimas.
        - **SubdomainLevel**: Nivel de subdominios en la URL (e.g., `sub1.sub2.dominio.com` tiene un nivel de 2). Un nivel alto puede ser sospechoso.
        - **PathLevel**: Profundidad del path en la URL (e.g., `/ruta1/ruta2/` tiene nivel 2). Los paths largos pueden indicar intentos de ocultar contenido malicioso.
        - **UrlLength**: Longitud total de la URL. Las URLs de phishing tienden a ser más largas para incluir parámetros o redirecciones.
        - **NumDash**: Número de guiones (`-`) en la URL. Los guiones son comunes en URLs maliciosas para imitar nombres de dominio legítimos.
        - **NumDashInHostname**: Número de guiones específicamente en el hostname. Un hostname con muchos guiones puede ser un indicador de phishing.
        - **AtSymbol**: Presencia del símbolo `@` en la URL (1 si está, 0 si no). Este símbolo puede usarse para engañar al usuario redirigiendo a otro dominio.
        - **TildeSymbol**: Presencia del símbolo `~` (1 si está, 0 si no). Es raro en URLs legítimas, pero puede aparecer en phishing.
        - **NumUnderscore**: Número de guiones bajos (`_`) en la URL. Similar a los guiones, un uso excesivo puede ser sospechoso.
        - **NumPercent**: Número de símbolos de porcentaje (`%`), usados en codificación URL. Un número alto puede indicar intentos de ocultar contenido.
        - **IframeOrFrame**: Presencia de etiquetas `<iframe>` o `<frame>` en el contenido vinculado a la URL (1 si está, 0 si no). Estas etiquetas son comunes en ataques de phishing.
        - **MissingTitle**: Indica si la página asociada a la URL carece de título (1 si falta, 0 si no). Las páginas de phishing suelen omitir metadatos básicos.
        - **ImagesOnlyInForm**: Indica si los formularios de la página contienen solo imágenes (1 si es cierto, 0 si no). Esto puede ser un intento de ocultar formularios maliciosos.
        - **SubdomainLevelRT**: Resultado de un análisis de riesgo del nivel de subdominio (valor codificado, e.g., -1, 0, 1). Un valor más negativo indica mayor riesgo.
        - **UrlLengthRT**: Resultado de un análisis de riesgo basado en la longitud de la URL (e.g., -1, 0, 1). URLs muy largas suelen tener un valor de riesgo más negativo.
        - **PctExtResourceUrlsRT**: Porcentaje de URLs de recursos externos (e.g., scripts, imágenes) con análisis de riesgo (valor codificado). Un valor alto puede indicar contenido sospechoso.
        - **AbnormalExtFormActionR**: Indica si las acciones de formularios externos son anormales (valor codificado, e.g., -1, 0, 1). Las acciones inusuales suelen estar asociadas con phishing.
        - **ExtMetaScriptLinkRT**: Análisis de riesgo de scripts, metadatos y enlaces externos (valor codificado). Un valor más negativo indica mayor probabilidad de phishing.
        - **PctExtNullSelfRedirectHyperlinksRT**: Porcentaje de hipervínculos que redirigen a sí mismos o son nulos, con análisis de riesgo (valor codificado). Un valor alto puede ser un indicador de phishing.
        - **CLASS_LABEL (Variable objetivo)**: Etiqueta objetivo del modelo, donde `1.0` indica una URL de phishing (positiva) y `0.0` indica una URL legítima (negativa).
        """)

    st.container()
    with st.container():
        st.header("🌳 Algoritmo Usado: XGBoost", anchor="algoritmo-usado")
        st.write("""
        El modelo implementado es **XGBoost (Extreme Gradient Boosting)**, un algoritmo de aprendizaje automático basado en árboles de decisión que utiliza el boosting para mejorar el rendimiento. 
        Fue elegido por las siguientes razones:
        - Alta capacidad para manejar datos numéricos y categóricos.
        - Robustez frente al sobreajuste gracias a parámetros de regularización.
        - Excelente rendimiento en tareas de clasificación binaria, como la detección de phishing.
        
        ### Parámetros del Modelo
        El modelo se entrenó con los siguientes hiperparámetros:
        - `random_state=42`: Semilla para reproducibilidad.
        - `colsample_bytree=0.8`: Proporción de características (columnas) muestreadas para construir cada árbol (80%).
        - `learning_rate=0.1`: Tasa de aprendizaje para controlar la contribución de cada árbol.
        - `max_depth=5`: Profundidad máxima de cada árbol, para evitar sobreajuste.
        - `n_estimators=300`: Número de árboles en el ensamblado.
        - `subsample=1.0`: Proporción de muestras usadas para entrenar cada árbol (100%, sin submuestreo).
        """)

    st.container()
    with st.container():
        st.header("📈 Precisión del Modelo", anchor="precision-del-modelo")
        st.write("""
        El modelo alcanzó las siguientes métricas en un conjunto de prueba de 3000 instancias:
        
        - **Precisión global (Accuracy)**: 0.9357 (93.57%), lo que indica un alto rendimiento en la clasificación de URLs.
        """)

    st.container()
    with st.container():
        st.header("📋 Informe del Modelo", anchor="informe-del-modelo")
        st.write("""
        ### Informe de Clasificación
        | Clase       | Precision | Recall | F1-Score | Support |
        |-------------|-----------|--------|----------|---------|
        | **0.0 (No Phishing)** | 0.94      | 0.93   | 0.93     | 1463    |
        | **1.0 (Phishing)**    | 0.93      | 0.95   | 0.94     | 1537    |
        | **Macro Avg**         | 0.94      | 0.94   | 0.94     | 3000    |
        | **Weighted Avg**      | 0.94      | 0.94   | 0.94     | 3000    |
        
        ### Matriz de Confusión
        La matriz de confusión (visualizada en la imagen) es la siguiente:
        - **Verdaderos Negativos (VN)**: 1354 (URLs legítimas correctamente clasificadas como no phishing).
        - **Falsos Positivos (FP)**: 109 (URLs legítimas clasificadas incorrectamente como phishing).
        - **Falsos Negativos (FN)**: 84 (URLs de phishing clasificadas incorrectamente como legítimas).
        - **Verdaderos Positivos (VP)**: 1453 (URLs de phishing correctamente clasificadas).
        
        #### Interpretación de Resultados
        - **Clase 0.0 (No Phishing)**: El modelo tiene una precisión de 0.94 y un recall de 0.93, lo que indica que identifica bien las URLs legítimas, pero comete 109 falsos positivos.
        - **Clase 1.0 (Phishing)**: Con un recall de 0.95, el modelo es muy efectivo detectando URLs de phishing, con solo 84 falsos negativos. Esto es crucial en un sistema de detección de phishing, ya que los falsos negativos (URLs maliciosas no detectadas) son más peligrosos que los falsos positivos.
        - **Comparación con RandomForest (contexto adicional)**: Aunque en un análisis previo se comparó con un modelo RandomForest (VN: 1361, FP: 102, FN: 107, VP: 1430), XGBoost muestra mejor capacidad para detectar la clase positiva (phishing), con menos falsos negativos (84 vs 107) y más verdaderos positivos (1453 vs 1430). Sin embargo, RandomForest tiene menos falsos positivos (102 vs 109).
        """)

    # Estilo adicional para ajustar contenido
    st.markdown("""
    <style>
    .block-container {
        padding-top: 20px;
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
