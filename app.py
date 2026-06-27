# -*- coding: utf-8 -*-
import streamlit as st

# 1. تعريف الدالة الحسابية
def calculate_egfr(creatinine, age, gender):
    if gender == "أنثى":
        kappa, alpha, gender_factor = 0.7, -0.241, 1.012
    else:
        kappa, alpha, gender_factor = 0.9, -0.302, 1.0
    
    if creatinine <= 0: return 0
    
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# 2. الواجهة
st.title("منصة نبراس الذكية")

creatinine = st.number_input("أدخل مستوى الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
age = st.number_input("أدخل العمر", min_value=0)
gender = st.selectbox("أدخل الجنس", ["ذكر", "أنثى"])

# إضافة عوامل المخاطر باستخدام نصوص إنجليزية لتجنب أخطاء الترميز
has_diabetes = st.checkbox("Diabetes (مرض السكري)")
has_hypertension = st.checkbox("Hypertension (ارتفاع ضغط الدم)")

# 3. زر التحليل
if st.button("تحليل"):
    if creatinine > 0 and age > 0:
        result = calculate_egfr(creatinine, age, gender)
        
        st.write(f"### معدل الترشيح الكبيبي المقدر (eGFR): {result}")
        
        # التقييم
        if result >= 90:
            st.success("النتيجة: وظائف كلى ضمن النطاق الطبيعي.")
        elif 60 <= result < 90:
            st.warning("النتيجة: انخفاض طفيف في وظائف الكلى.")
        else:
            st.error("النتيجة: انخفاض في وظائف الكلى، يرجى مراجعة طبيب مختص.")
            
        # تنبيه إضافي
        if has_diabetes or has_hypertension:
            st.info("ملاحظة: وجود السكري أو الضغط مع هذه النتائج يتطلب متابعة طبية دقيقة.")
    else:
        st.error("يرجى إدخال بيانات صحيحة.")
        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



