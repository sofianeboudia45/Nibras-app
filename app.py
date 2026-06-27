# أضف هذه الأسطر قبل زر التحليل في ملفك
has_diabetes = st.checkbox("هل تعاني من مرض السكري؟")
has_hypertension = st.checkbox("هل تعاني من ارتفاع ضغط الدم؟")
# عند الضغط على زر التحليل، ندمج النتائج
if st.button("تحليل"):
    eGFR = calculate_egfr(creatinine, age, gender) 
    # رسالة مخصصة بناءً على العوامل
    if has_diabetes or has_hypertension:
        st.write("ملاحظة: وجود السكري أو الضغط مع نتائج الكلى يتطلب متابعة دقيقة جداً.")
        # هنا يمكنك إضافة منطق لخفض درجة الأمان إذا كانت العوامل مجتمعة
    
    st.write(f"معدل eGFR الخاص بك هو: {eGFR}")
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



