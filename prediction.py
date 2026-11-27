import joblib
import pandas as pd
from pathlib import Path

# model directory

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "saved_models"

# available model

MODEL_PATHS = {
    "Logistic Regression": (
        MODEL_DIR / "logistic_regression.pkl"
    ),

    "Decision Tree": (
        MODEL_DIR / "decision_tree.pkl"
    ),

    "Random Forest": (
        MODEL_DIR / "random_forest.pkl"
    )
}


# loading selected model

def load_model(model_name):

    if model_name not in MODEL_PATHS:
        raise ValueError(
            f"Unknown model selected: {model_name}"
        )

    model_path = MODEL_PATHS[model_name]

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}"
        )

    return joblib.load(model_path)


# predicting loan eligibility

def predict_loan_eligibility(
    applicant_data,
    model_name="Random Forest"
):

    # Loading the user's selected model
    model = load_model(model_name)

    # Converting applicant information into a DataFrame
    input_data = pd.DataFrame([applicant_data])

    # Converting Dependents into numeric format
    input_data["Dependents"] = (
        input_data["Dependents"]
        .replace("3+", "3")
    )

    input_data["Dependents"] = pd.to_numeric(
        input_data["Dependents"],
        errors="coerce"
    )

    # Generating prediction
    prediction = model.predict(input_data)[0]

    # Generating prediction probabilities
    probabilities = model.predict_proba(input_data)[0]

    # Getting probability for the predicted class
    predicted_index = list(model.classes_).index(
        prediction
    )

    probability = probabilities[predicted_index]

    # Converting prediction into readable result
    result = (
        "Eligible"
        if prediction == 1
        else "Not Eligible"
    )

    return result, probability