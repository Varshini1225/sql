from joblib import load

vectorizer = load("model/vectorizer.joblib")
model = load("model/classifier.joblib")

def classify_response(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    score = model.predict_proba(vec)[0][1]

    print(f"[AI] Prediction: {'SQLi' if prediction else 'Safe'} | Confidence: {score:.2f}")
    return prediction == 1
