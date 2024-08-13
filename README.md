# siads_capstone - Team DNA (August 2024)

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


# Introduction

In this Capstone project, we experimented with different machine learning models to best predict the likelihood of a person being at risk for a based on risk factors such as history of angina or coronary heart disease, smoking, high blood pressure, high cholesterol, unhealthy diet, lack of exercise, obesity, use of alcohol, other comorbidities.

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

