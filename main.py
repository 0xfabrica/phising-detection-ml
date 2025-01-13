import streamlit as st
import pandas as pd
from algoritmo_streamlit import cargar_datos, cargar_modelo, prediccion_manual, entrenar_modelo
from docs import mostrar_explicacion_inputs


# Cargar los datos y entrenar el modelo
datos = cargar_datos('data.csv')  # Asegúrate de proporcionar la ruta correcta al archivo CSV
entrenar_modelo(datos)

# Agregar la opción al sidebar
opcion = st.sidebar.selectbox("Selecciona una opción", [ "Predecir URL", "Documentación"])
if opcion == "Documentación":
    mostrar_explicacion_inputs()
elif opcion == "Predecir URL":
    # Código para la predicción de la URL
    pass


# Cargar el modelo y el scaler
modelo, scaler = cargar_modelo()

# Título de la aplicación
st.title('Detección de Phishing en URLs')

# Explicación
st.markdown("""
Este es un sistema de detección de phishing en URLs utilizando un modelo de Random Forest. Introduce una URL y las características de la misma para predecir si es phishing o no.
""")

# Entrada de características de la URL
st.sidebar.header("Introducir Características de la URL")
subdomain_level = st.sidebar.slider("Subdomain Level", min_value=0, max_value=5, value=2)
num_dots = st.sidebar.slider("Número de Puntos", min_value=1, max_value=10, value=3)
path_level = st.sidebar.slider("Path Level", min_value=0, max_value=5, value=1)
ip_address = st.sidebar.selectbox("¿Contiene IP en la URL?", ["Sí", "No"])
insecure_forms = st.sidebar.selectbox("¿Contiene formularios inseguros?", ["Sí", "No"])
pct_ext_hyperlinks = st.sidebar.slider("Porcentaje de Enlaces Externos", min_value=0, max_value=100, value=20)
num_sensitive_words = st.sidebar.slider("Número de Palabras Sensibles", min_value=0, max_value=10, value=2)
embedded_brand_name = st.sidebar.selectbox("¿Contiene Nombre de Marca Embebido?", ["Sí", "No"])

# Convertir respuestas a valores numéricos
ip_address = 1 if ip_address == "Sí" else 0
insecure_forms = 1 if insecure_forms == "Sí" else 0
embedded_brand_name = 1 if embedded_brand_name == "Sí" else 0

# Recolectar inputs
inputs = {
    'SubdomainLevel': subdomain_level,
    'NumDots': num_dots,
    'PathLevel': path_level,
    'IpAddress': ip_address,
    'InsecureForms': insecure_forms,
    'PctExtHyperlinks': pct_ext_hyperlinks,
    'NumSensitiveWords': num_sensitive_words,
    'EmbeddedBrandName': embedded_brand_name
}

# Realizar predicción
if st.button("Predecir"):
    resultado = prediccion_manual(modelo, scaler, inputs)
    
    if resultado == 1:
        st.error("¡La URL es phishing!")
    else:
        st.success("La URL es segura.")

