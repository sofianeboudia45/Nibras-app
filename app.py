# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس: البطاقة الصحية", page_icon="🩺", layout="wide")

# دالة الحساب
def calculate_egfr_advanced(creatinine, age, gender, weight):
    kappa = 0.7 if gender == "أنثى" else 0.9
    alpha = -0.241 if gender == "أنثى" else -0.302
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age)
    if gender == "أنثى": eGFR *= 1.012
    return round(eGFR, 2)

if 'history' not in st.session_state: st.session_state.history = []

st.title("🩺 منصة نبراس: البطاقة الصحية الرقمية")
st.markdown("---")

with st.sidebar:
    st.header("إدخال البيانات السريرية")
    patient_name = st.text_input("اسم المريض") # خانة الاسم
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
    weight = st.number_input("الوزن (kg)", min_value=10.0, max_value=250.0, value=70.0)
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر", min_value=0, max_value=120)
    notes = st.text_input("ملاحظات المريض (اختياري)")
    
    if st.button("حفظ التحليل 💾"):
        if creatinine > 0 and age > 0:
            res = calculate_egfr_advanced(creatinine, age, gender, weight)
            st.session_state.history.append({
                "الاسم": patient_name,
                "التاريخ": datetime.now().strftime("%m-%d %H:%M"), 
                "eGFR": res, 
                "الوزن": weight,
                "ملاحظات": notes
            })
            st.success("تم الحفظ بنجاح!")
        else:
            st.error("يرجى إدخال قيم صحيحة")

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.subheader(f"سجل المتابعة للمريض: {df['الاسم'].iloc[-1]}")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.dataframe(df, use_container_width=True)
    with col2:
        st.subheader("تحليل بصري للتطور")
        fig = px.line(df, x="التاريخ", y="eGFR", markers=True)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("أدخل بيانات المريض في القائمة الجانبية للبدء.")

st.caption("⚠️ منصة نبراس: سجلاتك محفوظة لهذه الجلسة فقط.")



            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



