🌾 Crop Recommendation System
📌 Project Overview
This is a Machine Learning based Web Application that predicts the Top 5 Best Crops to cultivate based on soil and weather parameters.
The project is built with:

Python

Flask (Backend Web Framework)

HTML, CSS (Frontend)

Machine Learning (Random Forest Classifier)

🌟 Features:

Predict Top 5 recommended crops with confidence percentage

About Us Page

Feedback Form for users

Fully responsive, stylish high-contrast design

Feedbacks are saved locally

🚀 Tech Stack Used

Category	Technology
Language	Python 3
Libraries	Flask, scikit-learn, pandas, numpy, matplotlib, seaborn, joblib
Frontend	HTML5, CSS3
ML Model	Random Forest Classifier
🏗 Project Structure
bash
Copy
Edit
crop-recommendation/
│
├── app.py                  # Main Flask application
├── train_model.py           # ML model training script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
│
├── static/
│   └── css/
│       └── style.css        # Custom styling
│
├── templates/
│   ├── index.html           # Home page (input form)
│   ├── result.html          # Top 5 crop suggestions
│   ├── about.html           # About Us page
│   └── feedback.html        # Feedback form
│
├── model/
│   ├── crop_recommendation_model.pkl   # Trained Random Forest model
│   └── label_encoder.pkl               # Label Encoder for crop names
│
├── feedbacks.txt            # Stores user feedbacks
⚙️ How to Set Up Locally
1. Clone the repository
bash
Copy
Edit
git clone <repository-url>
cd crop-recommendation
2. Install all required packages
bash
Copy
Edit
pip install -r requirements.txt
3. Train the model (optional)
If model files are not available:

bash
Copy
Edit
python train_model.py
(Or directly use provided .pkl files inside model/ folder)

4. Run the Flask app
bash
Copy
Edit
python app.py
Flask server will start at:

http://127.0.0.1:5000/

🖥 How to Use
Go to Home page

Fill the form with:

Nitrogen, Phosphorus, Potassium values

Temperature, Humidity

Soil pH level

Rainfall amount

Click "Predict Crop"

Get Top 5 Crop Recommendations with confidence levels.

Visit "About Us" and "Give Feedback" pages if you want!

✨ Future Enhancements (Optional Ideas)
User Authentication (Login/Signup)

Admin Panel to read user feedbacks

Store feedbacks into database

Email notification on feedback submission

Deploy project publicly (Render / Railway)

🙏 Acknowledgements
Dataset: Crop Recommendation Dataset (open source)

Libraries: scikit-learn, Flask, pandas, numpy

Developer: Chirag Avasthi

"Plant the right seed, reap a smarter harvest! 🌾🌟"

