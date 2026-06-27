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

# كود التطبيق
# (باقي الكود كما هو، أضف فقط جزء التحميل أدناه)
# بعد زر "تحليل وحفظ النتيجة" مباشرة داخل if predict_btn:

# في مكان عرض النتيجة (بعد عملية التحليل والحفظ)
if predict_btn and name:
    # ... (كود الحفظ السابق) ...
    
    # زر تحميل التقرير
    pdf_data = create_pdf(name, age, glucose, result)
    st.download_button(
        label="📥 تحميل التقرير كـ PDF",
        data=pdf_data,
        file_name=f"{name}_report.pdf",
        mime="application/pdf"
    )
    
    
    



    

    
    
    
    



