import streamlit as st
import pandas as pd
import os

# إضافة عنوان وتنسيق للصفحة
st.title("📋 سجل بيانات المرضى")
st.markdown("---")

# استخدام الأعمدة لجعل الواجهة متناسقة
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("اسم المريض")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])

with col2:
    creatinine = st.number_input("الكرياتينين", min_value=0.0, format="%.2f")
    age = st.number_input("العمر", min_value=0.0, format="%.1f")

# زر الحفظ بتنسيق أفضل
if st.button("💾 حفظ البيانات"):
    data = {
        "اسم المريض": [name],
        "الكرياتينين": [creatinine],
        "العمر": [age],
        "الجنس": [gender]
    }
    df = pd.DataFrame(data)
    
    file_path = 'patients_data.csv'
    
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        
    st.success("تم حفظ البيانات بنجاح في السجل!")
    



            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



