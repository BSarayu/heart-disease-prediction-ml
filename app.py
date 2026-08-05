import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title='Heart Disease Prediction',
    page_icon='❤️',
    layout='centered'
)

# Load model
model = joblib.load('src/rf_model.pkl')

# Title
st.title('❤️ Heart Disease Prediction System')
st.markdown('Predict the likelihood of heart disease using machine learning.')

st.divider()

# Input fields
age = st.number_input('Age', 20, 100, 50)
sex = st.selectbox('Sex', ['Female', 'Male'])
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', 80, 200, 120)
chol = st.number_input('Cholesterol', 100, 600, 200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
restecg = st.selectbox('Resting ECG', [0, 1, 2])
thalach = st.number_input('Maximum Heart Rate', 60, 220, 150)
exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
oldpeak = st.number_input('Oldpeak', 0.0, 10.0, 1.0)
slope = st.selectbox('Slope', [0, 1, 2])
ca = st.selectbox('Number of Major Vessels', [0, 1, 2, 3, 4])
thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

# Convert categorical inputs
sex = 1 if sex == 'Male' else 0
fbs = 1 if fbs == 'Yes' else 0
exang = 1 if exang == 'Yes' else 0

# Predict
if st.button('🔍 Predict', use_container_width=True):
    data = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak,
        slope, ca, thal
    ]])

    prediction = model.predict(data)[0]

    st.divider()

    if prediction == 1:
        st.error('⚠️ Heart Disease Detected')
    else:
        st.success('✅ No Heart Disease Detected')

st.divider()
st.caption('Built with Scikit-learn and Streamlit')