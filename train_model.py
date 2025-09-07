import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump
import os

# Load dataset
data = pd.read_csv("dataset.csv")
X = data['text']
y = data['label']

# Vectorize
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Create model directory if not exists
os.makedirs("model", exist_ok=True)

# Save model
dump(vectorizer, "model/vectorizer.joblib")
dump(model, "model/classifier.joblib")

print("✅ Model trained and saved to 'model/' folder")
