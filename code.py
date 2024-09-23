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

# Input fields for the 7 features
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20)
glucose = st.number_input('Glucose Level', min_value=0, max_value=200)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100)
insulin = st.number_input('Insulin Level', min_value=0, max_value=900)
bmi = st.number_input('Body Mass Index (BMI)', min_value=0.0, max_value=60.0)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5)

# Prediction button
if st.button('Predict'):
    result = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree)
    if result == 1:
        st.success('You have a high risk of diabetes.')
    else:
        st.success('You have a low risk of diabetes.')
