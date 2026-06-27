# -*- coding: utf-8 -*-
import streamlit as st
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس الذكية", page_icon="🩺")

# دالة الحساب
def calculate_egfr(creatinine, age, gender):
    kappa, alpha, gender_factor = (0.7, -0.241, 1.012) if gender == "أنثى" else (0.9, -0.302, 1.0)
    if creatinine <= 0: return 0
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# محرك التوصيات الذكي (AI Logic)
def get_ai_recommendation(egfr):
    if egfr >= 90:
        return "وظائف الكلى ضمن النطاق الطبيعي. استمر في نمط الحياة الصحي. لا توجد توصيات دوائية خاصة."
    elif 60 <= egfr < 90:
        return "انخفاض طفيف: يُنصح بمراجعة الطبيب لمراجعة أي أدوية قد تؤثر على الكلى (مثل المسكنات NSAIDs)."
    elif 30 <= egfr < 60:
        return "انخفاض متوسط: يرجى استشارة الطبيب فوراً لتعديل جرعات الأدوية الحالية، فقد تحتاج لتقليل جرعات بعض الأدوية."
    else:
        return "حالة حرجة: يجب مراجعة الطبيب المختص فوراً. قد تتطلب حالتك تعديلاً جذرياً في الأدوية أو التوقف عن أدوية معينة تحت إشراف طبي."

# تهيئة ذاكرة الجلسة
if 'history' not in st.session_state: st.session_state.history = []

st.title("🩺 منصة نبراس الذكية")
st.subheader("تحليل وتقييم ذكي")
st.markdown("---")

patient_name = st.text_input("اسم المريض 👤")

col1, col2 = st.columns(2)
with col1:
    creatinine = st.number_input("الكرياتينين (mg/dL) 🧪", min_value=0.0, format="%.2f")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
with col2:
    age = st.number_input("العمر 📅", min_value=0, max_value=120)
    
if st.button("تحليل ذكي وتوصية 🔍"):
    if creatinine > 0 and age > 0:
        result = calculate_egfr(creatinine, age, gender)
        recommendation = get_ai_recommendation(result)
        
        # إضافة النتيجة للتاريخ مع التوصية
        entry = {"التوقيت": datetime.now().strftime("%H:%M"), "النتيجة": result, "توصية": recommendation}
        st.session_state.history.append(entry)
        
        st.metric(label="معدل الترشيح الكبيبي (eGFR)", value=f"{result} ml/min")
        st.info(f"💡 توصية ذكية: {recommendation}")
    else:
        st.error("يرجى إدخال قيم صحيحة.")

# عرض السجل والتقرير
if st.session_state.history:
    st.markdown("### 📊 سجل النتائج")
    st.table(st.session_state.history)
    
    report_text = f"تقرير نبراس الطبي - المريض: {patient_name}\n" + "-"*30 + "\n"
    for item in st.session_state.history:
        report_text += f"الوقت: {item['التوقيت']} | النتيجة: {item['النتيجة']} | التوصية: {item['توصية']}\n"
    
    st.download_button("📥 تحميل التقرير الشامل", report_text.encode('utf-8-sig'), "nibras_report.txt")
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



