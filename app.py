import streamlit as st
import pandas as pd

# إعداد الصفحة لتكون بوضع العرض الكامل
st.set_page_config(page_title="منصة نبراس الذكية", layout="wide")

# تخصيص العنوان بستايل جذاب
st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>🩺 منصة نبراس الذكية</h1>
    <hr>
""", unsafe_allow_html=True)

# استخدام القائمة الجانبية للمدخلات لتبدو الصفحة أنيقة
with st.sidebar:
    st.header("⚙️ بيانات الفحص")
    age = st.number_input("العمر", min_value=0, value=30)
    glucose = st.number_input("السكر", min_value=0, value=100)
    bp = st.number_input("ضغط الدم", min_value=0, value=120)
    bmi = st.number_input("مؤشر كتلة الجسم", min_value=0.0, value=22.0)
    
    predict_btn = st.button("تنبؤ وحفظ البيانات", type="primary")

# الحاوية الرئيسية لعرض النتائج
with st.container(border=True):
    st.subheader("📊 نتيجة التحليل")
    
    if predict_btn:
        # هنا تضع منطق التنبؤ الخاص بك (الـ RandomForest)
        # مثال بسيط للنتيجة:
        result = "آمن" if glucose < 150 else "تحذير"
        
        if result == "آمن":
            st.success("✅ النتيجة: المريض في حالة آمنة")
        else:
            st.error("⚠️ النتيجة: يرجى مراجعة الطبيب")
    else:
        st.info("قم بإدخال البيانات واضغط على زر التنبؤ للبدء.")

# عرض السجل بتنسيق احترافي
st.markdown("---")
st.subheader("📋 سجل المرضى المسجلين")
# يمكنك هنا جلب البيانات من Google Sheets وعرضها كالتالي:
# df = pd.DataFrame(...) 
# st.dataframe(df, use_container_width=True)

    
    
    
    



