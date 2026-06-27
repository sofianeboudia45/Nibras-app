# -*- coding: utf-8 -*-
import streamlit as st
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس الذكية", page_icon="🩺")

# دالة الحساب
def calculate_egfr(creatinine, age, gender):
    kappa, alpha, gender_factor = (0.7, -0.241, 1.012) if gender == "أنثى" else (0.9, -0.302, 1.0)
    if creatinine <= 0: return 0
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# تهيئة ذاكرة الجلسة لحفظ النتائج
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🩺 منصة نبراس الذكية")
st.subheader("تحليل ومقارنة وظائف الكلى")
st.markdown("---")

# المدخلات
col1, col2 = st.columns(2)
with col1:
    creatinine = st.number_input("الكرياتينين (mg/dL) 🧪", min_value=0.0, format="%.2f")
    gender = st.selectbox("الجنس 👤", ["ذكر", "أنثى"])
with col2:
    age = st.number_input("العمر 📅", min_value=0, max_value=120)
    st.write("") 
    st.write("") 
    if st.button("تحليل الحالة الآن 🔍"):
        if creatinine > 0 and age > 0:
            result = calculate_egfr(creatinine, age, gender)
            # إضافة النتيجة إلى التاريخ
            entry = {"date": datetime.now().strftime("%H:%M"), "eGFR": result}
            st.session_state.history.append(entry)
            
            st.metric(label="معدل الترشيح الكبيبي (eGFR)", value=f"{result} ml/min")
        else:
            st.error("يرجى إدخال قيم صحيحة.")

# عرض المقارنة والتاريخ
if st.session_state.history:
    st.markdown("### 📊 سجل النتائج في هذه الجلسة")
    # عرض النتائج في جدول بسيط
    st.table(st.session_state.history)
    
    if len(st.session_state.history) > 1:
        st.info(f"تم تسجيل {len(st.session_state.history)} فحوصات. يمكنك مقارنة النتائج أعلاه.")
    
    if st.button("مسح السجل 🗑️"):
        st.session_state.history = []
        st.rerun()

st.markdown("---")
st.caption("⚠️ إخلاء مسؤولية: النتائج للاسترشاد فقط. يرجى مراجعة الطبيب.")
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



