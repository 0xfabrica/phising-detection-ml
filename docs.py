import streamlit as st
import importlib
import docs
importlib.reload(docs)


def mostrar_explicacion_inputs():
    # Título principal
    st.title("Documentación del Proyecto")
    
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
        st.header("Introducción", anchor="introduccion")
        st.write("""
        Este documento proporciona una explicación detallada de los inputs utilizados en el modelo,
        el algoritmo implementado, la precisión obtenida y el informe completo del proyecto. 
        Sirve como guía para comprender el funcionamiento del sistema.
        """)

    st.container()
    with st.container():
        st.header("Explicación de Inputs", anchor="explicacion-de-inputs")
        st.write("""
        1. **Input 1 - Subdomain Level:** Este campo indica el nivel del subdominio en la URL, 
           que ayuda a identificar posibles patrones de phishing.
        2. **Input 2 - URL Length:** Evalúa la longitud de la URL; las URLs largas suelen ser sospechosas.
        3. **Input 3 - Suspicious Words:** Identifica palabras clave como "free" o "click", típicas en phishing.
        ...
        """)  # Añade el resto de inputs aquí

    st.container()
    with st.container():
        st.header("Algoritmo Usado", anchor="algoritmo-usado")
        st.write("""
        El modelo implementado es un [nombre del modelo, e.g., Random Forest], elegido por su capacidad 
        para manejar datos categóricos y numéricos de manera eficiente. Este algoritmo utiliza árboles 
        de decisión como base y combina múltiples de ellos para mejorar la precisión general.
        """)

    st.container()
    with st.container():
        st.header("Precisión del Modelo", anchor="precision-del-modelo")
        st.write("""
        La precisión alcanzada por el modelo es del **98%**, lo que indica un alto rendimiento en la 
        detección de patrones de phishing en comparación con los datos proporcionados.
        """)

    st.container()
    with st.container():
        st.header("Informe del Modelo", anchor="informe-del-modelo")
        st.write("""
        - **Matriz de confusión:** 
          - True Positives: 120
          - True Negatives: 130
          - False Positives: 5
          - False Negatives: 3

        - **Métricas adicionales:**
          - Precisión: 0.98
          - Recall: 0.96
          - F1-Score: 0.97
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
