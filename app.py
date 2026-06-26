import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="نبراس - المنصة الذكية", page_icon="🩺")

st.title("🩺 منصة نبراس الذكية")
st.subheader("تحليل البيانات الصحية الشامل")

# استخدام أعمدة لتنظيم الخانات
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("العمر", min_value=0, max_value=120, value=30)
    glucose = st.number_input("مستوى السكر في الدم (mg/dL)", min_value=50, max_value=400, value=100)

with col2:
    blood_pressure = st.number_input("ضغط الدم الانقباضي (mmHg)", min_value=50, max_value=200, value=120)
    bmi = st.number_input("مؤشر كتلة الجسم (BMI)", min_value=10.0, max_value=50.0, value=22.0)

# خانة اختيار إضافية
family_history = st.selectbox("هل يوجد تاريخ مرضي للعائلة؟", ["لا", "نعم"])

st.write("---")

if st.button("🚀 تحليل الحالة الصحية"):
    with st.spinner("جاري فحص المؤشرات..."):
        # منطق تنبؤ موسع
        risk_factors = 0
        if glucose > 125: risk_factors += 1
        if blood_pressure > 140: risk_factors += 1
        if bmi > 30: risk_factors += 1
        
        if risk_factors >= 2:
            st.error(f"⚠️ تنبيه: تم العثور على {risk_factors} مؤشرات تستدعي الانتباه. يرجى مراجعة طبيب مختص فوراً.")
        elif risk_factors == 1:
            st.warning("⚠️ تنبيه: هناك مؤشر واحد يتطلب المتابعة مع طبيب.")
        else:
            st.success("✅ النتيجة: جميع المؤشرات المدخلة ضمن النطاق الطبيعي.")

st.info("تنبيه: هذه النتائج تقديرية ولا تغني عن الفحوصات الطبية المعتمدة.")



