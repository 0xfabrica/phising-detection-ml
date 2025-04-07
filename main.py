import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
from docs import mostrar_explicacion_inputs

# Agregar la opción al sidebar
opcion = st.sidebar.selectbox("Selecciona una opción", ["Predecir URL", "Documentación"])
if opcion == "Documentación":
    mostrar_explicacion_inputs()
elif opcion == "Predecir URL":
    # Código para la predicción de la URL
    pass

path = 'modelo_xgboost.json'
modelo = xgb.XGBClassifier()
modelo.load_model(path)

# Título de la aplicación
st.title('Detección de Phishing en URLs')

# Explicación
st.markdown("""
Este es un sistema de detección de phishing en URLs utilizando un modelo de Random Forest. Introduce una URL y las características de la misma para predecir si es phishing o no.
""")

# Entrada de características de la URL
st.sidebar.header("Introducir Características de la URL")

num_dots = st.sidebar.slider("Número de Puntos en URL", min_value=0, max_value=10, value=3)
subdomain_level = st.sidebar.slider("Nivel de Subdominios", min_value=0, max_value=5, value=2)
path_level = st.sidebar.slider("Nivel de Ruta", min_value=0, max_value=10, value=2)
url_length = st.sidebar.slider("Longitud de URL", min_value=0, max_value=500, value=100)
num_dash = st.sidebar.slider("Número de Guiones", min_value=0, max_value=20, value=0)
num_dash_hostname = st.sidebar.slider("Número de Guiones en Hostname", min_value=0, max_value=10, value=0)
at_symbol = st.sidebar.selectbox("¿Contiene Símbolo @?", ["Sí", "No"])
tilde_symbol = st.sidebar.selectbox("¿Contiene Símbolo ~?", ["Sí", "No"])
num_underscore = st.sidebar.slider("Número de Guiones Bajos", min_value=0, max_value=20, value=0)
num_percent = st.sidebar.slider("Número de Símbolos %", min_value=0, max_value=20, value=0)
iframe_or_frame = st.sidebar.selectbox("¿Contiene iframe o frame?", ["Sí", "No"])
missing_title = st.sidebar.selectbox("¿Falta el título?", ["Sí", "No"])
images_only_in_form = st.sidebar.selectbox("¿Solo imágenes en formulario?", ["Sí", "No"])
subdomain_level_rt = st.sidebar.slider("Ratio de Nivel de Subdominios", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
url_length_rt = st.sidebar.slider("Ratio de Longitud URL", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
pct_ext_resource_urls_rt = st.sidebar.slider("% URLs Recursos Externos", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
abnormal_ext_form_action_r = st.sidebar.selectbox("¿Acción de Formulario Externa Anormal?", ["Sí", "No"])
ext_meta_script_link_rt = st.sidebar.slider("Ratio Meta Script Links Externos", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
pct_ext_null_self_redirect_hyperlinks_rt = st.sidebar.slider("% Enlaces Nulos/Redirección", min_value=0.0, max_value=1.0, value=0.0, step=0.1)

# Convertir respuestas Sí/No a valores numéricos
at_symbol = 1 if at_symbol == "Sí" else 0
tilde_symbol = 1 if tilde_symbol == "Sí" else 0
iframe_or_frame = 1 if iframe_or_frame == "Sí" else 0
missing_title = 1 if missing_title == "Sí" else 0
images_only_in_form = 1 if images_only_in_form == "Sí" else 0
abnormal_ext_form_action_r = 1 if abnormal_ext_form_action_r == "Sí" else 0

# Actualizar el diccionario de inputs
inputs = {
    'NumDots': num_dots,
    'SubdomainLevel': subdomain_level,
    'PathLevel': path_level,
    'UrlLength': url_length,
    'NumDash': num_dash,
    'NumDashInHostname': num_dash_hostname,
    'AtSymbol': at_symbol,
    'TildeSymbol': tilde_symbol,
    'NumUnderscore': num_underscore,
    'NumPercent': num_percent,
    'IframeOrFrame': iframe_or_frame,
    'MissingTitle': missing_title,
    'ImagesOnlyInForm': images_only_in_form,
    'SubdomainLevelRT': subdomain_level_rt,
    'UrlLengthRT': url_length_rt,
    'PctExtResourceUrlsRT': pct_ext_resource_urls_rt,
    'AbnormalExtFormActionR': abnormal_ext_form_action_r,
    'ExtMetaScriptLinkRT': ext_meta_script_link_rt,
    'PctExtNullSelfRedirectHyperlinksRT': pct_ext_null_self_redirect_hyperlinks_rt
}

def realizar_prediccion(modelo, inputs):
    # Convertir el diccionario de inputs a DataFrame
    df = pd.DataFrame([inputs])
    
    # Asegurar el orden correcto de las columnas
    columnas_esperadas = [
        'NumDots', 'SubdomainLevel', 'PathLevel', 'UrlLength', 'NumDash',
        'NumDashInHostname', 'AtSymbol', 'TildeSymbol', 'NumUnderscore',
        'NumPercent', 'IframeOrFrame', 'MissingTitle', 'ImagesOnlyInForm',
        'SubdomainLevelRT', 'UrlLengthRT', 'PctExtResourceUrlsRT',
        'AbnormalExtFormActionR', 'ExtMetaScriptLinkRT',
        'PctExtNullSelfRedirectHyperlinksRT'
    ]
    
    df = df[columnas_esperadas]
    
    # Realizar predicción
    try:
        prediccion = modelo.predict(df)[0]
        probabilidad = modelo.predict_proba(df)[0]
        return prediccion, probabilidad
    except Exception as e:
        st.error(f"Error en la predicción: {str(e)}")
        return None, None

# Realizar predicción
if st.button("Predecir"):
    prediccion, probabilidad = realizar_prediccion(modelo, inputs)
    
    if prediccion is not None:
        if prediccion == 1:
            st.error("⚠️ ¡ALERTA! Esta URL es probablemente phishing!")
            st.warning(f"Probabilidad de ser phishing: {probabilidad[1]:.2%}")
        else:
            st.success("✅ Esta URL parece segura")
            st.info(f"Probabilidad de ser legítima: {probabilidad[0]:.2%}")
        
        # Mostrar detalles adicionales
        with st.expander("Ver detalles del análisis"):
            st.write("Valores analizados:", inputs)
            st.write("Probabilidades:", {
                "Legítimo": f"{probabilidad[0]:.2%}",
                "Phishing": f"{probabilidad[1]:.2%}"
            })

