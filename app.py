import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
from fpdf import FPDF # مكتبة إنشاء الـ PDF

# دالة إنشاء ملف PDF
def create_pdf(name, age, gender, creatinine, glucose, egfr, interpretation):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Nibras Clinical Report - تقرير نبراس الطبي", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
    pdf.cell(200, 10, txt=f"Patient Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age} | Gender: {gender}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Creatinine: {creatinine} mg/dL | Glucose: {glucose} mg/dL", ln=True)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=f"Result (eGFR): {egfr} mL/min/1.73m2", ln=True)
    pdf.cell(200, 10, txt=f"Interpretation: {interpretation}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

# (بقية الدوال: init_db, calculate_egfr, get_egfr_interpretation كما هي في الكود السابق)
# ...

# في جزء الواجهة (tab1) عند التحليل:
    if st.button("تحليل الحالة 🔬"):
        # ... (حساب النتيجة) ...
        interpretation, status = get_egfr_interpretation(egfr)
        
        # عرض النتيجة
        st.metric("eGFR", f"{egfr} mL/min/1.73m²")
        
        # زر تحميل التقرير
        pdf_data = create_pdf(patient_name, age, gender, creatinine, glucose, egfr, interpretation)
        st.download_button(
            label="تحميل التقرير بصيغة PDF 📄",
            data=pdf_data,
            file_name=f"Report_{patient_name}.pdf",
            mime="application/pdf"
        )
        
        
