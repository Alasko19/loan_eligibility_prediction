from prediction import predict_loan_eligibility


applicant_data = {
    "Gender": "Male",
    "Married": "Yes",
    "Dependents": "0",
    "Education": "Graduate",
    "Self_Employed": "No",
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 2000,
    "LoanAmount": 120,
    "Loan_Amount_Term": 360,
    "Credit_History": 1.0,
    "Property_Area": "Urban"
}


models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest"
]


for model_name in models:

    result, probability = predict_loan_eligibility(
        applicant_data,
        model_name
    )

    print("\nModel:", model_name)
    print("Prediction:", result)
    print("Estimated Probability:", f"{probability:.2%}")