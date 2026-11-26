import streamlit as st

from prediction import predict_loan_eligibility


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# 2. CUSTOM RESPONSIVE CSS
# ==========================================

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #F4F7FB;
}

/* Main content width */
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main heading */
.main-title {
    color: #142B4A !important;
    font-size: 36px;
    font-weight: 800;
    line-height: 1.3;
    margin-bottom: 8px;
}

/* Subtitle */
.subtitle {
    color: #475569 !important;
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 25px;
}

/* Section headings */
.section-title {
    color: #142B4A !important;
    font-size: 24px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 12px;
}

/* Form section headings */
.stForm h2,
.stForm h3,
.stForm h4 {
    color: #142B4A !important;
    font-weight: 800 !important;
}

/* Input labels */
.stSelectbox label,
.stNumberInput label {
    color: #142B4A !important;
    font-size: 16px !important;
    font-weight: 700 !important;
}

/* Input text */
.stSelectbox div[data-baseweb="select"],
.stNumberInput input {
    color: #142B4A !important;
    font-size: 16px !important;
}

/* Improve general text visibility */
.stMarkdown p,
.stCaption {
    color: #334155;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EAF0F8;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #142B4A !important;
}

/* Form container */
[data-testid="stForm"] {
    background-color: #FFFFFF;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #D5DFEA;
}

/* Buttons */
div.stButton > button,
div.stFormSubmitButton > button {
    background-color: #145DA0 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 9px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    min-height: 48px;
}

/* Button hover */
div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background-color: #0D477D !important;
    color: #FFFFFF !important;
}

/* Prediction result card */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px;
}

/* Success and error messages */
[data-testid="stAlert"] {
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
}

/* Metrics */
[data-testid="stMetricLabel"] {
    color: #334155 !important;
    font-size: 16px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #142B4A !important;
    font-size: 32px !important;
    font-weight: 800 !important;
}

/* Footer */
.footer {
    color: #64748B;
    font-size: 13px;
    text-align: center;
    line-height: 1.7;
}

/* Mobile responsiveness */
@media screen and (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }

    .main-title {
        font-size: 27px;
    }

    .subtitle {
        font-size: 15px;
    }

    .section-title {
        font-size: 21px;
    }

    .stSelectbox label,
    .stNumberInput label {
        font-size: 15px !important;
    }

    [data-testid="stForm"] {
        padding: 12px;
    }

    [data-testid="stMetricValue"] {
        font-size: 28px !important;
    }

    div.stFormSubmitButton > button {
        min-height: 52px;
        font-size: 16px !important;
    }

}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🏦 Loan Predictor")

    st.write(
        "A machine learning application "
        "for predicting loan eligibility."
    )

    st.divider()

    st.subheader("About the Application")

    st.write(
        "This application uses a trained "
        "Scikit-learn machine learning model "
        "to analyse applicant information."
    )

    st.divider()

    st.subheader("How It Works")

    st.write("1. Enter personal information.")
    st.write("2. Enter financial information.")
    st.write("3. Submit your information.")
    st.write("4. View your prediction.")

    st.divider()

    st.subheader("Technology")

    st.write("🐍 Python")
    st.write("📊 Pandas")
    st.write("🤖 Scikit-learn")
    st.write("🌐 Streamlit")

    st.divider()

    st.caption(
        "Educational machine learning project."
    )


# ==========================================
# 4. MAIN HEADER
# ==========================================

st.markdown(
    '<div class="main-title">'
    '🏦 Loan Eligibility Predictor'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter the applicant details below to receive '
    'a machine learning-based loan eligibility prediction.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# 5. APPLICANT INFORMATION FORM
# ==========================================

st.markdown(
    '<div class="section-title">'
    'Applicant Information'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Please provide accurate information in all the fields."
)


with st.container(border=True):

    with st.form("loan_prediction_form"):

        # ----------------------------------
        # PERSONAL INFORMATION
        # ----------------------------------

        st.subheader("👤 Personal Information")

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
            ["0", "1", "2", "3+"]
        )

        education = st.selectbox(
            "Education Level",
            ["Graduate", "Not Graduate"]
        )

        self_employed = st.selectbox(
            "Self Employed",
            ["No", "Yes"]
        )

        st.divider()

        # ----------------------------------
        # FINANCIAL INFORMATION
        # ----------------------------------

        st.subheader("💰 Financial Information")

        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0,
            value=5000,
            help="Enter the applicant's income in the dataset's currency units."
        )

        coapplicant_income = st.number_input(
            "Co-applicant Income",
            min_value=0.0,
            value=0.0,
            help="Enter the co-applicant's income."
        )

        loan_amount = st.number_input(
            "Loan Amount (in thousands)",
            min_value=0.0,
            value=150.0
        )

        loan_term = st.number_input(
            "Loan Term (months)",
            min_value=1,
            value=360
        )

        credit_history = st.selectbox(
            "Credit History",
            [1.0, 0.0],
            format_func=lambda x:
                "Good (1)" if x == 1.0 else "Poor (0)"
        )

        property_area = st.selectbox(
            "Property Area",
            ["Urban", "Semiurban", "Rural"]
        )

        st.divider()

        # ----------------------------------
        # SUBMIT BUTTON
        # ----------------------------------

        submitted = st.form_submit_button(
            "🔍 Predict Loan Eligibility",
            use_container_width=True
        )


# ==========================================
# 6. PREDICTION PROCESS
# ==========================================

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

        # ----------------------------------
        # PREDICTION RESULT HEADING
        # ----------------------------------

        st.markdown(
            '<div class="section-title">'
            '📊 Loan Prediction Result'
            '</div>',
            unsafe_allow_html=True
        )

        # ----------------------------------
        # RESULT DISPLAY
        # ----------------------------------

        with st.container(border=True):

            if result == "Eligible":

                st.success(
                    "PREDICTION: ELIGIBLE"
                )

                st.markdown(
                    "### The model predicts that this "
                    "applicant is eligible for a loan."
                )

            else:

                st.error(
                    "PREDICTION: NOT ELIGIBLE"
                )

                st.markdown(
                    "### The model predicts that this "
                    "applicant is not eligible for a loan."
                )

            st.divider()

            # ----------------------------------
            # PROBABILITY DISPLAY
            # ----------------------------------

            st.subheader(
                "Model-estimated probability"
            )

            st.metric(
                label="Probability of the predicted outcome",
                value=f"{probability:.2%}"
            )

            st.progress(
                float(probability)
            )

            st.caption(
                "This probability represents the model's "
                "estimated confidence in its predicted class. "
                "It is not a guarantee of loan approval."
            )

        # ----------------------------------
        # EDUCATIONAL DISCLAIMER
        # ----------------------------------

        st.info(
            "Important: This application is an educational "
            "machine learning demonstration. Its prediction "
            "is not an actual loan approval or financial decision."
        )

    except Exception as error:

        st.error(
            f"An error occurred while making the prediction: {error}"
        )


# ==========================================
# 7. FOOTER
# ==========================================

st.divider()

st.markdown(
    """
    <div class="footer">
        <strong>Loan Eligibility Predictor</strong><br>
        Powered by Python, Streamlit, Pandas and Scikit-learn.<br>
        Educational demonstration only.
    </div>
    """,
    unsafe_allow_html=True
)