import streamlit as st
import pandas as pd
import os

# 1. إعداد واجهة الإدخال
name = st.text_input("اسم المريض")
creatinine = st.number_input("الكرياتينين", min_value=0.0, format="%.2f")
age = st.number_input("العمر", min_value=0.0, format="%.2f")
gender = st.selectbox("الجنس", ["ذكر", "أنثى"])

# 2. كود الحفظ البسيط
if st.button("حفظ في السحابة"):
    # تجهيز البيانات
    data = {
        "اسم المريض": [name],
        "الكرياتينين": [creatinine],
        "العمر": [age],
        "الجنس": [gender]
    }
    df = pd.DataFrame(data)
    
    # حفظ البيانات في ملف CSV
    file_path = 'patients_data.csv'
    
    # إذا كان الملف موجوداً نضيف عليه البيانات، إذا لم يكن موجوداً ننشئه
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        
    st.success("تم حفظ البيانات بنجاح في الملف!")



            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



