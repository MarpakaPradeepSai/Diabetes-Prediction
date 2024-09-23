import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('best_naive_bayes_model.pkl')

# Function to make predictions using the 7 selected features
def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree):
    input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree]],
                               columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction'])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
st.title('Diabetes Prediction App')
st.write('Enter the details below to check if you have diabetes. Leave fields blank if you do not want to provide that information.')

# Input fields for the 7 features
pregnancies = st.text_input('Pregnancies', '')
glucose = st.text_input('Glucose Level', '')
blood_pressure = st.text_input('Blood Pressure', '')
skin_thickness = st.text_input('Skin Thickness', '')
insulin = st.text_input('Insulin Level', '')
bmi = st.text_input('Body Mass Index (BMI)', '')
diabetes_pedigree = st.text_input('Diabetes Pedigree Function', '')

# Convert inputs to appropriate types, treating empty inputs as None
pregnancies = int(pregnancies) if pregnancies else None
glucose = float(glucose) if glucose else None
blood_pressure = float(blood_pressure) if blood_pressure else None
skin_thickness = float(skin_thickness) if skin_thickness else None
insulin = float(insulin) if insulin else None
bmi = float(bmi) if bmi else None
diabetes_pedigree = float(diabetes_pedigree) if diabetes_pedigree else None

# Prediction button
if st.button('Predict'):
    if None in [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree]:
        st.warning('Please provide all fields or leave them blank if you prefer not to input a value.')
    else:
        result = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree)
        if result == 1:
            st.success('You have a high risk of diabetes.')
        else:
            st.success('You have a low risk of diabetes.')
