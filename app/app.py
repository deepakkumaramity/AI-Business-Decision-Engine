import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("../models/model.pkl", "rb"))

st.title("AI Business Decision Engine")

income = st.number_input("Income")
loan = st.number_input("Loan Amount")

if st.button("Predict"):
    data = np.array([[income, loan]])
    result = model.predict(data)

    if result[0] == 1:
        st.error("High Risk Customer")
    else:
        st.success("Low Risk Customer")
