import joblib
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR
    / "saved_models"
    / "best_loan_eligibility_model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict_loan_eligibility(applicant_data):

    input_data = pd.DataFrame([applicant_data])

    prediction = model.predict(input_data)[0]

    # Get estimated probabilities for both classes
    probabilities = model.predict_proba(input_data)[0]

    # Find the probability corresponding to the predicted class
    predicted_index = list(model.classes_).index(prediction)

    probability = probabilities[predicted_index]

    if prediction == 1:
        result = "Eligible"
    else:
        result = "Not Eligible"

    return result, probability