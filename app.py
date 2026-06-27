 import streamlit as st

def calculate_kidney_risk(age, glucose, creatinine, gender):
    # هذه معادلة افتراضية تبسيطية لأغراض التدريب
    # في التطبيق النهائي سنستخدم معادلة CKD-EPI المعتمدة
    risk_score = 0
    
    if glucose > 126: # مستوى السكر الصائم الذي قد يشير لسكري
        risk_score += 2
    if creatinine > 1.2: # مثال لقيمة كرياتينين مرتفعة للرجال
        risk_score += 3
    if age > 60:
        risk_score += 1
        
    if risk_score >= 4:
        return "خطر مرتفع - يرجى مراجعة طبيب كلى"
    elif risk_score >= 2:
        return "خطر متوسط - يفضل إجراء فحوصات إضافية"
    else:
        return "خطر منخفض - يرجى المتابعة الدورية"

# واجهة المستخدم في Streamlit
st.title("منصة نبراس الذكية")
age = st.number_input("العمر", min_value=0, max_value=120)
glucose = st.number_input("نسبة السكر في الدم")
creatinine = st.number_input("مستوى الكرياتينين")
gender = st.selectbox("الجنس", ["ذكر", "أنثى"])

if st.button("تحليل الحالة"):
    result = calculate_kidney_risk(age, glucose, creatinine, gender)
    st.write(f"النتيجة: {result}")

    
    
    
    
    





    

    
    
    
    



