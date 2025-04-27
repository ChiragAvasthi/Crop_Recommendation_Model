from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model and encoder
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

        # Predict probabilities
        probabilities = model.predict_proba(final_features)[0]

        # Get Top 5 Crops
        top_indices = np.argsort(probabilities)[::-1][:5]
        top_crops = label_encoder.inverse_transform(top_indices)
        top_probs = probabilities[top_indices]

        results = list(zip(top_crops, (top_probs * 100).round(2)))

        return render_template('result.html', results=results)

    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback_text = request.form['feedback']
        with open('feedbacks.txt', 'a') as f:
            f.write(feedback_text + '\n')
        return "Thank you for your feedback!"
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
