import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import joblib
import warnings
warnings.filterwarnings('ignore')



# Función para cargar y procesar los datos
def cargar_datos(filepath):
    df = pd.read_csv(filepath)
    df.drop(['id'], axis=1, inplace=True)
    return df

# Función para mostrar el mapa de calor de correlaciones
def corr_heatmap(data, idx_s, idx_e):
    y = data['CLASS_LABEL']
    temp = data.iloc[:, idx_s:idx_e]
    temp['CLASS_LABEL'] = y
    plt.figure(figsize=(10, 8))
    sns.heatmap(temp.corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title("Mapa de Calor de Correlaciones")
    plt.show()

# Función para entrenar el modelo
def entrenar_modelo(datos):
    """
    Entrena un modelo Random Forest y guarda el modelo y el scaler.
    """
    X = datos[['SubdomainLevel', 'NumDots', 'PathLevel', 'IpAddress', 'InsecureForms', 
               'PctExtHyperlinks', 'NumSensitiveWords', 'EmbeddedBrandName']]
    y = datos['CLASS_LABEL']

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Escalar los datos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Entrenar el modelo
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train_scaled, y_train)

    # Guardar el modelo y el scaler
    joblib.dump(modelo, "modelo_entrenado.pkl")
    joblib.dump(scaler, "scaler.pkl")

    # Evaluar el modelo
    y_pred = modelo.predict(X_test_scaled)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "classification_report": classification_report(y_test, y_pred, output_dict=True)
    }

    return metrics

# Función para cargar el modelo preentrenado
def cargar_modelo():
    modelo = joblib.load("modelo_entrenado.pkl")
    scaler = joblib.load("scaler.pkl")
    return modelo, scaler

# Función para realizar predicciones
def prediccion_manual(modelo, scaler, inputs):
    """
    Realiza una predicción basada en los datos ingresados manualmente.
    """
    datos = pd.DataFrame([inputs])
    datos_scaled = scaler.transform(datos)
    return modelo.predict(datos_scaled)[0]
