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

    # Convert Dependents to the numeric format
    # used when training the original model.

    input_data["Dependents"] = (
        input_data["Dependents"]
        .replace("3+", "3")
    )

    input_data["Dependents"] = pd.to_numeric(
        input_data["Dependents"],
        errors="coerce"
    )

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    predicted_index = list(model.classes_).index(prediction)

    probability = probabilities[predicted_index]

    result = "Eligible" if prediction == 1 else "Not Eligible"

    return result, probability