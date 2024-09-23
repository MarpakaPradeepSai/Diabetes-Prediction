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
st.title('Diabetes Prediction App 🩺🍩')
st.write('Enter the details below to check if you have diabetes. 📝')

# Input fields for the first 7 features organized in columns
col1, col2, col3 = st.columns(3)

with col1:
    pregnancies = st.text_input('Pregnancies 👶', '')
    blood_pressure = st.text_input('Blood Pressure 🩸', '')
    diabetes_pedigree = st.text_input('Diabetes Pedigree Function 📊', '')

with col2:
    glucose = st.text_input('Glucose Level 💧', '')
    skin_thickness = st.text_input('Skin Thickness 🩹', '')

with col3:
    insulin = st.text_input('Insulin Level 💉', '')
    bmi = st.text_input('Body Mass Index (BMI) ⚖️', '')

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
        color: white !important; /* Text color */
        border: none;
        transition: none; /* Remove all transitions */
    }
    .stButton > button:focus,
    .stButton > button:active,
    .stButton > button:hover {
        outline: none; /* Remove focus outline */
        background-color: #007bff !important; /* Keep blue color on focus and active */
        color: white !important; /* Keep text color */
    }
    </style>
    """, unsafe_allow_html=True)

# Prediction button
if st.button('Predict🔎'):
    if None in [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree]:
        st.warning('⚠️ Please provide all fields.')
    else:
        result = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree)
        if result == 1:
            st.markdown("""
                <div style="background-color:red; padding:20px; color:white; text-align:center; border-radius:10px;">
                    <h3 style="color:black;">🚨 <strong>Warning!</strong></h3>
                    <p style="font-size:18px; color:white;">You have a <strong>high risk</strong> of diabetes.</p>
                    <p style="color:white;">It's time to take action! Consult a healthcare professional for advice on lifestyle changes.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background-color:green; padding:20px; color:white; text-align:center; border-radius:10px;">
                    <h3 style="color:black;">✅ <strong>Good News!</strong></h3>
                    <p style="font-size:18px; color:white;">You have a <strong>low risk</strong> of diabetes.</p>
                    <p style="color:white;">Keep up the healthy habits! Stay active and maintain a balanced diet.</p>
                </div>
            """, unsafe_allow_html=True)
