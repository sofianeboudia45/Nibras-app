import streamlit as st
import pandas as pd

st.set_page_config(page_title="نبراس - المنصة الذكية", page_icon="🩺")
st.title("🩺 منصة نبراس الذكية")

# إدخال البيانات
age = st.number_input("العمر", 0, 120, 30)
glucose = st.number_input("السكر", 50, 400, 100)
bp = st.number_input("ضغط الدم", 50, 200, 120)
bmi = st.number_input("مؤشر كتلة الجسم", 10.0, 50.0, 22.0)

# الاتصال بملف Google Sheets
conn = st.connection("gsheets", type="gsheets")

if st.button("🚀 حفظ البيانات إلى السحابة"):
    result = "آمن" if (glucose < 125 and bp < 140) else "تحذير"
    
    # تحضير البيانات الجديدة
    new_data = pd.DataFrame([{
        "Age": age,
        "Glucose": glucose,
        "BP": bp,
        "BMI": bmi,
        "Result": result
    }])
    
    # إضافة البيانات للملف
    conn.update(data=new_data)
    
    st.success("تم إرسال البيانات إلى Google Sheets بنجاح! ✅")
    



