import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor

# Paso 1: Cargamos el dataset para poder trabajar con el
df = pd.read_csv('dataset_transporte_masivo.csv')

# Mostramos los primeros registros del dataset
print("Primeros 5 registros del dataset:")
print(df.head())

# Paso 2: Preprocesamos los datos
label_encoder = LabelEncoder()

# Convertir las columnas categóricas a numéricas
df['Origen'] = label_encoder.fit_transform(df['Origen'])
df['Destino'] = label_encoder.fit_transform(df['Destino'])
df['Transporte'] = label_encoder.fit_transform(df['Transporte'])
df['Clima'] = label_encoder.fit_transform(df['Clima'])

# Definir las características (X) y la variable objetivo (y)
X = df[['Hora', 'Origen', 'Destino', 'Transporte', 'Clima']]  # Características
y = df['Demora']  # Variable objetivo

# Paso 3: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Entrenar un modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)  # Entrenar el modelo

# Hacer predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Paso 5: Evaluar el modelo de regresión lineal
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Modelo de regresión lineal:\nError cuadrático medio: {mse}\nCoeficiente de determinación (R^2): {r2}")

# Paso 6: Entrenar un modelo de árbol de decisión
tree_model = DecisionTreeRegressor()
tree_model.fit(X_train, y_train)  # Entrenar el modelo

# Hacer predicciones con el árbol de decisión
y_pred_tree = tree_model.predict(X_test)

# Evaluar el árbol de decisión
mse_tree = mean_squared_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

print(f"\nModelo de árbol de decisión:\nError cuadrático medio: {mse_tree}\nCoeficiente de determinación (R^2): {r2_tree}")
