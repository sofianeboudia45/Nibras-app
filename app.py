import streamlit as st
import pandas as pd

st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)

# 1. المدخلات
with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    age = st.number_input("العمر", value=30)
    glucose = st.number_input("السكر", value=100)
    predict_btn = st.button("تنبؤ")

# 2. عرض سجل المرضى (بيانات ثابتة للتجربة)
st.markdown("---")
st.subheader("📋 سجل المرضى المسجلين")

# إنشاء جدول تجريبي بسيط
data = {
    "الاسم": ["أحمد", "سارة", "محمد"],
    "العمر": [30, 25, 40],
    "السكر": [100, 110, 150]
}
df = pd.DataFrame(data)

# عرض الجدول
st.dataframe(df, use_container_width=True)


    

    
    
    
    



