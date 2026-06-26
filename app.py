import streamlit as st

st.title("نبراس: للتنبؤ بالأمراض")
st.write("الرجاء إدخال البيانات الحيوية للحصول على التنبؤ:")

# إنشاء خانات إدخال للمستخدم
age = st.number_input("العمر", min_value=0, max_value=120, value=30)
blood_pressure = st.number_input("ضغط الدم", min_value=50, max_value=200, value=120)

# زر التنبؤ
if st.button("توقع الحالة الصحية"):
    # خوارزمية تنبؤ بسيطة جداً للأغراض التجريبية
    if blood_pressure > 140 or (age > 50 and blood_pressure > 130):
        st.warning("النتيجة: قد يكون هناك خطر ارتفاع ضغط الدم، يرجى استشارة الطبيب.")
    else:
        st.success("النتيجة: المؤشرات ضمن النطاق الطبيعي.")

st.info("تنبيه: هذا التطبيق لأغراض تجريبية فقط.")

