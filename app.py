def create_pdf(name, age, glucose, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Nibras Smart Platform Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    # هذه النسخة لا تستخدم أي متغيرات معقدة لتجنب أي خطأ برمجي
    pdf.cell(200, 10, txt=f"Name: Patient", ln=True) 
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Glucose Level: {glucose}", ln=True)
    pdf.cell(200, 10, txt=f"Result: {result}", ln=True)
    return pdf.output(dest='S').encode('latin-1')





    

    
    
    
    



