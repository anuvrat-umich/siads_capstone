# siads_capstone - Team DNA (August 2024)

Capstone repo for SIADS Summer 2024 Team DNA (Deepak, Noah, Anuvrat)
Modified on : 2024 August, 13

## Table of Contents

- Introduction
- Application Use
- Technical details
- Folder structure
- Data Cleanup
- Methods
- Results
- Contributors

## Introduction

## Application Use

## Technical details

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

### Data cleanup

### Methods

### Results

### Contributors

Through this

In this Capstone project we want to experiment with different machine learning models which can help best predict the likelihood of a person being susceptible to a chronic health condition like Cardiovascular disease/diabetes/COPD based on risk factors such as smoking, high blood pressure, high cholesterol, unhealthy diet, lack of exercise, obesity, use of alcohol etc. We have chosen the Behavioral Risk Factor Surveillance System (BRFSS) data set which is a telephonic survey of US residents conducted by CDC every year about their health-related risk behaviors, chronic health conditions and use of preventive services. This dataset has information about individual survey respondents on various health dimensions such as their health status, access to healthcare, exercise, demographics, tobacco use, alcohol consumption, healthy eating habits etc. The dataset also provides their current chronic health conditions.

## Methods

Data cleanup: We will do a cleanup of the data wherever required by data imputation, scaling and encoding.
Feature selection: We are planning to analyze the medical literature on the most likely risk factors for a given chronic condition. We will choose these risk factors as features from the BRFSS dataset and the chronic condition as target variable. We will validate the dataset if there are reasonable correlations between these variables and the chosen risk factors within the BRFSS dataset. We will use unsupervised machine learning techniques to find the most important predictors from the dataset.
Build model: We will choose a suitable supervised model which will be trained on the BRFSS dataset where it will use the selected features to predict the target variable.
Validation: We will select the appropriate metrics to measure the performance of our model and also test using different validation methods.

## Results

We will elaborate the methods to arrive at our final model and also include the performance metrics and test results.
