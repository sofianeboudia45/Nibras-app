import streamlit as st

# 1. دالة حساب eGFR (معدل الترشيح الكبيبي)
def calculate_egfr(creatinine, age, gender):
    if gender.lower() == 'female':
        k = 0.7
        alpha = -0.241 if creatinine <= k else -1.200
        a = 144
    else:
        k = 0.9
        alpha = -0.302 if creatinine <= k else -1.200
        a = 141
    egfr = a * ((creatinine / k) ** alpha) * (0.9938 ** age)
    return round(egfr, 2)

# 2. تصميم الواجهة
st.title("نبراس - أداة التحليل السريري")

# استخدام الشريط الجانبي للمدخلات لتبقى الصفحة الرئيسية للنتائج
st.sidebar.header("بيانات المريض")
gender = st.sidebar.selectbox("الجنس", ["ذكر", "أنثى"])
age = st.sidebar.number_input("العمر (سنة)", min_value=1, max_value=120, value=50)
creatinine = st.sidebar.number_input("الكرياتينين (mg/dL)", min_value=0.1, max_value=20.0, value=1.0, step=0.01)
glucose = st.sidebar.number_input("نسبة السكر (mg/dL)", min_value=30, max_value=600, value=90)

if st.sidebar.button("تحليل الحالة"):
    # تحويل الجنس إلى الصيغة الإنجليزية للدالة
    gender_en = 'male' if gender == "ذكر" else 'female'
    
    # حساب النتيجة
    egfr_val = calculate_egfr(creatinine, age, gender_en)
    
    # 3. عرض النتائج بطريقة احترافية
    st.subheader("نتائج التحليل السريري")
    col1, col2 = st.columns(2)
    
    col1.metric("معدل الترشيح (eGFR)", f"{egfr_val} ml/min")
    col2.metric("مستوى السكر", f"{glucose} mg/dL")
    
    # تقييم الحالة
    st.write("---")
    if egfr_val >= 90:
        st.success(f"الحالة: طبيعية (المرحلة 1) - eGFR: {egfr_val}")
    elif 60 <= egfr_val < 90:
        st.warning(f"الحالة: انخفاض طفيف (المرحلة 2) - eGFR: {egfr_val}")
    elif 30 <= egfr_val < 60:
        st.error(f"الحالة: قصور كلوى متوسط (المرحلة 3) - eGFR: {egfr_val}")
    else:
        st.error(f"الحالة: قصور كلوى شديد (المرحلة 4 أو 5) - eGFR: {egfr_val}")
        
    st.info("ملاحظة: تم الحساب بناءً على معادلة CKD-EPI 2021 المعتمدة طبياً.")
    
