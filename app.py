import streamlit as st
import pandas as pd

st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")

# العنوان بتنسيق أنيق
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>", unsafe_allow_html=True)
st.write("---")

# 1. المدخلات (Sidebar)
with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    age = st.number_input("العمر", min_value=0, max_value=120, value=30)
    glucose = st.number_input("مستوى السكر في الدم", min_value=50, max_value=400, value=100)
    bmi = st.number_input("مؤشر كتلة الجسم (BMI)", min_value=10.0, max_value=50.0, value=22.0)
    predict_btn = st.button("تحليل الحالة الصحية")

# 2. منطق الذكاء الاصطناعي (نموذج بسيط)
def analyze_health(age, glucose, bmi):
    # منطق طبي مبسط جداً للتجربة فقط
    if glucose > 140 or bmi > 30:
        return "حالة تتطلب استشارة طبية (مستوى السكر أو الكتلة مرتفع)", "red"
    else:
        return "الحالة ضمن النطاق الطبيعي (حافظ على نمط حياتك)", "green"

# 3. عرض النتائج
if predict_btn:
    result, color = analyze_health(age, glucose, bmi)
    st.markdown(f"---")
    st.subheader("📊 نتيجة التحليل")
    st.markdown(f"<h3 style='color: {color};'>{result}</h3>", unsafe_allow_html=True)
    
    # إضافة نصيحة بناءً على النتيجة
    if color == "red":
        st.warning("ننصح بزيارة الطبيب لإجراء فحص دوري دقيق.")
    else:
        st.success("نتائجك جيدة، استمر في اتباع نظامك الصحي.")

# 4. سجل المرضى (البيانات الثابتة كما اتفقنا)
st.markdown("---")
st.subheader("📋 سجل المرضى المسجلين")
data = {
    "الاسم": ["أحمد", "سارة", "محمد"],
    "العمر": [30, 25, 40],
    "النتيجة": ["طبيعية", "طبيعية", "تتطلب استشارة"]
}
st.table(pd.DataFrame(data))



    

    
    
    
    



