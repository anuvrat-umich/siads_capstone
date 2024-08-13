# siads_capstone - Team DNA (August 2024)

Capstone repo for SIADS Summer 2024 Team DNA (Deepak, Noah, Anuvrat)
Modified on : 2024 August, 13

## Table of Contents

- Introduction
- Data
- Installation
- Application use
  - Data cleanup and feature engineering
  - Models
  - Streamlit app
- Folder structure

- [Introduction](#introduction)
- [Application](#application)
- [Technical details](#technical-details)
- [Tech stack](#tech-stack)
- [Folder structure](#folder-structure)
- [Data](#data)
- [Methods](#methods)
- [Discussion](#discussion)
- [Contributors](#contributors)

# Introduction

Risk Pulse is an application to predict risk of Heart Attack / Myocardial Infarction based on few user inputs including demographic information and history of angina or coronary heart disease, smoking, high blood pressure, high cholesterol, unhealthy diet, lack of exercise, obesity, use of alcohol, and other comorbidities. It takes user ~5 minutes to provide the inputs. The prediction takes place within a second. The prediction is done using an experimental, educational Machine Learning model built using public data and should not be considered medical advice. Please consult your doctor or a health care professional to talk about your situation.

## Application

The application can be accessed at [Risk Pulse](#https://myocardial-infarction.streamlit.app/). The application works equally well on traditional computing devices (laptop/desktop) and mobile devices (ipad/iphone/android). It may take couple of seconds to open the first time you click the link. The user is asked total 50 questions (42 radio button, 8 sliders). However, the application is pre-filled for an "average" respondent using historical median values for each specific questions the user is asked to help the user.

## Technical details

The following sections will deal with the technical set up including tech stack, data, folder structure, Machine Learning methods used, result and discussion.

## Tech stack

We have used Python based tech stack. Raw databases were obtained in SAS format that were readily converted to Pandas DataFrame as pickled to optimize space as SAS file used a highly sparse .XPT format. The data is processed using pandas and imblearn packages. The models are developed in Python using scikit-learn, xgboost and lightgbm packages. Matplolitb, seaborn and shap packages were used for visualization and explanation of results. Joblib is used to save and load models. Streamlit is used for final deployment.

## Data

We have chosen the Behavioral Risk Factor Surveillance System (BRFSS) data set which is a telephonic survey of US residents conducted by the CDC every year about their health-related risk behaviors, chronic health conditions, and use of preventive services. We are using the BRFSS data to build a model to predict whether an individual has a high risk of having a heart attack.

The data can be downloaded from CDC website -> https://www.cdc.gov/brfss/annual_data/annual_2022.html

We have used 2022 BRFSS Data (SAS Transport Format) for this project.
A copy of raw data has been included in the repository ../data/BRFSS2022_raw.pkl

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Application Use

The first step is to clean up the data and run feature engineering steps. The next step is train and evaluate different machine learning models.

### Data cleanup and feature engineering

This notebook reads the BRFSS2022 raw data (found in data folder in pkl foramt ) and applies the data cleanup (drop the unwanted columns) and feature engineering (encoding survey data as binary or one hot encoding). The final output is saved as ../data/BRFSS2022_modeling_data.pkl

### Models

This notebook has all the steps for training and evaluation of various classification models.

### streamlit app

This file is just for reference and no need to run this. This is the code for the stremlit app which hosts the logistic regression model. User can input their health parameters and get the prediction on myocardial infraction. You can access the app here:

https://myocardial-infarction.streamlit.app/

### Folder Structure

        root
        ├── ...
        ├── .streamlit                              # Configuration file fro Streamlit application
        ├── appdata                                 # Media files for Streamlit application
        ├── data                                    # Data files to train the model
        │ ├── BRFSS2022_modeling_data.zip           # ZIP file containing the final modeling data
        │ ├── BRFSS2022_raw.pkl                     # Raw pickled data
        ├── doc                                     # Documentation files to understand the data better
        │ ├── 2022-BRFSS-Questionnaire-508.pdf      # 2022 BRFSS Questionnaire
        │ ├── USCODE22_LLCP_102523.html             # Codebook
        ├── models                                  # Trained models
        │ ├── lgbm_model.pkl                        # Trained LGBM model
        │ ├── lr_model.pkl                          # Trained Logistic Regression model
        │ ├── rf_model.zip                          # Trained Random Forest model (Unzipped>100MB)
        │ ├── xgb_model.pkl                         # Trained XGBoost model
        ├── src                                     # Source code
        │ ├── load_data.ipynb                       # Load input files for further processing
        │ ├── model.ipynb                           # Experiment with various modelling techniques including LR, RF, XGB, LGBM, DT
        │ ├── streamlit.py                          # Python code to create the Streamlit application
        ├── LICENSE                                 # GNU General Public License v3.0
        ├── README.md                               # This file with overview of the repository
        └── requirements.txt                        # Project dependencies
