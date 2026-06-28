import streamlit as st
import sqlite3
from datetime import datetime

# 1. إعداد قاعدة البيانات
def init_db():
    conn = sqlite3.connect('nibras_records.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (date TEXT, gender TEXT, age REAL, creatinine REAL, glucose REAL, egfr REAL)''')
    conn.commit()
    conn.close()

init_db()

# 2. معادلة eGFR
def calculate_egfr(creatinine, age, gender):
    k = 0.7 if gender == 'female' else 0.9
    alpha = -0.241 if (gender == 'female' and creatinine <= k) else (-1.200 if (gender == 'female' and creatinine > k) else (-0.302 if creatinine <= k else -1.200))
    a = 144 if gender == 'female' else 141
    return round(a * ((creatinine / k) ** alpha) * (0.9938 ** age), 2)

# 3. واجهة التطبيق
st.title("نبراس - أداة التحليل السريري")

if 'egfr_val' not in st.session_state:
    st.session_state.egfr_val = None

st.subheader("بيانات المريض")

gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
age = st.number_input("العمر (سنة)", min_value=0, max_value=120, value=50)
creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, value=1.0, step=0.01)
glucose = st.number_input("نسبة السكر (mg/dL)", min_value=0.0, value=90.0)

# زر التحليل
if st.button("تحليل الحالة"):
    gender_en = 'male' if gender == "ذكر" else 'female'
    st.session_state.egfr_val = calculate_egfr(creatinine, age, gender_en)
    st.session_state.last_data = (gender, age, creatinine, glucose, st.session_state.egfr_val)
    
    # عرض النتيجة بشكل واضح
    st.success("تم حساب التحليل بنجاح")
    st.metric(label="معدل الترشيح الكبيبي المقدر (eGFR)", value=f"{st.session_state.egfr_val} mL/min/1.73m²")

# زر الحفظ
if st.button("حفظ النتيجة في السجل"):
    if st.session_state.egfr_val is not None:
        conn = sqlite3.connect('nibras_records.db')
        c = conn.cursor()
        c.execute("INSERT INTO patients VALUES (?,?,?,?,?,?)", 
                  (datetime.now().strftime("%Y-%m-%d"), *st.session_state.last_data))
        conn.commit()
        conn.close()
        st.success("تم حفظ البيانات في السجل!")
    else:
        st.error("يرجى إجراء التحليل أولاً قبل الحفظ.")
    
