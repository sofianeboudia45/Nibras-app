result_value = calculate_egfr(creatinine, age, gender)
if result_value >= 90:
    st.success(f"نتيجة وظائف الكلى: {result_value} (طبيعية)")
elif 60 <= result_value < 90:
    st.warning(f"نتيجة وظائف الكلى: {result_value} (انخفاض طفيف - يرجى استشارة الطبيب)")
elif 30 <= result_value < 60:
    st.error(f"نتيجة وظائف الكلى: {result_value} (انخفاض متوسط - ضرورة مراجعة طبيب كلى)")
else:
    st.error(f"نتيجة وظائف الكلى: {result_value} (حالة حرجة - يرجى مراجعة الطوارئ أو طبيب مختص فوراً)")
    
    

    
    
    
    
    





    

    
    
    
    



