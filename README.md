Loan Eligibility Prediction Using Python

Project Overview

This project uses machine learning to predict whether a loan application is likely to be approved or rejected based on applicant information.

The project uses the Loan Prediction Problem dataset from Kaggle.

Dataset

Source: Kaggle - Loan Prediction Problem Dataset

The dataset contains:

* 614 labelled training records.
* 367 test records.
* Applicant information such as income, education, employment status, credit history, and property area.

Technologies and Libraries

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

Project Workflow

1. Data loading and inspection.
2. Exploratory data analysis.
3. Missing-value identification and handling.
4. Categorical data encoding.
5. Feature and target separation.
6. Training and validation data splitting.
7. Data preprocessing using Scikit-learn pipelines.
8. Machine learning model development.
9. Model evaluation and comparison.
10. Model selection and saving.
11. Loan eligibility prediction.

Machine Learning Algorithms

Three classification algorithms were implemented:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

The best-performing model was selected using its validation F1-score.

Project Structure

loan-eligibility-prediction/
│
├── datasets/
├── saved_models/
├── loan_eligibility_prediction.ipynb
├── loan_eligibility_predictions.csv
├── requirements.txt
├── README.md
└── .gitignore

Installation and Usage

Clone the repository:

git clone YOUR_REPOSITORY_URL

Navigate into the project:

cd loan-eligibility-prediction

Create a virtual environment:

python -m venv venv

Activate the environment on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Launch Jupyter Notebook:

jupyter notebook

Open loan_eligibility_prediction.ipynb and execute the notebook cells.

Model Saving

The selected model is saved using Joblib in the saved_models/ directory.

Conclusion

This project demonstrates the application of supervised machine learning to a binary classification problem. It compares three classification algorithms and uses their validation performance to select a model for generating loan eligibility predictions.

Note: This project is for educational purposes. Its predictions are not intended to serve as actual financial or lending decisions.