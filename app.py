import streamlit as st

# داخل كود الـ Streamlit بعد حساب الـ eGFR:
st.subheader("نتائج التحليل السريري")

col1, col2 = st.columns(2)

# عرض النتيجة الرئيسية بوضوح
col1.metric("معدل الترشيح (eGFR)", f"{result} ml/min", delta_color="normal")

# عرض الحالة الطبية بناءً على النتيجة
if result >= 90:
    st.success("المرحلة 1: وظائف كلى طبيعية أو مرتفعة")
elif 60 <= result < 90:
    st.warning("المرحلة 2: انخفاض طفيف في وظائف الكلى")
elif 30 <= result < 60:
    st.error("المرحلة 3: قصور كلوى متوسط")
# ... وهكذا
وهكذا
