# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس الصحية", page_icon="📈", layout="wide")

# دالة الحساب
def calculate_egfr(creatinine, age, gender):
    kappa, alpha, gender_factor = (0.7, -0.241, 1.012) if gender == "أنثى" else (0.9, -0.302, 1.0)
    if creatinine <= 0: return 0
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# تهيئة الذاكرة
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🩺 منصة نبراس الصحية المتطورة")
st.markdown("---")

# واجهة المدخلات
with st.sidebar:
    st.header("بيانات المريض")
    patient_name = st.text_input("اسم المريض")
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر", min_value=0, max_value=120)
    if st.button("إضافة وتحليل"):
        if creatinine > 0 and age > 0:
            res = calculate_egfr(creatinine, age, gender)
            st.session_state.history.append({"التاريخ": datetime.now().strftime("%Y-%m-%d %H:%M"), "eGFR": res})
        else:
            st.error("أدخل بيانات صحيحة")

# عرض النتائج والرسوم البيانية
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("سجل النتائج")
        st.table(df)
        if st.button("مسح السجل"):
            st.session_state.history = []
            st.rerun()
            
    with col2:
        st.subheader("رسم بياني لتطور الحالة")
        fig = px.line(df, x="التاريخ", y="eGFR", markers=True, title="تغير معدل eGFR عبر الزمن")
        st.plotly_chart(fig)
        
    # التقرير
    report = df.to_string()
    st.download_button("📥 تحميل التقرير الشامل", report.encode('utf-8-sig'), "nibras_report.txt")

else:
    st.info("أدخل البيانات من القائمة الجانبية لبدء المتابعة.")

st.markdown("---")
st.caption("⚠️ تنبيه: هذه المنصة للاستخدام العام، يجب مراجعة الطبيب للحصول على تشخيص دقيق.")
            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



