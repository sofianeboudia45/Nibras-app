import streamlit as st
import pandas as pd
import os

# إعداد الصفحة
st.set_page_config(page_title="نبراس - الجزائر", page_icon="🇩🇿")

st.title("🇩🇿 بوابة نبراس الصحية")
st.subheader("تحليل ذكي للحالة الصحية للمريض")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("اسم المريض")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    age = st.number_input("العمر (سنة)", min_value=0.0, format="%.1f")

with col2:
    creatinine = st.number_input("الكرياتينين (mg/dL)", min_value=0.0, format="%.2f")
    sugar = st.number_input("نسبة السكر (mg/dL)", min_value=0.0, format="%.1f")

# دالة التحليل الذكي (المنطق الطبي المبسط)
def analyze_health(creatinine, sugar):
    if creatinine > 1.3 or sugar > 200:
        return "⚠️ حالة حرجة: يرجى مراجعة الطبيب فوراً", "error"
    elif creatinine > 1.1 or sugar > 140:
        return "⚖️ حالة تحت المراقبة: بحاجة لضبط الحمية", "warning"
    else:
        return "✅ حالة جيدة: النتائج ضمن النطاق الطبيعي", "success"

# تنفيذ التحليل عند الضغط
if st.button("🔍 تحليل الحالة"):
    analysis_result, type = analyze_health(creatinine, sugar)
    
    if type == "error":
        st.error(analysis_result)
    elif type == "warning":
        st.warning(analysis_result)
    else:
        st.success(analysis_result)

    # زر إضافي لحفظ النتيجة
    if st.button("💾 حفظ النتيجة في السجل"):
        data = {
            "اسم المريض": [name],
            "الكرياتينين": [creatinine],
            "السكر": [sugar],
            "النتيجة": [analysis_result]
        }
        df = pd.DataFrame(data)
        file_path = 'patients_data.csv'
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8-sig')
        else:
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
        st.success("تم الحفظ بنجاح!")

st.markdown("---")
st.caption("نبراس - صنع في الجزائر بفخر 🇩🇿")
                           
    
    





    

    
    
    
    



