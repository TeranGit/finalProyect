from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import numpy as np
import h5py
import os

app = Flask(__name__)

# Especificar la ruta del modelo utilizando una cadena de bytes
model_path = os.fsdecode(b'my_model.h5')

# Cargar el modelo
with h5py.File(model_path, 'r') as f:
    loaded_model = tf.keras.models.load_model(f)

# Ruta de inicio para renderizar un formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos de entrada de la solicitud POST
        data = request.form

        # Crear un DataFrame con los datos de entrada
        input_data = pd.DataFrame({
            'age': [int(data['age'])],
            'fnlwgt': [int(data['fnlwgt'])],
            'education.num': [int(data['education.num'])],
            # Añadir más columnas según las características de tu modelo
        })

        # Realizar preprocesamiento similar al que hiciste en el modelo original
        scaler = StandardScaler()
        input_scaled = scaler.fit_transform(input_data)

        # Realizar la predicción
        prediction_prob = loaded_model.predict(input_scaled)
        prediction_label = np.argmax(prediction_prob)  # Obtener el índice del valor máximo

        # Mapear el índice de la clase a la etiqueta original
        if prediction_label == 0:
            prediction = '<=50K'
        else:
            prediction = '>50K'

        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
