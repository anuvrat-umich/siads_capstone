import streamlit as st
import joblib


def predict(data):
    clf = joblib.load("./siads_capstone/models/rf_model.pkl")
    return clf.predict(data)


def predict_dummy(data):
    if data[0][-1] > 3000:
        return "High"
    else:
        return "Low"


# Yes/No radio button dictionary
dict_yes_no = {"Yes": 1, "No": 0}

# Set the app title
st.title("Risk of Heart Attack / Myocardial Infarction Prediction")
# Set the app description with a welcome message
st.markdown(
    "Hello! This app predicts the risk of heart attack based on a few user inputs."
)
# st.write("Thanks for using our model!")

# Getting user inputs
st.header("Inputs for Prediction")

# Create two columns for user inputs
col1, col2 = st.columns(2)

# Create a radio button for Angina or Coronary Heart Disease
rad_CVDCRHD4 = col1.radio(
    "(Ever told) (you had) angina or coronary heart disease?", ["Yes", "No"]
)
CVDCRHD4 = dict_yes_no[rad_CVDCRHD4]

# Create a slider for age
age = col2.slider("Age", 20, 100, 50)
if age > 80:
    _AGE80 = 1
else:
    _AGE80 = 0

# Create a radio button for General Health
rad_GENHLTH = col1.radio(
    "Would you say that in general your health is",
    ["Excellent", "Very good", "Good", "Fair", "Poor"],
)
dict_health = {
    "Excellent": 1,
    "Very good": 2,
    "Good": 3,
    "Fair": 4,
    "Poor": 5,
}
GENHLTH = dict_health[rad_GENHLTH]

# Create a slider for Weight
WTKG3 = col2.slider("Weight (KG)", 23.00, 295.00, 100.00)
WTKG3 = WTKG3 * 100

# Create a slider for Height
HTM4 = col2.slider("Height (CM)", 122, 213, 170)

# Calculate BMI
_BMI5 = int(
    WTKG3 / ((HTM4 / 100) ** 2)
)  # BMI = weight (kg) / height (m)^2. BMI = weight (g) / height (cm)^2. BMI = weight (g) / height (cm)^2 * 10000

# Create a text input
# user_input = st.text_input("Enter a custom message:", "Hello, Streamlit!")
# Display the customized message
# st.write("Customized Message:", user_input)

# Data
st.write("Your BMI is:", _BMI5)

# Create the prediction button
if st.button("Predict risk of heart attack"):
    prediction = predict_dummy([[CVDCRHD4, age, _AGE80, GENHLTH, WTKG3, HTM4, _BMI5]])

    # Display the prediction
    st.write("The predicted risk of heart attack is:", prediction)  # prediction[0]
