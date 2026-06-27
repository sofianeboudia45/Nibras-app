import streamlit as st
import pandas as pd
import os
from fpdf import FPDF

def create_pdf(name, age, glucose, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Nibras Smart Platform Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Name: Patient", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Glucose Level: {glucose}", ln=True)
    pdf.cell(200, 10, txt=f"Result: {result}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

st.set_page_config(page_title="Nibras Platform", layout="wide")
st.title("🩺 Nibras Smart Platform")

with st.sidebar:
    st.header("Patient Data")
    name = st.text_input("Name")
    age = st.number_input("Age", value=30)
    glucose = st.number_input("Glucose", value=100)
    predict_btn = st.button("Analyze and Save")

if predict_btn:
    result = "Needs Consultation" if glucose > 140 else "Normal"
    new_data = pd.DataFrame({"Name": [name], "Age": [age], "Glucose": [glucose], "Result": [result]})
    if os.path.exists("patients_data.csv"):
        new_data.to_csv("patients_data.csv", mode='a', header=False, index=False)
    else:
        new_data.to_csv("patients_data.csv", index=False)
    st.success("Analysis completed!")
    pdf_data = create_pdf(name, age, glucose, result)
    st.download_button("Download Report", data=pdf_data, file_name="report.pdf", mime="application/pdf")

st.markdown("---")
st.subheader("Dashboard")
if os.path.exists("patients_data.csv"):
    df = pd.read_csv("patients_data.csv")
    st.table(df)
    





    

    
    
    
    



