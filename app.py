import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="نبراس", page_icon="🩺")
st.title("🩺 منصة نبراس الذكية")

# إدخال البيانات
age = st.number_input("العمر", 0, 120, 30)
glucose = st.number_input("السكر", 50, 400, 100)
bp = st.number_input("ضغط الدم", 50, 200, 120)

if st.button("حفظ البيانات"):
    result = "آمن" if (glucose < 125 and bp < 140) else "تحذير"
    
    # إنشاء صف جديد للبيانات
    new_data = pd.DataFrame([[age, glucose, bp, result]], 
                            columns=["Age", "Glucose", "BP", "Result"])
    
    # حفظ البيانات في ملف CSV
    if os.path.exists('patients.csv'):
        new_data.to_csv('patients.csv', mode='a', header=False, index=False)
    else:
        new_data.to_csv('patients.csv', index=False)
        
    st.success("تم حفظ البيانات بنجاح!")

# عرض البيانات
if os.path.exists('patients.csv'):
    st.write("### سجل المرضى:")
    st.table(pd.read_csv('patients.csv'))
    
    



