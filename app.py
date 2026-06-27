import streamlit as st
import pandas as pd
import os
from fpdf import FPDF
import re

# دالة إنشاء الـ PDF
def create_pdf(name, age, glucose, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Nibras Smart Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    
    # تنظيف الاسم: إزالة أي حروف غير لاتينية (عربية) لتجنب الخطأ
    clean_name = re.sub(r'[^\x00-\x7F]+', '', name)
    if not clean_name: clean_name = "Patient"
    
    pdf.cell(200, 10, txt=f"Name: {clean_name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Glucose Level: {glucose}", ln=True)
    pdf.cell(200, 10, txt=f"Result: {result}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")
st.markdown("<h1 style='text-align: center;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ بيانات المريض")
    name = st.text_input("اسم المريض")
    age = st.number_input("العمر", value=30)
    glucose = st.number_input("مستوى السكر", value=100)
    predict_btn = st.button("تحليل وحفظ")

if predict_btn and name:
    result = "يحتاج استشارة" if glucose > 140 else "طبيعي"
    new_data = pd.DataFrame({"الاسم": [name], "العمر": [age], "السكر": [glucose], "النتيجة": [result]})
    
    if os.path.exists("patients_data.csv"):
        new_data.to_csv("patients_data.csv", mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        new_data.to_csv("patients_data.csv", index=False, encoding='utf-8-sig')
        
    st.success(f"تم تحليل بيانات {name}!")
    pdf_data = create_pdf(name, age, glucose, result)
    st.download_button("📥 تحميل التقرير PDF", data=pdf_data, file_name="report.pdf", mime="application/pdf")

st.markdown("---")
st.subheader("📊 لوحة التحكم")
if os.path.exists("patients_data.csv"):
    df = pd.read_csv("patients_data.csv", encoding='utf-8-sig')
    st.table(df)
    
    
    
    





    

    
    
    
    



