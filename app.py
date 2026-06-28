import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# إعداد قاعدة البيانات (هيكلية محسنة)
def init_db():
    conn = sqlite3.connect('nibras_records.db')
    c = conn.cursor()
    # أضفنا معرف فريد (ID) لتسهيل إدارة السجلات
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  date TEXT, name TEXT, gender TEXT, age REAL, 
                  creatinine REAL, glucose REAL, egfr REAL)''')
    conn.commit()
    conn.close()

init_db()

# دالة الحساب
def calculate_egfr(creatinine, age, gender):
    k = 0.7 if gender == 'female' else 0.9
    alpha = -0.241 if (gender == 'female' and creatinine <= k) else (-1.200 if (gender == 'female' and creatinine > k) else (-0.302 if creatinine <= k else -1.200))
    a = 144 if gender == 'female' else 141
    return round(a * ((creatinine / k) ** alpha) * (0.9938 ** age), 2)

# واجهة التطبيق
st.set_page_config(page_title="Nibras Pro", layout="wide")
st.title("نبراس - المنصة الطبية الرقمية 🩺")

tab1, tab2 = st.tabs(["📊 التحليل السريري", "📋 سجل المرضى والأرشيف"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("اسم المريض")
        gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
        age = st.number_input("العمر (سنة)", min_value=0, value=50)
    with col2:
        creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, value=1.0, step=0.01)
        glucose = st.number_input("نسبة السكر (mg/dL)", min_value=0.0, value=90.0)
    
    if st.button("حفظ التحليل 💾"):
        gender_en = 'male' if gender == "ذكر" else 'female'
        egfr = calculate_egfr(creatinine, age, gender_en)
        
        conn = sqlite3.connect('nibras_records.db')
        c = conn.cursor()
        c.execute("INSERT INTO patients (date, name, gender, age, creatinine, glucose, egfr) VALUES (?,?,?,?,?,?,?)", 
                  (datetime.now().strftime("%Y-%m-%d %H:%M"), patient_name, gender, age, creatinine, glucose, egfr))
        conn.commit()
        conn.close()
        st.metric(label="النتيجة (eGFR)", value=f"{egfr} mL/min/1.73m²")
        st.success("تم حفظ البيانات في الأرشيف بنجاح!")

with tab2:
    st.subheader("أرشيف المرضى")
    conn = sqlite3.connect('nibras_records.db')
    df = pd.read_sql_query("SELECT * FROM patients", conn)
    conn.close()
    
    st.dataframe(df, use_container_width=True)
    
    # ميزة تصدير البيانات (قيمة تجارية مضافة)
    if not df.empty:
        csv = df.to_csv(index=False).encode('utf-8-sig') # ترميز utf-8-sig لدعم العربية في Excel
        st.download_button("📥 تصدير السجلات إلى Excel", csv, "Nibras_Records.csv", "text/csv")
