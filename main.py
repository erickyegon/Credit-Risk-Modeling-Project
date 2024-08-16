import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title
st.set_page_config(page_title="Lauki Finance: Credit Risk Modelling", page_icon="📊", layout="wide")

# Custom CSS for a more modern look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 10px;
        border: 1px solid #ccc;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }
    .metric {
        font-size: 1.2em;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
    .metric-poor {
        background-color: #ff6666; /* Deep Red */
        color: #800000;
    }
    .metric-average {
        background-color: #ffff99; /* Yellow */
        color: #e6b800;
    }
    .metric-good {
        background-color: #66ff66; /* Green */
        color: #006600;
    }
    .metric-excellent {
        background-color: #009933; /* Deep Green */
        color: #003300;
    }
    </style>
    """, unsafe_allow_html=True)

# Title with custom styling
st.markdown("<h1 style='text-align: center;'>Lauki Finance: Credit Risk Modelling</h1>", unsafe_allow_html=True)

# Instructions section
st.markdown("""
**Instructions:**
1. **Input your details** in the fields below.
2. **Click "Calculate Risk"** to see the credit risk assessment.
3. **Interpret the results** based on the color-coded metrics.
""")

# Container for better spacing
container = st.container()

with container:
    # Create rows of three columns each
    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    # Assign inputs to the first row with default values
    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
    with row1[1]:
        income = st.number_input('Income', min_value=0, value=1200000)
    with row1[2]:
        loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

    # Calculate Loan to Income Ratio and display it
    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    with row2[0]:
        st.markdown(f"**Loan to Income Ratio:** {loan_to_income_ratio:.2f}")

    # Assign inputs to the remaining controls
    with row2[1]:
        loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
    with row2[2]:
        avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

    with row3[0]:
        delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
    with row3[1]:
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
    with row3[2]:
        num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

    with row4[0]:
        residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
    with row4[1]:
        loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
    with row4[2]:
        loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

    # Button to calculate risk
    if st.button('Calculate Risk'):
        # Call the predict function from the helper module
        probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months,
                                                    avg_dpd_per_delinquency,
                                                    delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                    residence_type, loan_purpose, loan_type)

        # Determine the class for the rating metric
        rating_class = ""
        if credit_score >= 720:
            rating_class = "metric-excellent"
        elif 690 <= credit_score < 720:
            rating_class = "metric-good"
        elif 630 <= credit_score < 690:
            rating_class = "metric-average"
        else:
            rating_class = "metric-poor"

        # Display the results in a visually appealing way
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Default Probability", f"{probability:.2%}")
        with col2:
            st.metric("Credit Score", credit_score)
        with col3:
            st.markdown(f"<div class='metric {rating_class}'>{rating}</div>", unsafe_allow_html=True)

# Footer
st.markdown('<p style="text-align: center; color: grey;">Project developed by Erick Kiprotich Yegon, PhD - Based on Codebasics ML Course</p>', unsafe_allow_html=True)
