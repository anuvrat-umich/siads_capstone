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
dict_yes_no_alt = {"Yes": 1, "No": 2}

# Health radio button dictionary
dict_health = {
    "Excellent": 1,
    "Very good": 2,
    "Good": 3,
    "Fair": 4,
    "Poor": 5,
}

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

# Create a slider for Physical Health
PHYSHLTH = col1.slider(
    "Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?",
    0,
    30,
    0,
)

# Create a slider for Mental Health
MENTHLTH = col2.slider(
    "Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?",
    0,
    30,
    0,
)

# Create a radio button for Sex
rad_SEX = col1.radio("What is your birth sex?", ["Male", "Female"])
dict_sex = {"Male": 1, "Female": 2}
_SEX = dict_sex[rad_SEX]

# Create a radio button for Personal Doctor
rad_PERSDOC3 = col1.radio(
    "Do you have one person or a group of doctors you think of as your personal doctor or health care provider?",
    ["Yes", "No"],
)
PERSDOC3 = dict_yes_no[rad_PERSDOC3]

# Create a radio button for MEDCOST1
rad_MEDCOST1 = col1.radio(
    "Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?",
    ["Yes", "No"],
)
MEDCOST1 = dict_yes_no[rad_MEDCOST1]

# Create a radio button for CHECKUP1
rad_CHECKUP1 = col1.radio(
    "About how long has it been since you last visited a doctor for a routine checkup?",
    [
        "Within past year",
        "Within past 2 years",
        "Within past 5 years",
        "5 or more years",
    ],
)
dict_checkup = {
    "Within past year": 1,
    "Within past 2 years": 2,
    "Within past 5 years": 3,
    "5 or more years": 4,
}
CHECKUP1 = dict_checkup[rad_CHECKUP1]

# Create a slider for Sleep Time
SLEPTIM1 = col2.slider(
    "On average, how many hours of sleep do you get in a 24-hour period?",
    1,
    24,
    8,
)

# Create a radio button for Stroke
rad_CVDSTRK3 = col1.radio("Ever told you had a stroke?", ["Yes", "No"], index=1)
CVDSTRK3 = dict_yes_no[rad_CVDSTRK3]

# Create a radio button for Cholesterol
rad_CHCOCNC1 = col1.radio(
    "Have you ever been told that you had melanoma or any other types of cancer?",
    ["Yes", "No"],
)
CHCOCNC1 = dict_yes_no[rad_CHCOCNC1]

# Create a radio button for COPD
rad_CHCCOPD3 = col1.radio(
    "Ever told you had C.O.P.D. (chronic obstructive pulmonary disease), emphysema or chronic bronchitis?",
    ["Yes", "No"],
)
CHCCOPD3 = dict_yes_no[rad_CHCCOPD3]

# Create a radio button for Depression
rad_ADDEPEV3 = col1.radio(
    "Ever told you had a depressive disorder, including depression, major depression, dysthymia, or minor depression?",
    ["Yes", "No"],
)
ADDEPEV3 = dict_yes_no[rad_ADDEPEV3]

# Create a radio button for Kidney Disease
rad_CHCKDNY2 = col1.radio(
    "Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?",
    ["Yes", "No"],
    index=1,
)
CHCKDNY2 = dict_yes_no[rad_CHCKDNY2]

# Create a radio button for Diabetes
rad_DIABETE4 = col2.radio(
    "Have you ever been told by a doctor that you have diabetes?",
    ["Yes", "No", "Pre-diabetes or borderline diabetes only"],
)

if (
    (rad_DIABETE4 == "Yes")
    or (rad_DIABETE4 == "Pre-diabetes or borderline diabetes only")
) and (rad_SEX == "Female"):
    rad_DIABETE4_GESTATIONAL = col2.radio(
        "Was this only when you were pregnant?",
        ["Yes", "No"],
    )
else:
    rad_DIABETE4_GESTATIONAL = "No"

if (
    (rad_DIABETE4 == "Yes")
    or (rad_DIABETE4 == "Pre-diabetes or borderline diabetes only")
) and (rad_DIABETE4_GESTATIONAL == "No"):
    DIABETE4 = 1
else:
    DIABETE4 = 0


# Create a radio button for Education
options_EDUCA = [
    "Never attended school or only kindergarten",
    "Grades 1 through 8 (Elementary)",
    "Grades 9 through 11 (Some high school)",
    "Grade 12 or GED (High school graduate)",
    "College 1 year to 3 years (Some college or technical school)",
    "College 4 years or more (College graduate)",
]
EDUCA = 1 + options_EDUCA.index(
    col2.radio(
        "What is the highest grade or year of school you completed?",
        options_EDUCA,
    ),
    0,
)

# Create a radio button for Veteran Status
rad_VETERAN3 = col1.radio(
    "Have you ever served on active duty in the U.S. Armed Forces, military Reserves, or National Guard?",
    ["Yes", "No"],
)
VETERAN3 = dict_yes_no[rad_VETERAN3]

# Create a slider for Number of Children
CHILDREN = col2.slider("How many children live in your household?", 0, 87, 0)

# Create a radio button for Income
options_INCOME3 = [
    "Less than $10,000",
    "10,000 to less than 15,000",
    "15,000 to less than 20,000",
    "20,000 to less than 25,000",
    "25,000 to less than 35,000",
    "35,000 to less than 50,000",
    "50,000 to less than 75,000",
    "75,000 to less than 100,000",
    "100,000 to less than 150,000",
    "150,000 to less than 200,000",
    "200,000 or more",
]
INCOME3 = 1 + options_INCOME3.index(
    col2.radio("Is your annual household income from all sources:", options_INCOME3),
    0,
)

# Create a radio button for Decision Making
rad_DECIDE = col2.radio(
    "Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?",
    ["Yes", "No"],
)
DECIDE = dict_yes_no[rad_DECIDE]

# Create a radio button for Difficulty doing Errands Alone
rad_DIFFALON = col2.radio(
    "Because of a physical, mental, or emotional condition, do you have difficulty doing errands alone such as visiting a doctor's office or shopping?",
    ["Yes", "No"],
)
DIFFALON = dict_yes_no[rad_DIFFALON]

# Create a radio button for COVID-19 Positive
rad_COVIDPOS = col2.radio(
    "Has a doctor, nurse, or other health professional ever told you that you tested positive for COVID 19?",
    ["Yes", "No", "Tested positive using home test without health professional"],
)
if (rad_COVIDPOS == "Yes") or (
    rad_COVIDPOS == "Tested positive using home test without health professional"
):
    COVIDPOS = 1
else:
    COVIDPOS = 0

# Create a radio button for Pre-Diabetes
rad_PREDIAB2 = col2.radio(
    "Have you ever been told by a doctor that you have pre-diabetes or borderline diabetes?",
    ["Yes", "Yes, during pregnancy", "No"],
)
PREDIAB2 = dict_yes_no[rad_PREDIAB2]
if (rad_COVIDPOS == "Yes") or (rad_COVIDPOS == "Yes, during pregnancy"):
    PREDIAB2 = 1
else:
    PREDIAB2 = 0

# Display the user inputs
st.write("Diabetes is:", DIABETE4)

# Data
st.write("Your BMI is:", _BMI5)

# Create the prediction button
if st.button("Predict risk of heart attack"):
    prediction = predict_dummy([[CVDCRHD4, age, _AGE80, GENHLTH, WTKG3, HTM4, _BMI5]])

    # Display the prediction
    st.write("The predicted risk of heart attack is:", prediction)  # prediction[0]


# ['GENHLTH', 'PHYSHLTH', 'MENTHLTH', 'PERSDOC3', 'MEDCOST1', 'CHECKUP1',
#       'SLEPTIM1', 'CVDCRHD4', 'CVDSTRK3', 'CHCOCNC1', 'CHCCOPD3', 'ADDEPEV3',
#       'CHCKDNY2', 'DIABETE4', 'EDUCA', 'VETERAN3', 'CHILDREN', 'INCOME3',
#       'DECIDE', 'DIFFALON', 'COVIDPOS', 'PREDIAB2', 'CNCRDIFF', 'LSATISFY',
#       'EMTSUPRT', 'SDHISOLT', 'SDHEMPLY', 'FOODSTMP', 'SDHFOOD1', 'SDHBILLS',
#       'SDHUTILS', 'SDHTRNSP', 'SDHSTRE1', 'QSTLANG', '_METSTAT', '_URBSTAT',
#       '_HLTHPLN', '_TOTINDA', '_DRDXAR2', '_SEX', '_AGE80', 'HTM4', 'WTKG3',
#       '_BMI5', '_RFBING6', '_DRNKWK2', '_RFDRHV8', '_ASTHMS1_2.0',
#       '_ASTHMS1_3.0', 'RENTHOM1_1.0', 'RENTHOM1_3.0', '_BMI5CAT_1.0',
#      '_BMI5CAT_2.0', '_BMI5CAT_3.0', '_RACEPR1_2.0', '_RACEPR1_3.0',
#       '_RACEPR1_4.0', '_RACEPR1_5.0', '_RACEPR1_6.0', '_RACEPR1_7.0',
#       '_SMOKGRP_1.0', '_SMOKGRP_3.0', 'EMPLOY1_3.0', 'EMPLOY1_5.0',
#       'EMPLOY1_7.0', 'EMPLOY1_8.0', 'MARITAL_2.0', 'MARITAL_5.0']
