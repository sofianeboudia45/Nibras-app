import sqlite3
from datetime import datetime

# إنشاء قاعدة البيانات عند بدء التطبيق
def init_db():
    conn = sqlite3.connect('nibras_records.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (date TEXT, gender TEXT, age REAL, creatinine REAL, glucose REAL, egfr REAL)''')
    conn.commit()
    conn.close()

# دالة حفظ النتيجة
def save_record(gender, age, creatinine, glucose, egfr):
    conn = sqlite3.connect('nibras_records.db')
    c = conn.cursor()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
    c.execute("INSERT INTO patients VALUES (?,?,?,?,?,?)", 
              (date_now, gender, age, creatinine, glucose, egfr))
    conn.commit()
    conn.close()

# داخل دالة "تحليل الحالة" في الكود السابق، أضف زر حفظ:
if st.sidebar.button("حفظ النتيجة في السجل"):
    save_record(gender, age, creatinine, glucose, egfr_val)
    st.sidebar.success("تم حفظ السجل بنجاح!")
    
