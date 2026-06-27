import streamlit as st

# 1. تعريف الدالة أولاً (ليتمكن البرنامج من التعرف عليها لاحقاً)
def calculate_egfr(creatinine, age, gender):
    if gender == "أنثى":
        kappa, alpha, gender_factor = 0.7, -0.241, 1.012
    else:
        kappa, alpha, gender_factor = 0.9, -0.302, 1.0
    
    # حماية من القسمة على صفر أو القيم غير المنطقية
    if creatinine <= 0: return 0
    
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    return round(eGFR, 2)

# 2. واجهة المستخدم (مطابقة لما في 2051.jpg)
creatinine = st.number_input("أدخل مستوى الكرياتينين")
age = st.number_input("أدخل العمر")
gender = st.selectbox("أدخل الجنس", ["ذكر", "أنثى"])

# 3. زر التحليل (يستدعي الدالة المعرفة أعلاه)
if st.button("تحليل"):
    if creatinine > 0 and age > 0:
        result = calculate_egfr(creatinine, age, gender)
        st.write(f"معدل الترشيح الكبيبي المقدر (eGFR): {result}")
        # إضافة تصنيف سريع
        if result >= 90: st.success("النتيجة: طبيعية")
        elif result >= 60: st.warning("النتيجة: انخفاض طفيف")
        else: st.error("النتيجة: تتطلب استشارة طبية")
    else:
        st.error("يرجى إدخال قيم صحيحة للكرياتينين والعمر")
        
    
    
    

    
    
    
    
    





    

    
    
    
    



