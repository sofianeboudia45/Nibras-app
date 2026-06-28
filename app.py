import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
from fpdf import FPDF

# إعداد قاعدة البيانات
def init_db():
    conn = sqlite3.connect('nibras_records.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (date TEXT, name TEXT, gender TEXT, age REAL, creatinine REAL, glucose REAL, egfr REAL)''')
    conn.commit()
    conn.close()

init_db()

# دالة PDF معدلة لتجنب الخطأ
def create_pdf(name, age, gender, creatinine, glucose, egfr):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Nibras Medical Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    # تصفية الاسم من أي حروف عربية لمنع الخطأ في 2121.jpg
    safe_name = "".join([c if ord(c) < 128 else "" for c in name])
    pdf.cell(200, 10, txt=f"Patient: {safe_name} | Age: {age} | Gender: {gender}", ln=True)
    pdf.cell(200, 10, txt=f"Creatinine: {creatinine} mg/dL | Glucose: {glucose} mg/dL", ln=True)
    pdf.cell(200, 10, txt=f"eGFR: {egfr} mL/min/1.73m2", ln=True)
    return pdf.output(dest='S').encode('latin-1')

# دالة الحساب
def calculate_egfr(creatinine, age, gender):
    k = 0.7 if gender == 'female' else 0.9
    alpha = -0.241 if (gender == 'female' and creatinine <= k) else (-1.200 if (gender == 'female' and creatinine > k) else (-0.302 if creatinine <= k else -1.200))
    a = 144 if gender == 'female' else 141
    return round(a * ((creatinine / k) ** alpha) * (0.9938 ** age), 2)

# الواجهة
st.title("نبراس - أداة التحليل السريري 🩺")

tab1, tab2 = st.tabs(["تحليل جديد", "سجل المرضى 📋"])

with tab1:
    patient_name = st.text_input("اسم المريض")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر (سنة)", min_value=0, value=50)
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, value=1.0, step=0.01)
    glucose = st.number_input("نسبة السكر (mg/dL)", min_value=0.0, value=90.0)
    
    if st.button("تحليل الحالة 🔬"):
        gender_en = 'male' if gender == "ذكر" else 'female'
        egfr = calculate_egfr(creatinine, age, gender_en)
        st.metric(label="eGFR", value=f"{egfr} mL/min/1.73m²")
        
        # زر تحميل PDF
        pdf_data = create_pdf(patient_name, age, gender, creatinine, glucose, egfr)
        st.download_button("تحميل التقرير PDF 📄", data=pdf_data, file_name="report.pdf")

with tab2:
    if st.button("تحديث السجلات 🔄"):
        conn = sqlite3.connect('nibras_records.db')
        df = pd.read_sql_query("SELECT * FROM patients", conn)
        conn.close()
        st.dataframe(df)
    
