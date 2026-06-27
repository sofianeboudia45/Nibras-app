import streamlit as st
import pandas as pd
import os

# إعداد الصفحة
st.set_page_config(page_title="نبراس - الجزائر", page_icon="🇩🇿")

# العنوان
st.title("🇩🇿 بوابة نبراس الصحية")
st.subheader("نظام متابعة وتقييم حالة المرضى")
st.markdown("---")

# تقسيم المدخلات لتنظيم الواجهة
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("اسم المريض")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    # إضافة خانة اختيار الحالة
    status = st.selectbox("حالة المريض الصحية", ["مستقرة", "جيدة", "تحت المراقبة", "حرجة"])

with col2:
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
    age = st.number_input("العمر (سنة)", min_value=0.0, format="%.1f")

# زر الحفظ
if st.button("💾 حفظ البيانات"):
    data = {
        "اسم المريض": [name],
        "الكرياتينين": [creatinine],
        "العمر": [age],
        "الجنس": [gender],
        "الحالة الصحية": [status] # إضافة الحالة للبيانات المحفوظة
    }
    df = pd.DataFrame(data)
    
    file_path = 'patients_data.csv'
    
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        
    st.success(f"تم حفظ بيانات المريض ({name}) بنجاح بحالة: {status}")

# إضافة تذييل
st.markdown("---")
st.caption("نبراس - صنع في الجزائر بفخر 🇩🇿")


    
    



            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



