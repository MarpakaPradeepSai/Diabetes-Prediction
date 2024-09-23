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
st.write('Enter the details below to check if you have diabetes.')

# Input fields for the first 6 features organized in columns
col1, col2, col3 = st.columns(3)

with col1:
    pregnancies = st.text_input('Pregnancies', '')
    blood_pressure = st.text_input('Blood Pressure', '')
    diabetes_pedigree = st.text_input('Diabetes Pedigree Function', '')

with col2:
    glucose = st.text_input('Glucose Level', '')
    skin_thickness = st.text_input('Skin Thickness', '')

with col3:
    insulin = st.text_input('Insulin Level', '')
    bmi = st.text_input('Body Mass Index (BMI)', '')

# Convert inputs to appropriate types, treating empty inputs as None
pregnancies = int(pregnancies) if pregnancies else None
glucose = float(glucose) if glucose else None
blood_pressure = float(blood_pressure) if blood_pressure else None
skin_thickness = float(skin_thickness) if skin_thickness else None
insulin = float(insulin) if insulin else None
bmi = float(bmi) if bmi else None
diabetes_pedigree = float(diabetes_pedigree) if diabetes_pedigree else None

# Add custom CSS to change button color without hover or active effect
st.markdown("""
    <style>
    .stButton > button {
        background-color: #007bff; /* Bootstrap primary blue */
        color: white; /* Text color */
        border: none;
        transition: background-color 0s; /* No transition on click */
    }
    .stButton > button:focus,
    .stButton > button:active,
    .stButton > button:hover {
        outline: none; /* Remove focus outline */
        background-color: #007bff; /* Keep blue color on focus and active */
        color: white; /* Keep text color */
    }
    </style>
    """, unsafe_allow_html=True)

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
