import streamlit as st

from prediction import predict_loan_eligibility


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F4F7FB;
}

.main-title {
    color: #142B4A;
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    color: #64748B;
    font-size: 16px;
    margin-bottom: 25px;
}

.section-title {
    color: #142B4A;
    font-size: 22px;
    font-weight: 700;
}

.result-card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #DCE4EF;
    margin-top: 20px;
}

div.stButton > button,
div.stFormSubmitButton > button {
    background-color: #145DA0;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background-color: #0D477D;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# SIDEBAR
# --------------------------------

with st.sidebar:

    st.title("🏦 Loan Predictor")

    st.write(
        "A machine learning application "
        "for estimating loan eligibility."
    )

    st.divider()

    st.subheader("About the Application")

    st.write(
        "This application uses a trained "
        "Scikit-learn model to analyse "
        "applicant information and generate "
        "a prediction."
    )

    st.divider()

    st.subheader("How it works")

    st.write("1. Enter applicant information.")
    st.write("2. Submit the prediction form.")
    st.write("3. View the model's prediction.")

    st.divider()

    st.caption(
        "Built with Python, Streamlit, "
        "Pandas and Scikit-learn."
    )


# --------------------------------
# MAIN HEADER
# --------------------------------

st.markdown(
    '<div class="main-title">Loan Eligibility Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter applicant details to generate a machine learning prediction.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------
# APPLICANT INFORMATION
# --------------------------------

st.markdown(
    '<div class="section-title">Applicant Information</div>',
    unsafe_allow_html=True
)

st.write(
    "Provide the information below to evaluate the applicant."
)


with st.container(border=True):

    with st.form("loan_prediction_form"):

        st.subheader("Personal Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            gender = st.selectbox(
                "Gender",
                ["Male", "Female"]
            )

        with col2:
            married = st.selectbox(
                "Married",
                ["Yes", "No"]
            )

        with col3:
            dependents = st.selectbox(
                "Number of Dependents",
                ["0", "1", "2", "3+"]
            )

        col4, col5 = st.columns(2)

        with col4:
            education = st.selectbox(
                "Education",
                ["Graduate", "Not Graduate"]
            )

        with col5:
            self_employed = st.selectbox(
                "Self Employed",
                ["No", "Yes"]
            )

        st.divider()

        st.subheader("Financial Information")

        col6, col7 = st.columns(2)

        with col6:
            applicant_income = st.number_input(
                "Applicant Income",
                min_value=0,
                value=5000
            )

            loan_amount = st.number_input(
                "Loan Amount (in thousands)",
                min_value=0.0,
                value=150.0
            )

            credit_history = st.selectbox(
                "Credit History",
                [1.0, 0.0],
                format_func=lambda x:
                    "Good (1)" if x == 1.0 else "Poor (0)"
            )

        with col7:
            coapplicant_income = st.number_input(
                "Co-applicant Income",
                min_value=0.0,
                value=0.0
            )

            loan_term = st.number_input(
                "Loan Term (months)",
                min_value=1,
                value=360
            )

            property_area = st.selectbox(
                "Property Area",
                ["Urban", "Semiurban", "Rural"]
            )

        st.divider()

        submitted = st.form_submit_button(
            "Predict Loan Eligibility",
            use_container_width=True
        )


# --------------------------------
# PREDICTION
# --------------------------------

if submitted:

    applicant_data = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }

    try:

        result, probability = predict_loan_eligibility(
            applicant_data
        )

        st.divider()

        st.markdown(
            '<div class="section-title">Prediction Result</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):

            if result == "Eligible":

                st.success(
                    "The model predicts that this applicant "
                    "is eligible for a loan."
                )

            else:

                st.error(
                    "The model predicts that this applicant "
                    "is not eligible for a loan."
                )

            st.metric(
                "Model-estimated probability",
                f"{probability:.2%}"
            )

            st.progress(float(probability))

            st.caption(
                "The displayed probability relates to the "
                "predicted class. It is not a guarantee of approval."
            )

    except Exception as error:

        st.error(
            f"An error occurred while making the prediction: {error}"
        )


# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.caption(
    "Loan Eligibility Predictor | "
    "Powered by Python, Streamlit and Scikit-learn"
)

st.caption(
    "Educational demonstration only. "
    "Not an actual lending or credit approval system."
)