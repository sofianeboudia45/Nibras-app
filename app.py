import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# إعداد قاعدة البيانات
def init_db():
    conn = sqlite3.connect('nibras_records.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (date TEXT, name TEXT, gender TEXT, age REAL, creatinine REAL, glucose REAL, egfr REAL)''')
    conn.commit()
    conn.close()

init_db()

# دالة الحساب
def calculate_egfr(creatinine, age, gender):
    k = 0.7 if gender == 'female' else 0.9
    alpha = -0.241 if (gender == 'female' and creatinine <= k) else (-1.200 if (gender == 'female' and creatinine > k) else (-0.302 if creatinine <= k else -1.200))
    a = 144 if gender == 'female' else 141
    return round(a * ((creatinine / k) ** alpha) * (0.9938 ** age), 2)

# الواجهة
st.title("نبراس - أداة التحليل السريري 🩺")

tab1, tab2 = st.tabs(["تحليل جديد", "سجل المرضى 📋"])

with tab1:
    patient_name = st.text_input("اسم المريض")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر (سنة)", min_value=0, value=50)
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, value=1.0, step=0.01)
    glucose = st.number_input("نسبة السكر (mg/dL)", min_value=0.0, value=90.0)
    
    if st.button("تحليل الحالة 🔬"):
        gender_en = 'male' if gender == "ذكر" else 'female'
        egfr = calculate_egfr(creatinine, age, gender_en)
        st.metric(label="eGFR", value=f"{egfr} mL/min/1.73m²")
        
        # حفظ النتيجة تلقائياً في السجل عند التحليل
        conn = sqlite3.connect('nibras_records.db')
        c = conn.cursor()
        c.execute("INSERT INTO patients VALUES (?,?,?,?,?,?,?)", 
                  (datetime.now().strftime("%Y-%m-%d"), patient_name, gender, age, creatinine, glucose, egfr))
        conn.commit()
        conn.close()
        st.success("تم إجراء التحليل وحفظ النتيجة في السجل!")

with tab2:
    st.subheader("سجل المرضى")
    if st.button("تحديث السجلات 🔄"):
        conn = sqlite3.connect('nibras_records.db')
        df = pd.read_sql_query("SELECT * FROM patients", conn)
        conn.close()
        st.dataframe(df)
        
