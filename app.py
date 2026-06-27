import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)

# المدخلات
with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    age = st.number_input("العمر", value=30)
    glucose = st.number_input("السكر", value=100)
    bp = st.number_input("ضغط الدم", value=120)
    bmi = st.number_input("مؤشر كتلة الجسم", value=22.0)
    predict_btn = st.button("تنبؤ")

# عرض بسيط للنتائج
st.subheader("📊 نتيجة التحليل")
if predict_btn:
    st.success("تم استقبال البيانات بنجاح")

st.write("التطبيق يعمل الآن!")

    

    
    
    
    



