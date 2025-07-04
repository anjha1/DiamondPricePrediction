from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('artifacts/model.pkl', 'rb'))
preprocessor = pickle.load(open('artifacts/preprocessor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [
        float(request.form['carat']),
        request.form['cut'],
        request.form['color'],
        request.form['clarity'],
        float(request.form['depth']),
        float(request.form['table']),
        float(request.form['x']),
        float(request.form['y']),
        float(request.form['z'])
    ]

    columns = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
    df = pd.DataFrame([data], columns=columns)

    transformed_data = preprocessor.transform(df)
    prediction = model.predict(transformed_data)[0]
    prediction = round(prediction, 2)

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
