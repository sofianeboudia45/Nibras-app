import streamlit as st
import pandas as pd
import os
from fpdf import FPDF

# الدالة الجديدة (بالإنجليزية لتجنب خطأ الترميز)
def create_pdf(name, age, glucose, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Nibras Smart Platform Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    # هذا السطر يضمن تحويل أي حروف عربية لعلامات استفهام لتجنب الخطأ
    safe_name = name.encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(200, 10, txt=f"Name: {safe_name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Glucose Level: {glucose}", ln=True)
    pdf.cell(200, 10, txt=f"Result: {result}", ln=True)
    return pdf.output(dest='S').encode('latin-1')
    




    

    
    
    
    



