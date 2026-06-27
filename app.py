import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
# إعداد الصفحة لتكون بوضع العرض الكامل
st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")

# تخصيص العنوان
st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>
    <hr>
""", unsafe_allow_html=True)

# القائمة الجانبية للمدخلات
with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    age = st.number_input("العمر", min_value=0, value=30)
    glucose = st.number_input("السكر", min_value=0, value=100)
    bp = st.number_input("ضغط الدم", min_value=0, value=120)
    bmi = st.number_input("مؤشر كتلة الجسم", min_value=0.0, value=22.0)
    
    predict_btn = st.button("تنبؤ وحفظ البيانات", type="primary")

# الحاوية الرئيسية لعرض النتائج
with st.container(border=True):
    st.subheader("📊 نتيجة التحليل")
    if predict_btn:
        # ضع هنا منطق التنبؤ الخاص بك
        result = "آمن" if glucose < 150 else "تحذير"
        if result == "آمن":
            st.success("✅ النتيجة: المريض في حالة آمنة")
        else:
            st.error("⚠️ النتيجة: يرجى مراجعة الطبيب")
    else:
        st.info("قم بإدخال البيانات واضغط على زر التنبؤ.")

# إضافة السجل (الجزء الذي طلبته)
st.markdown("---")
st.subheader("📋 سجل المرضى المسجلين")

try:
    # الاتصال بملف Google Sheets
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
    # عرض الجدول بشكل احترافي
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.warning("تعذر تحميل السجل حالياً. يرجى التأكد من ربط ملف Google Sheets بشكل صحيح.")
    

    
    
    
    



