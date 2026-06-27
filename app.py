# -*- coding: utf-8 -*-
import streamlit as st
from datetime import datetime

# إعداد الصفحة لتكون بتنسيق واسع
st.set_page_config(page_title="منصة نبراس الذكية", page_icon="🩺")

# 1. الدالة الحسابية
def calculate_egfr(creatinine, age, gender):
    if gender == "أنثى":
        kappa, alpha, gender_factor = 0.7, -0.241, 1.012
    else:
        kappa, alpha, gender_factor = 0.9, -0.302, 1.0
    if creatinine <= 0: return 0
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# 2. الواجهة الأمامية بتصميم منظم
st.title("🩺 منصة نبراس الذكية")
st.subheader("تحليل وظائف الكلى الدقيق")
st.markdown("---")

# استخدام أعمدة لتنظيم المدخلات
col1, col2 = st.columns(2)
with col1:
    creatinine = st.number_input("الكرياتينين (mg/dL) 🧪", min_value=0.0, format="%.2f")
    gender = st.selectbox("الجنس 👤", ["ذكر", "أنثى"])
with col2:
    age = st.number_input("العمر 📅", min_value=0, max_value=120)
    st.write("") # فراغ للتنسيق
    has_diabetes = st.checkbox("مرض السكري 🍬")
    has_hypertension = st.checkbox("ارتفاع ضغط الدم 🩸")

# 3. معالجة التحليل
if st.button("تحليل الحالة الآن 🔍"):
    if creatinine > 0 and age > 0:
        result = calculate_egfr(creatinine, age, gender)
        
        # عرض النتيجة في إطار
        st.metric(label="معدل الترشيح الكبيبي (eGFR)", value=f"{result} ml/min")
        
        if result >= 90:
            st.success("النتيجة: وظائف الكلى طبيعية ✅")
        elif 60 <= result < 90:
            st.warning("النتيجة: انخفاض طفيف ⚠️")
        elif 30 <= result < 60:
            st.error("النتيجة: انخفاض متوسط 🚨")
        else:
            st.error("النتيجة: حالة حرجة 🆘")
            
        # إنشاء التقرير
        report_text = f"تقرير منصة نبراس - {datetime.now().strftime('%Y-%m-%d')}\n\n"
        report_text += f"العمر: {age}\nالجنس: {gender}\nالكرياتينين: {creatinine}\nالنتيجة (eGFR): {result}\n"
        
        st.download_button("📥 تحميل التقرير الطبي", report_text.encode('utf-8-sig'), "report.txt")
    else:
        st.error("يرجى إدخال قيم صحيحة.")

st.markdown("---")
st.caption("⚠️ إخلاء مسؤولية: هذه الأداة للاسترشاد فقط. يرجى مراجعة الطبيب المختص.")





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



