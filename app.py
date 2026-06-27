import streamlit as st
import pandas as pd
import os
from fpdf import FPDF

# إعداد ملف PDF
def create_pdf(name, age, glucose, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="تقرير منصة نبراس الذكية", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"الاسم: {name}", ln=True)
    pdf.cell(200, 10, txt=f"العمر: {age}", ln=True)
    pdf.cell(200, 10, txt=f"مستوى السكر: {glucose}", ln=True)
    pdf.cell(200, 10, txt=f"النتيجة: {result}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)

# المدخلات
with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    name = st.text_input("اسم المريض")
    age = st.number_input("العمر", value=30)
    glucose = st.number_input("مستوى السكر", value=100)
    predict_btn = st.button("تحليل وحفظ النتيجة")

# المنطق والتحليل
if predict_btn:
    result = "تتطلب استشارة" if glucose > 140 else "طبيعية"
    
    # حفظ في ملف
    new_data = pd.DataFrame({"الاسم": [name], "العمر": [age], "السكر": [glucose], "النتيجة": [result]})
    if os.path.exists("patients_data.csv"):
        new_data.to_csv("patients_data.csv", mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        new_data.to_csv("patients_data.csv", index=False, encoding='utf-8-sig')
    
    st.success(f"تم تحليل حالة {name} بنجاح!")
    
    # زر التحميل
    pdf_data = create_pdf(name, age, glucose, result)
    st.download_button("📥 تحميل التقرير كـ PDF", data=pdf_data, file_name=f"{name}_report.pdf", mime="application/pdf")

# العرض
st.markdown("---")
st.subheader("📊 لوحة التحكم")
if os.path.exists("patients_data.csv"):
    df = pd.read_csv("patients_data.csv")
    st.bar_chart(df.set_index("الاسم")["السكر"])
    st.table(df)




    

    
    
    
    



