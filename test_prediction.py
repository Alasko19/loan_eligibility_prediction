from prediction import predict_loan_eligibility

sample_applicant = {
    "Gender": "Male",
    "Married": "Yes",
    "Dependents": 0,
    "Education": "Graduate",
    "Self_Employed": "No",
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 0,
    "LoanAmount": 150,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area": "Urban"
}


result = predict_loan_eligibility(sample_applicant)

print("Loan Eligibility Prediction:", result)