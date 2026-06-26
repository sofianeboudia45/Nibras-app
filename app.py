import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="نبراس - المنصة الذكية", page_icon="🩺")

# العنوان الرئيسي مع أيقونة
st.title("🩺 منصة نبراس الذكية")
st.subheader("تحليل وتنبؤ صحي مدعوم بالبيانات")

# استخدام الأعمدة لترتيب المدخلات
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("السن (العمر)", min_value=0, max_value=120, value=30)

with col2:
    blood_pressure = st.number_input("ضغط الدم (mmHg)", min_value=50, max_value=200, value=120)

st.write("---") # خط فاصل

# زر التنبؤ بتصميم واضح
if st.button("🚀 ابدأ عملية التنبؤ"):
    with st.spinner("جاري تحليل البيانات..."):
        # منطق التنبؤ
        if blood_pressure > 140 or (age > 50 and blood_pressure > 130):
            st.warning("⚠️ تنبيه: تشير البيانات إلى احتمالية ارتفاع ضغط الدم. يرجى استشارة طبيب مختص.")
        else:
            st.success("✅ النتيجة: المؤشرات ضمن النطاق الطبيعي. حافظ على نمط حياتك الصحي!")

st.info("تنبيه: هذه المنصة لأغراض تجريبية وتدريبية فقط، ولا تغني عن التشخيص الطبي المهني.")


