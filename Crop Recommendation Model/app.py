from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('model/crop_recommendation_model.pkl')
label_encoder = joblib.load('model/label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)
        crop_name = label_encoder.inverse_transform(prediction)[0]
        return render_template('result.html', crop=crop_name)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
