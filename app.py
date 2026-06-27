import streamlit as st
import pandas as pd
import os

# إعداد الصفحة لتكون واسعة
st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")

# إضافة صورتك الشخصية بحجم كبير وعرض كامل
image_file = "my_photo.jpg.jpg"

if os.path.exists(image_file):
    # وضع الصورة في حاوية تأخذ عرض الصفحة بالكامل
    st.image(image_file, use_container_width=True)
else:
    st.warning("يرجى التأكد من اسم الملف.")

st.markdown("<h1 style='text-align: center;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ بيانات المريض")
    name = st.text_input("اسم المريض")
    age = st.number_input("العمر", value=30)
    glucose = st.number_input("مستوى السكر", value=100)
    predict_btn = st.button("تحليل وحفظ النتيجة")

if predict_btn and name:
    result = "⚠️ يحتاج استشارة" if glucose > 140 else "✅ طبيعي"
    new_data = pd.DataFrame({"الاسم": [name], "العمر": [age], "السكر": [glucose], "النتيجة": [result]})
    
    if os.path.exists("patients_data.csv"):
        new_data.to_csv("patients_data.csv", mode='a', header=False, index=False, encoding='utf-8-sig')
    else:
        new_data.to_csv("patients_data.csv", index=False, encoding='utf-8-sig')
        
    st.success(f"تم تحليل بيانات {name}!")

st.markdown("---")
st.subheader("📊 لوحة التحكم")
if os.path.exists("patients_data.csv"):
    df = pd.read_csv("patients_data.csv", encoding='utf-8-sig')
    st.dataframe(df, use_container_width=True)
    
    
    
    
    
    
    
    





    

    
    
    
    



