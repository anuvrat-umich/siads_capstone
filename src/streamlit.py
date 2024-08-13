import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler


def predict(data):
    clf = joblib.load("./models/lr_model.pkl")
    threshold = 0.8

    # Define scaler to scale the data
    # scaler = StandardScaler()
    # data_scaled = scaler.fit_transform(data)

    # Make prediction
    predicted_proba = clf.predict_proba(data)[0][1]

    if predicted_proba > threshold:
        return f"High ({predicted_proba:.0%})"
    else:
        # return probability as percentage
        return f"Low ({predicted_proba:.0%})"


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

from pathlib import Path
import base64


# Function to convert image to base64
@st.cache_resource
def get_base64_image(image_file):
    image_path = Path(image_file).resolve()
    with open(image_path, "rb") as f:
        return f"data:image/webp;base64,{base64.b64encode(f.read()).decode()}"


background_image = get_base64_image("appdata/backgroundimage2.webp")

# Set the background image with transparency
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.92)), 
                    url("{background_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Set the app title
st.title("Risk of Heart Attack / Myocardial Infarction Prediction")
# Set the app description with a welcome message
st.markdown(
    "Hello! This app predicts the risk of heart attack based on a few user inputs. Time to complete: ~5 mins."
)
st.markdown(
    "Disclaimer: This is an experimental, educational model built using public data and should not be considered medical advice. \
    Please consult your doctor or a health care professional to talk about your situation."
)

# Getting user inputs
st.header("Inputs for Prediction")

# Create two columns for user inputs
col1, col2 = st.columns(2)

# Create a radio button for Sex
rad_SEX = col1.radio("What is your birth sex?", ["Male", "Female"], index=0)
dict_sex = {"Male": 1, "Female": 2}
_SEX = dict_sex[rad_SEX]

# Create a slider for Height
HTM4 = col1.slider("Height (CM)", 122, 213, 170)

# Create a slider for Weight
WTKG3 = col1.slider("Weight (KG)", 23.00, 295.00, 75.00)
WTKG3 = WTKG3 * 100

# Calculate BMI
_BMI5 = int(
    WTKG3 / ((HTM4 / 100) ** 2)
)  # BMI = weight (kg) / height (m)^2. BMI = weight (g) / height (cm)^2. BMI = weight (g) / height (cm)^2 * 10000

# Create a slider for age. Age value collapsed above 80
age = col1.slider("Age", 20, 100, 65)
if age > 80:
    _AGE80 = 80
else:
    _AGE80 = age

# Create a radio button for General Health
rad_GENHLTH = col1.radio(
    "Would you say that in general your health is",
    ["Excellent", "Very good", "Good", "Fair", "Poor"],
    index=1,
)
GENHLTH = dict_health[rad_GENHLTH]

# Create a slider for Physical Health
PHYSHLTH = col1.slider(
    "Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?",
    0,
    30,
    0,
)

# Create a slider for Mental Health
MENTHLTH = col1.slider(
    "Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?",
    0,
    30,
    0,
)

# Create a radio button for Personal Doctor
rad_PERSDOC3 = col1.radio(
    "Do you have one person or a group of doctors you think of as your personal doctor or health care provider?",
    ["Yes", "No"],
    index=0,
)
PERSDOC3 = dict_yes_no[rad_PERSDOC3]

# Create a radio button for MEDCOST1
rad_MEDCOST1 = col1.radio(
    "Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?",
    ["Yes", "No"],
    index=1,
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
        "Never",
    ],
    index=0,
)
dict_checkup = {
    "Within past year": 1,
    "Within past 2 years": 2,
    "Within past 5 years": 3,
    "5 or more years": 4,
    "Never": 8,
}
CHECKUP1 = dict_checkup[rad_CHECKUP1]

# Create a slider for Sleep Time
SLEPTIM1 = col1.slider(
    "On average, how many hours of sleep do you get in a 24-hour period?",
    1,
    24,
    8,
)

# Create a radio button for Angina or Coronary Heart Disease
rad_CVDCRHD4 = col1.radio(
    "Have you ever been told by a doctor that you have angina or coronary heart disease?",
    ["Yes", "No"],
    index=1,
)
CVDCRHD4 = dict_yes_no[rad_CVDCRHD4]

# Create a radio button for Stroke
rad_CVDSTRK3 = col1.radio("Ever told you had a stroke?", ["Yes", "No"], index=1)
CVDSTRK3 = dict_yes_no[rad_CVDSTRK3]

# Create a radio button for Cholesterol
rad_CHCOCNC1 = col1.radio(
    "Have you ever been told that you had melanoma or any other types of cancer?",
    ["Yes", "No"],
    index=1,
)
CHCOCNC1 = dict_yes_no[rad_CHCOCNC1]

# Create a radio button for COPD
rad_CHCCOPD3 = col1.radio(
    "Ever told you had C.O.P.D. (chronic obstructive pulmonary disease), emphysema or chronic bronchitis?",
    ["Yes", "No"],
    index=1,
)
CHCCOPD3 = dict_yes_no[rad_CHCCOPD3]

# Create a radio button for Depression
rad_ADDEPEV3 = col1.radio(
    "Ever told you had a depressive disorder, including depression, major depression, dysthymia, or minor depression?",
    ["Yes", "No"],
    index=1,
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
rad_DIABETE4 = col1.radio(
    "Have you ever been told by a doctor that you have diabetes?",
    ["Yes", "No", "Pre-diabetes or borderline diabetes only"],
    index=1,
)

if (
    (rad_DIABETE4 == "Yes")
    or (rad_DIABETE4 == "Pre-diabetes or borderline diabetes only")
) and (rad_SEX == "Female"):
    rad_DIABETE4_GESTATIONAL = col1.radio(
        "Was this only when you were pregnant?", ["Yes", "No"], index=1
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
    col1.radio(
        "What is the highest grade or year of school you completed?",
        options_EDUCA,
        index=5,
    ),
    0,
)

# Create a radio button for Veteran Status
rad_VETERAN3 = col1.radio(
    "Have you ever served on active duty in the U.S. Armed Forces, military Reserves, or National Guard?",
    ["Yes", "No"],
    index=1,
)
VETERAN3 = dict_yes_no[rad_VETERAN3]

# Create a slider for Number of Children
CHILDREN = col1.slider("How many children live in your household?", 0, 40, 0)

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
    col1.radio(
        "Is your annual household income from all sources:", options_INCOME3, index=5
    ),
    0,
)

# Create a radio button for Decision Making
rad_DECIDE = col1.radio(
    "Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?",
    ["Yes", "No"],
    index=1,
)
DECIDE = dict_yes_no[rad_DECIDE]

# Create a radio button for Difficulty doing Errands Alone
rad_DIFFALON = col1.radio(
    "Because of a physical, mental, or emotional condition, do you have difficulty doing errands alone such as visiting a doctor's office or shopping?",
    ["Yes", "No"],
    index=1,
)
DIFFALON = dict_yes_no[rad_DIFFALON]

# Create a radio button for COVID-19 Positive
rad_COVIDPOS = col1.radio(
    "Has a doctor, nurse, or other health professional ever told you that you tested positive for COVID 19?",
    ["Yes", "No", "Tested positive using home test without health professional"],
    index=1,
)
if (rad_COVIDPOS == "Yes") or (
    rad_COVIDPOS == "Tested positive using home test without health professional"
):
    COVIDPOS = 1
else:
    COVIDPOS = 0

# Create a radio button for Pre-Diabetes
rad_PREDIAB2 = col1.radio(
    "Have you ever been told by a doctor that you have pre-diabetes or borderline diabetes?",
    ["Yes", "Yes, during pregnancy", "No"],
    index=2,
)
if (rad_COVIDPOS == "Yes") or (rad_COVIDPOS == "Yes, during pregnancy"):
    PREDIAB2 = 1
else:
    PREDIAB2 = 0

# Create a radio button for Cancer Diagnosis
options_CNCRDIFF = ["Only one", "Two", "Three or more"]
if rad_CHCOCNC1 == "Yes":
    rad_CANCRDIFF = col1.radio(
        "How many different types of cancer have you been diagnosed with?",
        options_CNCRDIFF,
        index=0,
    )
    CNCRDIFF = 1 + options_CNCRDIFF.index(rad_CANCRDIFF)
else:
    CNCRDIFF = 0

# Create a radio button for Satisfaction with Life
rad_LSATISFY = col2.radio(
    "In general, how satisfied are you with your life?",
    ["Very satisfied", "Satisfied", "Dissatisfied", "Very dissatisfied"],
    index=0,
)
if (rad_LSATISFY == "Very satisfied") or (rad_LSATISFY == "Satisfied"):
    LSATISFY = 1
else:
    LSATISFY = 0

# Create a radio button for Emotional Support
options_EMTSUPRT = ["Always", "Usually", "Sometimes", "Rarely", "Never"]
EMTSUPRT = 1 + options_EMTSUPRT.index(
    col2.radio(
        "How often do you get the social and emotional support you need?",
        options_EMTSUPRT,
        index=0,
    )
)

# Create a radio button for Social Isolation
options_SDHISOLT = ["Always", "Usually", "Sometimes", "Rarely", "Never"]
SDHISOLT = 1 + options_SDHISOLT.index(
    col2.radio("How often do you feel isolated from others?", options_SDHISOLT, index=4)
)

# Create a radio button for Employment Status
rad_SDHEMPLY = col2.radio(
    "In the past 12 months have you lost employment or had hours reduced?",
    ["Yes", "No"],
    index=1,
)
SDHEMPLY = dict_yes_no[rad_SDHEMPLY]

# Create a radio button for Food Stamps
rad_FOODSTMP = col2.radio(
    "During the past 12 months, have you received food stamps, also called SNAP, the Supplemental Nutrition Assistance Program on an EBT card?",
    ["Yes", "No"],
    index=1,
)
FOODSTMP = dict_yes_no[rad_FOODSTMP]

# Create a radio button for Food Insecurity
options_SDHFOOD1 = ["Always", "Usually", "Sometimes", "Rarely", "Never"]
SDHFOOD1 = 1 + options_SDHFOOD1.index(
    col2.radio(
        "During the past 12 months how often did the food that you bought not last, and you didn't have money to get more?",
        options_SDHFOOD1,
        index=4,
    )
)

# Create a radio button for Bills
rad_SDHBILLS = col2.radio(
    "During the last 12 months, was there a time when you were not able to pay your mortgage, rent or utility bills?",
    ["Yes", "No"],
    index=1,
)
SDHBILLS = dict_yes_no[rad_SDHBILLS]

# Create a radio button for Utilities
rad_SDHUTILS = col2.radio(
    "During the last 12 months was there a time when an electric, gas, oil, or water company threatened to shut off services?",
    ["Yes", "No"],
    index=1,
)
SDHUTILS = dict_yes_no[rad_SDHUTILS]

# Create a radio button for Transportation
rad_SDHTRNSP = col2.radio(
    "During the past 12 months has a lack of reliable transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living?",
    ["Yes", "No"],
    index=1,
)
SDHTRNSP = dict_yes_no[rad_SDHTRNSP]

# Create a radio button for Stress
options_SDHSTRE1 = ["Always", "Usually", "Sometimes", "Rarely", "Never"]
SDHSTRE1 = 1 + options_SDHSTRE1.index(
    col2.radio(
        "Stress means a situation in which a person feels tense, restless, nervous, or anxious, or is unable to sleep at night because his/her mind is troubled all the time. Within the last 30 days, how often have you felt this kind of stress?",
        options_SDHSTRE1,
        index=4,
    )
)

# Create a radio button for Language
rad_QSTLANG = col2.radio(
    "What language do you mainly speak at home?", ["English", "Spanish"], index=0
)
if rad_QSTLANG == "English":
    QSTLANG = 1
else:
    QSTLANG = 2

# Create a radio button for Metropolitan Status
rad_METSTAT = col2.radio(
    "Do you live in a Metropolitan county?", ["Yes", "No"], index=0
)
_METSTAT = dict_yes_no[rad_METSTAT]

# Create a radio button for Urban Status
rad_URBSTAT = col2.radio("Do you live in an Urban county?", ["Yes", "No"], index=0)
_URBSTAT = dict_yes_no[rad_URBSTAT]

# Create a radio button for Health Plan
rad_HLTHPLN = col2.radio(
    "Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare?",
    ["Yes", "No"],
    index=0,
)
_HLTHPLN = dict_yes_no[rad_HLTHPLN]

# Create a radio button for any activity or exercise
rad_TOTINDA = col2.radio(
    "During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?",
    ["Yes", "No"],
    index=0,
)
_TOTINDA = dict_yes_no[rad_TOTINDA]

# Create a radio button for Arthritis
rad_DRDXAR2 = col2.radio(
    "Have you ever been told by a doctor or other health professional that you have some form of arthritis, rheumatoid arthritis, gout, lupus, or fibromyalgia?",
    ["Yes", "No"],
    index=1,
)
_DRDXAR2 = dict_yes_no[rad_DRDXAR2]

# Calculate feature for Binge Drinking
if rad_SEX == "Male":
    question_text = (
        "In the past 30 days, have you had five or more drinks on one occasion?"
    )
else:
    question_text = (
        "In the past 30 days, have you had four or more drinks on one occasion?"
    )
rad_RFBING6 = col2.radio(
    question_text,
    ["Yes", "No"],
)
_RFBING6 = dict_yes_no[rad_RFBING6]

# Create a slider for Drinking Frequency
ALCDAY4 = col2.slider(
    "During the past 30 days, how many days per week did you have at least one drink of any alcoholic beverage??",
    0,
    7,
    0,
)

if ALCDAY4 > 0:
    # Create a radio button for Drinking Frequency
    AVEDRNK3 = col2.slider(
        "On the days when you drank, about how many drinks did you drink on average?",
        1,
        99,
        1,
    )
else:
    AVEDRNK3 = 0

# Calculate total number of alcoholic beverages consumed per week
_DRNKWK2 = round(ALCDAY4 * AVEDRNK3 * 100, ndigits=0)

# Calculate the Heavy Drinking Category
if (
    ((rad_SEX == "Male") and (_DRNKWK2 > 1400))
    or (rad_SEX == "Female")
    and (_DRNKWK2 > 700)
):
    _RFDRHV8 = 1
else:
    _RFDRHV8 = 0

# Create a radio button for Asthma
rad_ASTHMS1 = col2.radio(
    "Have you ever been told by a doctor or other health professional that you have asthma?",
    ["Current", "Former", "Never"],
    index=2,
)

if rad_ASTHMS1 == "Former":
    _ASTHMS1_2 = 1
else:
    _ASTHMS1_2 = 0

if rad_ASTHMS1 == "Never":
    _ASTHMS1_3 = 1
else:
    _ASTHMS1_3 = 0

# Create a radio button for Home Ownership
rad_RENTHOM1 = col2.radio(
    "Do you own or rent your home?", ["Own", "Rent", "Other"], index=0
)

if rad_RENTHOM1 == "Own":
    RENTHOM1_1 = 1
else:
    RENTHOM1_1 = 0

if rad_RENTHOM1 == "Other":
    RENTHOM1_3 = 1
else:
    RENTHOM1_3 = 0

# Calculate BMI Category
_BMI5CAT_1 = 0
_BMI5CAT_2 = 0
_BMI5CAT_3 = 0
if _BMI5 < 1850:
    _BMI5CAT_1 = 1
elif _BMI5 < 2500:
    _BMI5CAT_2 = 1
elif _BMI5 < 3000:
    _BMI5CAT_3 = 1

# Create a radio button for Race
rad_RACEPR1 = col2.radio(
    "What is your Race/ethnicity? Please select the closest match. We understand that this may not be a perfect match. These are the only categories present in the data.",
    [
        "White only, non-Hispanic",
        "Black only, non-Hispanic",
        "American Indian or Alaskan Native only, Non-Hispanic",
        "Asian only, non-Hispanic",
        "Native Hawaiian or other Pacific Islander only, Non-Hispanic",
        "Multiracial, non-Hispanic",
        "Hispanic",
    ],
    index=0,
)
_RACEPR1_2 = 0
_RACEPR1_3 = 0
_RACEPR1_4 = 0
_RACEPR1_5 = 0
_RACEPR1_6 = 0
_RACEPR1_7 = 0
if rad_RACEPR1 == "Black only, non-Hispanic":
    _RACEPR1_2 = 1
elif rad_RACEPR1 == "American Indian or Alaskan Native only, Non-Hispanic":
    _RACEPR1_3 = 1
elif rad_RACEPR1 == "Asian only, non-Hispanic":
    _RACEPR1_4 = 1
elif rad_RACEPR1 == "Native Hawaiian or other Pacific Islander only, Non-Hispanic":
    _RACEPR1_5 = 1
elif rad_RACEPR1 == "Multiracial, non-Hispanic":
    _RACEPR1_6 = 1
elif rad_RACEPR1 == "Hispanic":
    _RACEPR1_7 = 1

# Create a radio button for Smoking
rad_SMOKGRP = col2.radio(
    "Do you now smoke cigarettes?",
    [
        "Current smoker, 20+ Pack Years",
        "Former smoker, 20+ Pack Years, quit < 15 years",
        "Other smoker",
        "Never smoked",
    ],
    index=3,
)
_SMOKGRP_1 = 0
_SMOKGRP_3 = 0
if rad_SMOKGRP == "Current smoker, 20+ Pack Years":
    _SMOKGRP_1 = 1
elif rad_SMOKGRP == "Other smoker":
    _SMOKGRP_3 = 1

# Create a radio button for Employment
rad_EMPLOY1 = col2.radio(
    "What is your current employment status?",
    [
        "Employed for wages",
        "Self-employed",
        "Out of work for 1 year or more",
        "Out of work for less than 1 year",
        "A homemaker",
        "A student",
        "Retired",
        "Unable to work",
    ],
    index=0,
)
EMPLOY1_3 = 0
EMPLOY1_5 = 0
EMPLOY1_7 = 0
EMPLOY1_8 = 0
if rad_EMPLOY1 == "Out of work for 1 year or more":
    EMPLOY1_3 = 1
elif rad_EMPLOY1 == "Out of work for less than 1 year":
    EMPLOY1_5 = 1
elif rad_EMPLOY1 == "Retired":
    EMPLOY1_7 = 1
elif rad_EMPLOY1 == "Unable to work":
    EMPLOY1_8 = 1

# Create a radio button for Marital Status
rad_MARITAL = col2.radio(
    "What is your current marital status?",
    [
        "Married",
        "Divorced",
        "Widowed",
        "Separated",
        "Never married",
        "A member of an unmarried couple",
    ],
    index=0,
)
MARITAL_2 = 0
MARITAL_5 = 0
if rad_MARITAL == "Divorced":
    MARITAL_2 = 1
elif rad_MARITAL == "Never married":
    MARITAL_5 = 1


# List of user inputs in the order of the model for prediction
lst_inputs = [
    GENHLTH,
    PHYSHLTH,
    MENTHLTH,
    PERSDOC3,
    MEDCOST1,
    CHECKUP1,
    SLEPTIM1,
    CVDCRHD4,
    CVDSTRK3,
    CHCOCNC1,
    CHCCOPD3,
    ADDEPEV3,
    CHCKDNY2,
    DIABETE4,
    EDUCA,
    VETERAN3,
    CHILDREN,
    INCOME3,
    DECIDE,
    DIFFALON,
    COVIDPOS,
    PREDIAB2,
    CNCRDIFF,
    LSATISFY,
    EMTSUPRT,
    SDHISOLT,
    SDHEMPLY,
    FOODSTMP,
    SDHFOOD1,
    SDHBILLS,
    SDHUTILS,
    SDHTRNSP,
    SDHSTRE1,
    QSTLANG,
    _METSTAT,
    _URBSTAT,
    _HLTHPLN,
    _TOTINDA,
    _DRDXAR2,
    _SEX,
    _AGE80,
    HTM4,
    WTKG3,
    _BMI5,
    _RFBING6,
    _DRNKWK2,
    _RFDRHV8,
    _ASTHMS1_2,
    _ASTHMS1_3,
    RENTHOM1_1,
    RENTHOM1_3,
    _BMI5CAT_1,
    _BMI5CAT_2,
    _BMI5CAT_3,
    _RACEPR1_2,
    _RACEPR1_3,
    _RACEPR1_4,
    _RACEPR1_5,
    _RACEPR1_6,
    _RACEPR1_7,
    _SMOKGRP_1,
    _SMOKGRP_3,
    EMPLOY1_3,
    EMPLOY1_5,
    EMPLOY1_7,
    EMPLOY1_8,
    MARITAL_2,
    MARITAL_5,
]

# Custom CSS for the button
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: red;
        color: white;
        font-size: 10px;
        font-weight: bold;
        font-family: Arial;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create the prediction button
if st.button(
    "Predict risk of heart attack",
    key="predict_button",
    help="Button to trigger the prediction",
):
    # Assuming `predict` is your function and `lst_inputs` is your input list
    prediction = predict([lst_inputs])

    # Display the prediction with custom styling
    st.markdown(
        f"<h3 style='font-family:Arial; font-weight:bold; font-size: 20px;'>The predicted risk of heart attack is: {prediction}</h3>",
        unsafe_allow_html=True,
    )
