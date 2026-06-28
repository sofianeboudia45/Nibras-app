import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# 1. إعداد قاعدة البيانات
def init_db():
    conn = sqlite3.connect('nibras_records.db')
    c = conn.cursor()
    # أنشأنا الجدول مسبقاً، لا داعي لـ DROP إلا إذا أردت تحديث الهيكل
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (date TEXT, name TEXT, gender TEXT, age REAL, creatinine REAL, glucose REAL, egfr REAL)''')
    conn.commit()
    conn.close()

init_db()

# 2. معادلة eGFR
def calculate_egfr(creatinine, age, gender):
    k = 0.7 if gender == 'female' else 0.9
    alpha = -0.241 if (gender == 'female' and creatinine <= k) else (-1.200 if (gender == 'female' and creatinine > k) else (-0.302 if creatinine <= k else -1.200))
    a = 144 if gender == 'female' else 141
    return round(a * ((creatinine / k) ** alpha) * (0.9938 ** age), 2)

# 3. دالة تصنيف الحالة
def get_egfr_interpretation(egfr):
    if egfr >= 90: return "طبيعي (وظائف الكلى سليمة) ✅", "success"
    elif 60 <= egfr < 90: return "انخفاض طفيف (مقبول) ⚠️", "info"
    elif 30 <= egfr < 60: return "انخفاض متوسط (يستوجب مراجعة الطبيب) 🩺", "warning"
    else: return "خطر / فشل كلوي 🏥", "error"

# 4. واجهة التطبيق
st.title("نبراس - أداة التحليل السريري 🩺")
st.subheader("الجزائر - الرعاية الصحية الرقمية 🇩🇿")

# استخدام التبويبات للتنظيم
tab1, tab2 = st.tabs(["تحليل جديد", "سجل المرضى 📋"])

with tab1:
    st.subheader("بيانات المريض")
    patient_name = st.text_input("اسم المريض")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر (سنة)", min_value=0, value=50)
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, value=1.0, step=0.01)
    glucose = st.number_input("نسبة السكر (mg/dL)", min_value=0.0, value=90.0)

    if st.button("تحليل الحالة 🔬"):
        gender_en = 'male' if gender == "ذكر" else 'female'
        egfr = calculate_egfr(creatinine, age, gender_en)
        st.session_state.last_data = (patient_name, gender, age, creatinine, glucose, egfr)
        st.metric(label="معدل الترشيح الكبيبي المقدر (eGFR)", value=f"{egfr} mL/min/1.73m²")
        
        interp, status = get_egfr_interpretation(egfr)
        if status == "success": st.success(interp)
        elif status == "info": st.info(interp)
        elif status == "warning": st.warning(interp)
        else: st.error(interp)

    if st.button("حفظ النتيجة في السجل 💾"):
        if 'last_data' in st.session_state and st.session_state.last_data[0]:
            conn = sqlite3.connect('nibras_records.db')
            c = conn.cursor()
            c.execute("INSERT INTO patients VALUES (?,?,?,?,?,?,?)", 
                      (datetime.now().strftime("%Y-%m-%d"), *st.session_state.last_data))
            conn.commit()
            conn.close()
            st.success("تم الحفظ!")
        else:
            st.error("يرجى إجراء التحليل وإدخال الاسم.")

with tab2:
    st.subheader("سجل المرضى المخزن")
    if st.button("تحديث السجلات 🔄"):
        conn = sqlite3.connect('nibras_records.db')
        df = pd.read_sql_query("SELECT * FROM patients", conn)
        conn.close()
        st.dataframe(df)
        
