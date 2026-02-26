import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('breast_cancer_model.pkl', 'rb'))

st.title("Breast Cancer Prediction App")

st.write("Enter values below")

radius_mean = st.number_input("Radius Mean")
texture_mean = st.number_input("Texture Mean")
perimeter_mean = st.number_input("Perimeter Mean")

if st.button("Predict"):
    input_data = np.array([[radius_mean, texture_mean, perimeter_mean]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Malignant")
    else:
        st.success("Benign")
