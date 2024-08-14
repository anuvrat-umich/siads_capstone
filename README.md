# Risk Pulse - Developed by Team DNA (August 2024)

Capstone repository for SIADS Summer 2024 Team DNA (Deepak, Noah, Anuvrat) @ University of Michigan, School of Information, Ann Arbor, MI, USA.

Page modified on : 2024 August, 13

## Table of Contents

- [Introduction](#introduction)
- [Application](#application)
- [Technical details](#technical-details)
- [Tech stack](#tech-stack)
- [Folder structure](#folder-structure)
- [Installation](#installation)
- [Data](#data)
- [Methods](#methods)
- [Discussion](#discussion)
- [Contributors](#contributors)

## Introduction

Risk Pulse is an application to predict risk of Heart Attack / Myocardial Infarction based on few user inputs including demographic information such as age, gender, height, weight, history of angina or coronary heart disease, diabetes, lack of exercise, obesity, smoking, use of alcohol, health status, and other comorbidities. It takes user ~5 minutes to provide the inputs. The prediction takes place within a second. The prediction is done using an experimental, educational Machine Learning model built using public data and should not be considered medical advice. Please consult your doctor or a health care professional to talk about your situation.

## Application

The application can be accessed at [Risk Pulse](https://myocardial-infarction.streamlit.app/). The application works equally well on traditional computing devices (laptop/desktop) and mobile devices (ipad/iphone/android). It may take a couple of seconds to open the first time you click the link. The user is asked a total of 50 questions (42 radio buttons, 8 sliders). However, the application is pre-filled for an "average" respondent using historical median values for each specific question to help the user easily fill the form.

<b>[../src/streamlit.py](https://github.com/anuvrat-umich/siads_capstone/blob/main/src/streamlit.py) </b> contains the code base to develop the application. The background for the application is saved under [../appdata](https://github.com/anuvrat-umich/siads_capstone/tree/main/appdata). Streamlit configuration file is saved under [../.streamlit/config.toml](https://github.com/anuvrat-umich/siads_capstone/blob/main/.streamlit/config.toml).

## Technical details

The following sections will deal with the technical set up including tech stack, folder structure, data, Machine Learning methods used, result and discussion.

## Tech stack

We have used Python based tech stack. Raw databases were obtained in SAS format that were readily converted to Pandas DataFrame as pickled to optimize space as SAS file used a highly sparse .XPT format. The data is processed using pandas and imblearn packages. The models are developed in Python using scikit-learn, xgboost and lightgbm packages. Matplolitb, seaborn and shap packages were used for visualization and explanation of results. Joblib is used to save and load models. Streamlit is used for final deployment.

## Folder Structure

        root
        ├── ...
        ├── .streamlit                              # Configuration file fro Streamlit application
        ├── appdata                                 # Media files for Streamlit application
        ├── data                                    # Data files to train the model
        │ ├── BRFSS2022_modeling_data.pkl           # ZIP file containing the final modeling data
        │ ├── BRFSS2022_raw.pkl                     # Raw pickled data
        ├── doc                                     # Documentation files to understand the data better
        │ ├── 2022-BRFSS-Questionnaire-508.pdf      # 2022 BRFSS Questionnaire
        │ ├── USCODE22_LLCP_102523.html             # Codebook
        ├── models                                  # Trained models
        │ ├── dt_model.pkl                          # Trained Decision Tree model
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

## Installation

To replicate the steps in the repository, use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages using requirements.txt file.

```bash
pip install -r requirements.txt
```

## Data

We have chosen the Behavioral Risk Factor Surveillance System (BRFSS) data set which is a telephonic survey of US residents conducted by the CDC every year about their health-related risk behaviors, chronic health conditions, and use of preventive services. The data can be downloaded from [CDC website](https://www.cdc.gov/brfss/annual_data/annual_2022.html)

We have used 2022 BRFSS Data (SAS Transport Format) for this project. As already stated, it is a highly uncompressed format. We have converted the raw data to a Pandas DataFrame and have included a pickled copy of the same in the repository under [../data/BRFSS2022_raw.pkl](https://github.com/anuvrat-umich/siads_capstone/blob/main/data/BRFSS2022_raw.pkl)

<b>Data access statement:</b> Generally, data and materials produced by federal agencies are in the public domain and may be reproduced without permission. However, we are asked that any published material derived from the data acknowledge CDC’s BRFSS as the original source. for public access and use, cited as "Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System Survey Data. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, 2022". For more information check response to #14 on the [FAQs page](https://www.cdc.gov/brfss/about/brfss_faq.htm).

## Data cleanup and feature engineering

<b>[../src/load_data.ipynb](https://github.com/anuvrat-umich/siads_capstone/blob/main/src/load_data.ipynb):</b> This notebook reads the [../data/BRFSS2022_raw.pkl](https://github.com/anuvrat-umich/siads_capstone/blob/main/data/BRFSS2022_raw.pkl) and applies relevant data cleanup (dropping unwanted columns) and feature engineering (encoding some survey columns as binary, custom binning or one hot encoding) steps. Some of the reasons to drop columns included low fill rate, a lot of non-informative responses, and multicollinearity. We also dropped some records that had an abundance of non-informative responses (missing, not sure, don't know, etc.). Specific imputation methods including zero imputation, mean imputation, and majority class imputation were used for specific features. The file used downstream for modeling is saved as [../data/BRFSS2022_modeling_data.pkl](https://github.com/anuvrat-umich/siads_capstone/blob/main/data/BRFSS2022_modeling_data.pkl)

## Methods

<b>[../src/model.ipynb](https://github.com/anuvrat-umich/siads_capstone/blob/main/src/model.ipynb):</b> We have experimented with various modelling techniques in this notebook. The first step is to clean up the data and experiment with under/oversampling. The next step is to train and evaluate different machine learning models across various families - including linear models (logistic regression), Decision Trees, and tree based ensembles (Random Forest, XGBoost, Light GBM). The notebook follows a fixed structure with similar blocks appearing for each model category.

We have used Grid Search and Random Search to find out the best hyperparameters for each model family, using 3-5 fold cross validation.

We have evaluated models based on similar evaluation criteria - including precision, recall, and AUC. We aim to improve overall model performance by addressing the precision-recall trade-off. Our models demonstrated high recall but low precision. Given this, we've opted to use precision as the scoring function to strike a better balance. Although high recall is crucial for disease prediction because the consequences of false negatives (missing critical patients at risk of heart attack) are significantly more critical than those of false positives (raising some false alarms).

The best models across each model family were pickled and saved at the end of workbook under [../models](https://github.com/anuvrat-umich/siads_capstone/tree/main/models). Random Forest model has been saved as a zip file as it was too big to save without compressing.

## Discussion

Heart disease is the leading cause of death for men, women, and people of most racial and ethnic groups. In the United States, someone has a heart attack every 40 seconds. About 1 in 5 heart attacks are silent—the damage is done, but the person is not aware of it. All of these facts are taken from [CDC](https://www.cdc.gov/heart-disease/data-research/facts-stats/index.html). Early identification of risks of heart attack is critical to minimize the damage and possibly work towards making better lifestyle choices that can reduce the risk itself.

Through this work we present users with the ability to run what-if scenarios to gauge their potential risk of a heart attack. It is important to note, many of the risk factors our outside a patients ability to control.

Now this is in itself not a novel problem or a solution thereof, but public access to such solutions remain limited. For example, we tried to use Cleveland Clinic's [ASCVD risk calculator ](https://my.clevelandclinic.org/health/articles/17085-heart-risk-factor-calculators) but the page has been down for maintenance as last reported. Moreover, transparency, interpretability, explanability and public accesss to data and methodologies remain major challenges. We have open sourced our work under public GNU license including the data and model.

We found that prior history of Angina, Stroke and an advanced age and BMI are important risk factors for myocaridal infarction. We also found some demographic risk factors including gender and race. We also found some correlated (but not causal features) including socio economic factors such as employment, educational and marital status.

We would ideally want to understand the ethical concerns associated with such predictions better. Although, the application is designed to be personalized and it not designed to compare one group against another, it can be used to do so. It can perpetuate percepctions. For example, everything else remaining same, we found that the Asians have a lower risk prediction compared to other races. [CDC](https://www.cdc.gov/heart-disease/data-research/facts-stats/index.html) data doesn't support this. But more importantly, can a application like this create perception that in turn lead to a particular section of the populace being disadvantaged is an important ethical concern. There has been ample research on this topic concerning mental stress among Af-Am population in US including this [ncbi paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4406484/). However, this risk needs to be weighed against the potential public health benefits.

Future enhancements to this tool can include addition of interpretability or explanability directly in the Risk Pulse application so that individuals can understand the factors leading to the high risk they have, or vice versa what's working for them and keeping the risk levels low.

## Contributors

The project has been initiated by [Deepak Prabhu](https://github.com/Better-tomorrow), [Noah Chasse](https://github.com/nchasse) and [Anuvrat Chaturvedi](https://github.com/anuvrat-umich) under the guidance of [Michelle LeBlanc](https://github.com/michelledleblanc).
