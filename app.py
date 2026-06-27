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

# تهيئة ذاكرة الجلسة
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🩺 منصة نبراس الذكية")
st.subheader("تحليل وظائف الكلى - سجل المريض")
st.markdown("---")

# بيانات المريض الشخصية
patient_name = st.text_input("اسم المريض 👤")
patient_meds = st.text_area("الأدوية الحالية (إن وجدت) 💊")

# المدخلات الطبية
col1, col2 = st.columns(2)
with col1:
    creatinine = st.number_input("الكرياتينين (mg/dL) 🧪", min_value=0.0, format="%.2f")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
with col2:
    age = st.number_input("العمر 📅", min_value=0, max_value=120)
    if st.button("تحليل وإضافة للسجل 🔍"):
        if creatinine > 0 and age > 0:
            result = calculate_egfr(creatinine, age, gender)
            entry = {
                "التوقيت": datetime.now().strftime("%H:%M"), 
                "النتيجة (eGFR)": result
            }
            st.session_state.history.append(entry)
            st.success(f"تم تسجيل النتيجة: {result}")
        else:
            st.error("يرجى إدخال قيم صحيحة.")

# عرض السجل والتقرير
if st.session_state.history:
    st.markdown("### 📊 سجل النتائج")
    st.table(st.session_state.history)
    
    # نص التقرير المحدث
    report_text = f"تقرير منصة نبراس الذكية\n"
    report_text += f"التاريخ: {datetime.now().strftime('%Y-%m-%d')}\n"
    report_text += f"اسم المريض: {patient_name}\n"
    report_text += f"الأدوية: {patient_meds}\n"
    report_text += "-"*30 + "\n"
    for item in st.session_state.history:
        report_text += f"الوقت: {item['التوقيت']} | النتيجة: {item['النتيجة (eGFR)']} ml/min\n"
    
    st.download_button(
        label="📥 تحميل التقرير الكامل",
        data=report_text.encode('utf-8-sig'),
        file_name="nibras_medical_report.txt",
        mime="text/plain"
    )
    
    if st.button("مسح السجل 🗑️"):
        st.session_state.history = []
        st.rerun()

st.markdown("---")
st.caption("⚠️ إخلاء مسؤولية: هذه المنصة للاسترشاد فقط. يرجى مراجعة الطبيب.")

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



