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
    # استبدل سطر safe_name بهذا السطر المباشر safe_name = name 
    pdf.cell(200, 10, txt=f"Name: {safe_name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Glucose Level: {glucose}", ln=True)
    pdf.cell(200, 10, txt=f"Result: {result}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    name = st.text_input("اسم المريض")
    age = st.number_input("العمر", value=30)
    glucose = st.number_input("مستوى السكر", value=100)
    predict_btn = st.button("تحليل وحفظ النتيجة")

if predict_btn and name:
    result = "Needs Consultation" if glucose > 140 else "Normal"
    new_data = pd.DataFrame({"Name": [name], "Age": [age], "Glucose": [glucose], "Result": [result]})
    if os.path.exists("patients_data.csv"):
        new_data.to_csv("patients_data.csv", mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        new_data.to_csv("patients_data.csv", index=False, encoding='utf-8-sig')
    st.success(f"Analysis for {name} completed!")
    pdf_data = create_pdf(name, age, glucose, result)
    st.download_button("📥 Download Report as PDF", data=pdf_data, file_name=f"{name}_report.pdf", mime="application/pdf")

st.markdown("---")
# العرض - كود محدث لتجنب KeyError
st.markdown("---")
st.subheader("📊 Dashboard")
if os.path.exists("patients_data.csv"):
    df = pd.read_csv("patients_data.csv")
    
    # التأكد من أن الأعمدة هي باللغة الإنجليزية كما نستخدمها في التطبيق
    expected_columns = ["Name", "Age", "Glucose", "Result"]
    
    # إذا كانت الأعمدة في الملف القديم لا تطابق الأسماء المطلوبة، سنحذف الملف ونعيد تحميل الصفحة
    if list(df.columns) != expected_columns:
        os.remove("patients_data.csv")
        st.rerun()
    else:
        # عرض الرسم البياني والجدول إذا كانت البيانات صحيحة
        st.bar_chart(df.set_index("Name")["Glucose"])
        st.table(df)
        




    

    
    
    
    



