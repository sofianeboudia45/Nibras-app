# -*- coding: utf-8 -*-
import streamlit as st
from datetime import datetime

# إعداد الصفحة
st.set_page_config(page_title="منصة نبراس الذكية", page_icon="🩺")

def calculate_egfr(creatinine, age, gender):
    kappa, alpha, gender_factor = (0.7, -0.241, 1.012) if gender == "أنثى" else (0.9, -0.302, 1.0)
    if creatinine <= 0: return 0
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# المحلل الذكي للأدوية
def analyze_medication_risk(egfr):
    if egfr >= 90:
        return "لا توجد قيود خاصة على الأدوية الشائعة."
    elif 60 <= egfr < 90:
        return "يجب الحذر عند تناول المسكنات (مثل الإيبوبروفين والنابروكسين) واستشارة الطبيب."
    elif 30 <= egfr < 60:
        return "تنبيه: يجب تعديل جرعات أدوية السكري (مثل الميتفورمين) وبعض المضادات الحيوية. لا تتناول أي دواء دون مراجعة الطبيب."
    else:
        return "خطر عالي: يمنع استخدام العديد من الأدوية (مثل بعض مسكنات NSAIDs وبعض مدرات البول) دون إشراف طبي دقيق."

if 'history' not in st.session_state: st.session_state.history = []

st.title("🩺 منصة نبراس الذكية")
st.subheader("تحليل وظائف الكلى والمخاطر الدوائية")
st.markdown("---")

patient_name = st.text_input("اسم المريض 👤")
creatinine = st.number_input("الكرياتينين (mg/dL) 🧪", min_value=0.0, format="%.2f")
gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
age = st.number_input("العمر 📅", min_value=0, max_value=120)

if st.button("تحليل الأدوية والمخاطر 🔍"):
    if creatinine > 0 and age > 0:
        result = calculate_egfr(creatinine, age, gender)
        advice = analyze_medication_risk(result)
        
        st.metric(label="معدل eGFR", value=f"{result} ml/min")
        st.warning(f"⚠️ التوجيه الدوائي: {advice}")
        
        st.session_state.history.append({"الوقت": datetime.now().strftime("%H:%M"), "النتيجة": result, "توجيه": advice})
    else:
        st.error("يرجى إدخال قيم صحيحة.")

# عرض السجل
if st.session_state.history:
    st.markdown("### 📊 السجل الطبي للجلسة")
    st.table(st.session_state.history)
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



