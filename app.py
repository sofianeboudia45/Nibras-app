# -*- coding: utf-8 -*-
import streamlit as st
from datetime import datetime

# تعريف الدالة الحسابية
def calculate_egfr(creatinine, age, gender):
    if gender == "أنثى":
        kappa, alpha, gender_factor = 0.7, -0.241, 1.012
    else:
        kappa, alpha, gender_factor = 0.9, -0.302, 1.0
    
    if creatinine <= 0: return 0
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# إعداد واجهة التطبيق
st.title("منصة نبراس الذكية")
st.markdown("---")

# المدخلات
creatinine = st.number_input("أدخل مستوى الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
age = st.number_input("أدخل العمر", min_value=0)
gender = st.selectbox("أدخل الجنس", ["ذكر", "أنثى"])
has_diabetes = st.checkbox("Diabetes (مرض السكري)")
has_hypertension = st.checkbox("Hypertension (ارتفاع ضغط الدم)")

# منطق التحليل
if st.button("تحليل الحالة"):
    if creatinine > 0 and age > 0:
        result = calculate_egfr(creatinine, age, gender)
        st.metric(label="معدل الترشيح الكبيبي (eGFR)", value=f"{result} ml/min/1.73m²")
        
        # التقييم
        if result >= 90:
            status = "وظائف الكلى ضمن النطاق الطبيعي"
            st.success(f"النتيجة: {status}")
        elif 60 <= result < 90:
            status = "انخفاض طفيف في وظائف الكلى"
            st.warning(f"النتيجة: {status}")
        elif 30 <= result < 60:
            status = "انخفاض متوسط في وظائف الكلى"
            st.error(f"النتيجة: {status}")
        else:
            status = "حالة حرجة"
            st.error(f"النتيجة: {status}")
            
        # إعداد نص التقرير للتحميل
        report_text = f"تقرير منصة نبراس الذكية - {datetime.now().strftime('%Y-%m-%d')}\n\n"
        report_text += f"العمر: {age}\nالجنس: {gender}\nالكرياتينين: {creatinine}\n"
        report_text += f"النتيجة (eGFR): {result}\nالحالة: {status}\n"
        
        # زر التحميل
        st.download_button(
            label="تحميل التقرير كملف نصي",
            data=report_text,
            file_name="nibras_report.txt",
            mime="text/plain"
        )
    else:
        st.error("يرجى إدخال قيم صحيحة.")

st.markdown("---")
st.caption("تنبيه: هذه المنصة لأغراض استرشادية فقط ولا تغني عن استشارة الطبيب المختص.")



        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



