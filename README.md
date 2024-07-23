# siads_capstone
Capstone repo for SIADS Summer 2024 student group of Anuvrat, Deepak and Noah

Introduction

In this Capstone project we want to experiment with different machine learning models which can help best predict the likelihood of a person being susceptible to a chronic health condition like Cardiovascular disease/diabetes/COPD based on risk factors such as smoking, high blood pressure, high cholesterol, unhealthy diet, lack of exercise, obesity, use of alcohol etc. We have chosen the Behavioral Risk Factor Surveillance System (BRFSS) data set which is a telephonic survey of US residents conducted by CDC every year about their health-related risk behaviors, chronic health conditions and use of preventive services. This dataset has information about individual survey respondents on various health dimensions such as their health status, access to healthcare, exercise, demographics, tobacco use, alcohol consumption, healthy eating habits etc. The dataset also provides their current chronic health conditions.

Methods section 

Data cleanup: We will do a cleanup of the data wherever required by data imputation, scaling and encoding.
Feature selection: We are planning to analyze the medical literature on the most likely risk factors for a given chronic condition. We will choose these risk factors as features from the BRFSS dataset and the chronic condition as target variable. We will validate the dataset if there are reasonable correlations between these variables and the chosen risk factors within the BRFSS dataset. We will use unsupervised machine learning techniques to find the most important predictors from the dataset.
Build model: We will choose a suitable supervised model which will be trained on the BRFSS dataset where it will use the selected features to predict the target variable.
Validation: We will select the appropriate metrics to measure the performance of our model and also test using different validation methods.

Results

We will elaborate the methods to arrive at our final model and also include the performance metrics and test results.

