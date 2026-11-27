import streamlit as st
from prediction import predict_loan_eligibility


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #F4F7FB;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #102A43 !important;
        font-weight: 800 !important;
    }

    p, label {
        color: #243B53 !important;
    }

    /* Form container */
    div[data-testid="stForm"] {
        background-color: #FFFFFF;
        padding: 22px;
        border: 1px solid #D9E2EC;
        border-radius: 14px;
    }

    /* Input labels */
    div[data-testid="stWidgetLabel"] p {
        color: #102A43 !important;
        font-weight: 700 !important;
    }

    /* Input fields */
    .stNumberInput input {
        color: #102A43 !important;
        background-color: #FFFFFF !important;
    }

    /* Select boxes */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
    }

    /* Predict button */
    div[data-testid="stFormSubmitButton"] button {
        background-color: #102A43 !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        border: none !important;
        border-radius: 9px !important;
        min-height: 50px !important;
        width: 100% !important;
        font-size: 17px !important;
        font-weight: 800 !important;
    }

    div[data-testid="stFormSubmitButton"] button p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    div[data-testid="stFormSubmitButton"] button:hover {
        background-color: #1D4E89 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #102A43;
    }

    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* Mobile layout */
    @media screen and (max-width: 768px) {

        .block-container {
            padding: 1rem;
        }

        h1 {
            font-size: 27px !important;
        }

        h2 {
            font-size: 22px !important;
        }

        div[data-testid="stForm"] {
            padding: 14px;
        }

        div[data-testid="stFormSubmitButton"] button {
            min-height: 55px !important;
            font-size: 16px !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🏦 Loan Predictor")

    st.divider()

    st.subheader("About")

    st.write(
        """
        This application uses a trained machine learning
        model to estimate loan eligibility based on the
        information provided by an applicant.
        """
    )

    st.divider()

    st.subheader("How it works")

    st.write(
        """
        1. Enter personal information.
        2. Enter financial information.
        3. Submit the details.
        4. View the prediction results.
        """
    )

    st.divider()

    st.subheader("Technologies")

    st.write(
        """
        - Python
        - Streamlit
        - Pandas
        - Scikit-learn
        - Machine Learning
        """
    )

    st.divider()

    st.caption("Educational Machine Learning Project")


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.title("Loan Eligibility Prediction")

st.write(
    """
    Welcome! Enter the applicant's information below
    to estimate their loan eligibility using our
    machine learning model.
    """
)

st.divider()


# --------------------------------------------------
# APPLICATION FORM
# --------------------------------------------------

with st.form("loan_prediction_form"):

    st.header("🤖 Choose Your Prediction Model")

    model_name = st.selectbox(

        "Select Machine Learning Model",

        options=[
            "Logistic Regression",
            "Decision Tree",
            "Random Forest"
        ],
        index=2,
        help="Choose the machine learning model you want to use."
    )
    st.divider()

    st.header("👤 Personal Information")
    
    st.caption("Enter the applicant's personal details.")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    married = st.selectbox(
        "Marital Status",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Number of Dependents",
        options=["0", "1", "2", "3"],
        index=0,
        key="applicant_dependents"
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    st.divider()

    st.header("💰 Financial Information")

    st.caption("Enter the applicant's financial details.")

    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0,
        value=5000,
        step=500
    )

    coapplicant_income = st.number_input(
        "Co-applicant Income",
        min_value=0,
        value=0,
        step=500
    )

    loan_amount = st.number_input(
        "Loan Amount (in thousands)",
        min_value=0,
        value=120,
        step=10
    )

    loan_amount_term = st.number_input(
        "Loan Amount Term (Months)",
        min_value=1,
        value=360,
        step=12
    )

    credit_history = st.selectbox(
        "Credit History",
        options=[1.0, 0.0],
        format_func=lambda value: (
            "Good Credit History"
            if value == 1.0
            else "No/Unsatisfactory Credit History"
        )
    )

    property_area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )

    st.divider()

    submit_button = st.form_submit_button(
        "Predict Loan Eligibility",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# PREDICTION RESULTS
# --------------------------------------------------

if submit_button:

    applicant_data = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_amount_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }

    try:

        result, probability = predict_loan_eligibility(
            applicant_data,
            model_name="Random Forest"
        )

        st.divider()

        st.header("📊 Prediction Results")
        st.info(f"Prediction generated using: {model_name}")

        if result == "Eligible":

            st.success(
                "ELIGIBLE\n\n"
                "The model predicts that this applicant "
                "is eligible for a loan."
            )

        else:

            st.error(
                "NOT ELIGIBLE\n\n"
                "The model predicts that this applicant "
                "is not eligible for a loan."
            )

        st.subheader("Model-estimated probability")

        st.metric(
            label="Predicted outcome probability",
            value=f"{probability:.2%}"
        )

        st.progress(
            float(probability),
            text=f"Estimated probability: {probability:.2%}"
        )

        st.info(
            """
            This percentage represents the model's estimated
            probability for the predicted outcome.
            """
        )

        st.warning(
            """
            **Important Disclaimer**

            This application is an educational machine learning
            demonstration. Its predictions are estimates generated
            by a trained model and should not be used as actual
            lending decisions or as a substitute for a financial
            institution's assessment.
            """
        )

    except Exception as error:

        st.error(
            "An error occurred while generating the prediction."
        )

        st.exception(error)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Loan Eligibility Prediction | Machine Learning Project"
)