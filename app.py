# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس الصحية", page_icon="📈", layout="wide")

# دالة الحساب المحدثة (دقة أعلى)
def calculate_egfr_advanced(creatinine, age, gender, weight):
    # معادلة CKD-EPI 2021
    kappa = 0.7 if gender == "أنثى" else 0.9
    alpha = -0.241 if gender == "أنثى" else -0.302
    
    # حساب eGFR الأساسي
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age)
    if gender == "أنثى": eGFR *= 1.012
    
    # تعديل النتيجة بناءً على مساحة سطح الجسم (BSA) تقريباً
    # BSA (Mosteller) = sqrt((height * weight) / 3600)
    # للتبسيط نستخدم عامل الوزن المرجعي 1.73m2
    return round(eGFR, 2)

if 'history' not in st.session_state: st.session_state.history = []

st.title("🩺 منصة نبراس: التحليل السريري المتقدم")
with st.sidebar:
    st.header("البيانات السريرية")
    patient_name = st.text_input("اسم المريض")
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
    weight = st.number_input("الوزن (kg)", min_value=10.0, max_value=250.0)
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر", min_value=0, max_value=120)
    if st.button("تحليل دقيق"):
        if creatinine > 0 and age > 0:
            res = calculate_egfr_advanced(creatinine, age, gender, weight)
            st.session_state.history.append({"التاريخ": datetime.now().strftime("%Y-%m-%d %H:%M"), "eGFR": res})
        else:
            st.error("أدخل بيانات صحيحة")

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    col1, col2 = st.columns(2)
    with col1:
        st.table(df)
    with col2:
        fig = px.line(df, x="التاريخ", y="eGFR", markers=True, title="تطور مؤشر eGFR السريري")
        st.plotly_chart(fig)
else:
    st.info("أدخل البيانات من القائمة الجانبية لبدء التحليل السريري.")

st.caption("⚠️ ملاحظة: تم تحديث الخوارزمية لتوافق معايير CKD-EPI 2021.")

            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



