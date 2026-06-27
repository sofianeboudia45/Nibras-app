import streamlit as st
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="نبراس", page_icon="🩺")
st.title("🩺 منصة نبراس الذكية")

# إدخال البيانات
age = st.number_input("العمر", 0, 120, 30)
glucose = st.number_input("السكر", 50, 400, 100)
bp = st.number_input("ضغط الدم", 50, 200, 120)

# زر التنبؤ والحفظ
if st.button("تنبؤ وحفظ البيانات"):
    
    # 1. تدريب النموذج بناءً على السجلات السابقة
    if os.path.exists('patients.csv'):
        df = pd.read_csv('patients.csv')
        
        # التأكد من وجود بيانات كافية (على الأقل فئتين مختلفتين للنتيجة)
        if df['Result'].nunique() < 2:
            st.warning("يرجى إدخال بيانات متنوعة (آمن وتحذير) لتدريب النموذج بشكل أفضل.")
            result = "تحت التدريب"
        else:
            X = df[['Age', 'Glucose', 'BP']]
            y = df['Result']
            
            # بناء النموذج
            model = RandomForestClassifier(n_estimators=100)
            model.fit(X, y)
            
            # التنبؤ للحالة الجديدة
            new_patient = pd.DataFrame([[age, glucose, bp]], columns=["Age", "Glucose", "BP"])
            result = model.predict(new_patient)[0]
    else:
        # إذا كان أول استخدام ولا يوجد ملف، نستخدم المنطق البسيط مؤقتاً
        result = "آمن" if (glucose < 125 and bp < 140) else "تحذير"
    
    # 2. حفظ البيانات الجديدة
    new_data = pd.DataFrame([[age, glucose, bp, result]], 
                            columns=["Age", "Glucose", "BP", "Result"])
    
    if os.path.exists('patients.csv'):
        new_data.to_csv('patients.csv', mode='a', header=False, index=False)
    else:
        new_data.to_csv('patients.csv', index=False)
        
    st.success(f"النتيجة المتوقعة: {result}")
    st.success("تم حفظ البيانات بنجاح!")

# عرض البيانات
if os.path.exists('patients.csv'):
    st.write("### سجل المرضى:")
    st.table(pd.read_csv('patients.csv'))
    
    
    



