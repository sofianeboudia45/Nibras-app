# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس: البطاقة الصحية", page_icon="🩺", layout="wide")

# دالة الحساب المتقدمة (CKD-EPI)
def calculate_egfr_advanced(creatinine, age, gender):
    kappa = 0.7 if gender == "أنثى" else 0.9
    alpha = -0.241 if gender == "أنثى" else -0.302
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age)
    if gender == "أنثى": eGFR *= 1.012
    return round(eGFR, 2)

# تهيئة حالة الجلسة
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🩺 منصة نبراس: البطاقة الصحية الرقمية")
st.markdown("---")

# القائمة الجانبية للمدخلات
with st.sidebar:
    st.header("إدخال البيانات السريرية")
    patient_name = st.text_input("اسم المريض")
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
    weight = st.number_input("الوزن (kg)", min_value=10.0, max_value=250.0, value=70.0)
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر", min_value=0, max_value=120)
    notes = st.text_input("ملاحظات المريض (اختياري)")
    
    if st.button("حفظ التحليل 💾"):
        if creatinine > 0 and age > 0:
            res = calculate_egfr_advanced(creatinine, age, gender)
            st.session_state.history.append({
                "الاسم": patient_name,
                "التاريخ": datetime.now().strftime("%m-%d %H:%M"), 
                "eGFR": res, 
                "الوزن": weight,
                "ملاحظات": notes
            })
            st.success("تم الحفظ بنجاح!")
        else:
            st.error("يرجى إدخال قيم صحيحة للكرياتينين والعمر.")

# عرض البيانات والرسوم البيانية
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    
    # عنوان ديناميكي يتفادى الخطأ السابق
    current_name = df['الاسم'].iloc[-1] if not df['الاسم'].empty else "غير معروف"
    st.subheader(f"سجل المتابعة للمريض: {current_name}")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.dataframe(df, use_container_width=True)
    with col2:
        st.subheader("تحليل بصري للتطور")
        fig = px.line(df, x="التاريخ", y="eGFR", markers=True)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("أدخل البيانات من القائمة الجانبية لبدء بطاقتك الصحية.")

st.caption("⚠️ ملاحظة: هذه المنصة للاستخدام العام، يجب مراجعة الطبيب للتشخيص الدقيق.")




            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



