import streamlit as st

# 1. أولاً: تعريف الدالة
def calculate_egfr(creatinine, age, gender):
    # (هنا نضع الكود الذي كتبناه سابقاً للمعادلة)
    ...

# 2. ثانياً: جمع المدخلات من المستخدم
creatinine = st.number_input("أدخل مستوى الكرياتينين")
age = st.number_input("أدخل العمر")
gender = st.selectbox("أدخل الجنس", ["ذكر", "أنثى"])

# 3. ثالثاً: استدعاء الدالة بعد تعريفها وتجهيز المتغيرات
if st.button("تحليل"):
    result_value = calculate_egfr(creatinine, age, gender)
    st.write(f"النتيجة: {result_value}")
    
    
    

    
    
    
    
    





    

    
    
    
    



