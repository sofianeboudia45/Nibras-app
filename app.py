# -*- coding: utf-8 -*-
import streamlit as st

# تعريف الدالة الحسابية (معادلة CKD-EPI)
def calculate_egfr(creatinine, age, gender):
    if gender == "أنثى":
        kappa, alpha, gender_factor = 0.7, -0.241, 1.012
    else:
        kappa, alpha, gender_factor = 0.9, -0.302, 1.0
    
    if creatinine <= 0: return 0
    
    # المعادلة العلمية
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# إعداد واجهة التطبيق
st.title("منصة نبراس الذكية")
st.markdown("---")

# المدخلات
creatinine = st.number_input("أدخل مستوى الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
age = st.number_input("أدخل العمر", min_value=0)
gender = st.selectbox("أدخل الجنس", ["ذكر", "أنثى"])

# عوامل المخاطر
has_diabetes = st.checkbox("Diabetes (مرض السكري)")
has_hypertension = st.checkbox("Hypertension (ارتفاع ضغط الدم)")

# منطق التحليل عند الضغط على الزر
if st.button("تحليل الحالة"):
    if creatinine > 0 and age > 0:
        result = calculate_egfr(creatinine, age, gender)
        
        # عرض النتيجة بشكل احترافي
        st.metric(label="معدل الترشيح الكبيبي (eGFR)", value=f"{result} ml/min/1.73m²")
        
        # التقييم والتوصية
        if result >= 90:
            st.success("النتيجة: وظائف الكلى ضمن النطاق الطبيعي.")
            st.write("حافظ على نمط حياة صحي واشرب كميات كافية من الماء.")
        elif 60 <= result < 90:
            st.warning("النتيجة: انخفاض طفيف في وظائف الكلى.")
            st.write("ننصح بمراقبة الضغط والسكر وإجراء فحص دوري كل 6 أشهر.")
        elif 30 <= result < 60:
            st.error("النتيجة: انخفاض متوسط في وظائف الكلى.")
            st.write("يجب استشارة طبيب كلى لإجراء فحوصات تأكيدية.")
        else:
            st.error("النتيجة: حالة حرجة.")
            st.write("يرجى مراجعة الطبيب المختص أو الطوارئ فوراً.")
            
        # ملاحظة إضافية بناءً على التاريخ المرضي
        if has_diabetes or has_hypertension:
            st.info("ملاحظة: وجود السكري أو الضغط مع هذه النتائج يتطلب متابعة طبية دقيقة.")
            
    else:
        st.error("يرجى إدخال قيم صحيحة للكرياتينين والعمر.")

# إخلاء المسؤولية
st.markdown("---")
st.caption("تنبيه: هذه المنصة لأغراض استرشادية فقط ولا تغني عن استشارة الطبيب المختص.")


        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



