import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
data = pd.read_csv('Crop_recommendation.csv')

# Check first few rows
print(data.head())

# Check info
print(data.info())

# Check missing values
print(data.isnull().sum())

# Visualize distributions
data.hist(figsize=(12,10))
plt.show()

# Label encoding target variable
le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])

# Train-test split
X = data.drop('label', axis=1)
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train Random Forest Classifier
rf = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42, class_weight='balanced')
rf.fit(X_train, y_train)

# Predictions and evaluation
y_pred = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save the model and label encoder
joblib.dump(rf, 'crop_recommendation_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
