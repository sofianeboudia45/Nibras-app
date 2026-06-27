import streamlit as st
import pandas as pd
import os

# إعداد الصفحة مع أيقونة تعبر عن الصحة
st.set_page_config(page_title="نبراس - الجزائر", page_icon="🇩🇿")

# إضافة العلم الجزائري والعنوان
st.title("🇩🇿 بوابة نبراس الصحية")
st.subheader("نحو رعاية صحية أفضل")
st.markdown("---")

# استخدام الأعمدة لجعل الواجهة منظمة
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("اسم المريض")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])

with col2:
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
    age = st.number_input("العمر (سنة)", min_value=0.0, format="%.1f")

# زر الحفظ مع إضافة لمسة ترحيبية
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
        
    st.success("تم حفظ بيانات المريض بنجاح في سجلات نبراس!")

# إضافة تذييل بسيط
st.markdown("---")
st.caption("نبراس - صنع في الجزائر بفخر 🇩🇿")

    
    



            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



