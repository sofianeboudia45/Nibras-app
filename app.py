import streamlit as st
import pandas as pd
import os

DATA_FILE = "patients_data.csv"

st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)

# 1. المدخلات
with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    name = st.text_input("اسم المريض")
    age = st.number_input("العمر", value=30)
    glucose = st.number_input("مستوى السكر", value=100)
    predict_btn = st.button("تحليل وحفظ النتيجة")

def analyze_health(glucose):
    return "تتطلب استشارة" if glucose > 140 else "طبيعية"

if predict_btn and name:
    result = analyze_health(glucose)
    new_data = pd.DataFrame({"الاسم": [name], "العمر": [age], "السكر": [glucose], "النتيجة": [result]})
    if os.path.exists(DATA_FILE):
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        new_data.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')
    st.success("تم الحفظ!")

# 2. لوحة التحكم الإحصائية (الجديد)
st.markdown("---")
st.subheader("📊 لوحة التحكم الإحصائية")

if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
    
    # تقسيم الشاشة إلى عمودين
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("معدل السكر للمرضى:")
        st.bar_chart(df.set_index("الاسم")["السكر"])
    
    with col2:
        st.write("توزيع الأعمار:")
        st.line_chart(df.set_index("الاسم")["العمر"])
        
    st.subheader("📋 سجل المرضى المسجلين")
    st.table(df)
else:
    st.write("أدخل بياناتك لتظهر الإحصائيات.")
    
    



    

    
    
    
    



