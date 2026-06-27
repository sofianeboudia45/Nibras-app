import streamlit as st
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="نبراس", page_icon="🩺")
st.title("🩺 منصة نبراس الذكية")

# 1. إدخال البيانات
age = st.number_input("العمر", 0, 120, 30)
glucose = st.number_input("السكر", 50, 400, 100)
bp = st.number_input("ضغط الدم", 50, 200, 120)

# 2. زر التنبؤ والحفظ
if st.button("تنبؤ وحفظ البيانات"):
    if os.path.exists('patients.csv'):
        df = pd.read_csv('patients.csv')
        
        # التأكد من تنوع البيانات
        if df['Result'].nunique() < 2:
            st.warning("يرجى إدخال بيانات متنوعة (آمن وتحذير) لتدريب النموذج.")
            result = "تحت التدريب"
        else:
            # تدريب النموذج
            X = df[['Age', 'Glucose', 'BP']]
            y = df['Result']
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X, y)
            
            # التنبؤ للحالة الجديدة
            new_patient = pd.DataFrame([[age, glucose, bp]], columns=["Age", "Glucose", "BP"])
            result = model.predict(new_patient)[0]
            
            # حساب وعرض الدقة
            y_pred = model.predict(X)
            accuracy = accuracy_score(y, y_pred)
            st.info(f"📊 دقة النموذج الحالي: {accuracy * 100:.2f}%")
    else:
        result = "آمن" if (glucose < 125 and bp < 140) else "تحذير"
        st.write("ملاحظة: هذه أول حالة، سيتم بناء النموذج لاحقاً.")
    
    # حفظ البيانات
    new_data = pd.DataFrame([[age, glucose, bp, result]], columns=["Age", "Glucose", "BP", "Result"])
    if os.path.exists('patients.csv'):
        new_data.to_csv('patients.csv', mode='a', header=False, index=False)
    else:
        new_data.to_csv('patients.csv', index=False)
        
    st.success(f"النتيجة المتوقعة: **{result}**")
    st.success("تم حفظ البيانات بنجاح!")

# 3. عرض البيانات
if os.path.exists('patients.csv'):
    st.write("### سجل المرضى:")
    st.table(pd.read_csv('patients.csv'))
    
    
    
    



