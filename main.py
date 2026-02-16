import streamlit as st
from prediction_helper import predict

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Health Insurance Premium Predictor",
    page_icon="💊",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #0E6EFD;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            height: 3em;
            width: 100%;
        }
        .prediction-box {
            background-color: #E8F4FF;
            padding: 20px;
            border-radius: 10px;
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            color: #0E6EFD;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("## 💊 Health Insurance Premium Predictor")
st.markdown("Predict your estimated insurance premium based on personal and medical details.")

st.divider()

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("📌 About")
st.sidebar.info(
    "This app predicts health insurance premium using a trained ML model.\n\n"
    "Fill in the details and click Predict."
)

# ---------------- FORM ---------------- #
with st.form("prediction_form"):

    st.subheader("👤 Personal Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
        gender = st.selectbox("Gender", ['Male', 'Female'])
        marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])

    with col2:
        number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=20)
        income_lakhs = st.number_input("Income (in Lakhs)", min_value=0, max_value=200)
        employment_status = st.selectbox("Employment Status",
                                         ['Salaried', 'Self-Employed', 'Freelancer'])

    with col3:
        region = st.selectbox("Region",
                              ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
        insurance_plan = st.selectbox("Insurance Plan",
                                      ['Bronze', 'Silver', 'Gold'])

    st.divider()

    st.subheader("🏥 Health Information")

    col4, col5, col6 = st.columns(3)

    with col4:
        bmi_category = st.selectbox("BMI Category",
                                    ['Normal', 'Obesity', 'Overweight', 'Underweight'])

    with col5:
        smoking_status = st.selectbox("Smoking Status",
                                      ['No Smoking', 'Regular', 'Occasional'])

    with col6:
        genetical_risk = st.slider("Genetical Risk", 0, 5)

    medical_history = st.selectbox("Medical History", [
        'No Disease', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid',
        'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ])

    st.divider()

    submit = st.form_submit_button("🔍 Predict Premium")

# ---------------- PREDICTION ---------------- #
if submit:

    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    prediction = predict(input_dict)

    st.markdown(
        f"""
        <div class="prediction-box">
            💰 Estimated Premium: ₹ {prediction}
        </div>
        """,
        unsafe_allow_html=True
    )
