# 🌾 Crop Recommendation System

---

## 📌 Project Overview

This is a **Machine Learning based Web Application** that predicts the **Top 5 Best Crops** to cultivate based on **soil and weather conditions**.

It is built with:
- **Python**
- **Flask** (Backend Framework)
- **HTML & CSS** (Frontend)
- **Random Forest Classifier** (Machine Learning Model)

🌟 Features:
- Predict **Top 5 crop recommendations** with confidence percentages
- Beautiful dark-themed and fully responsive design
- About Us Page
- Feedback Form (User feedbacks are stored locally)

---

## 🚀 Tech Stack Used

| Category | Technology |
|:---|:---|
| Language | Python 3 |
| Libraries | Flask, scikit-learn, pandas, numpy, matplotlib, seaborn, joblib |
| Frontend | HTML5, CSS3 |
| Machine Learning Model | Random Forest Classifier |

---

## 🏗 Project Structure

```bash
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
│   └── label_encoder.pkl               # Label Encoder for crops
│
├── feedbacks.txt            # Stores user feedbacks
└── screenshots/             # (Optional) Screenshots for README
```


⚙️ How to Set Up Locally
1. Clone the Repository
```bash
Copy
Edit
git clone <repository-link>
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
(Or use the provided .pkl files inside the model/ folder.)

4. Run the Flask app
bash
Copy
Edit
python app.py
Server will start at:

http://127.0.0.1:5000/
```

✨ Future Enhancements
Add User Login/Signup

Admin Panel to View Feedbacks

Save feedbacks into database (instead of text file)

Deploy application publicly (Render / Railway)

Add more weather parameters (wind speed, sunshine hours)

🙏 Acknowledgements
Dataset: Crop Recommendation Dataset (open source)

Libraries: Flask, scikit-learn, pandas, numpy, seaborn

Developer: Chirag Avasthi


