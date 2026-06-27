import math

def calculate_egfr(creatinine, age, gender):
    """
    حساب معدل الترشيح الكبيبي المقدر (eGFR) باستخدام معادلة CKD-EPI 2021.
    
    :param creatinine: مستوى الكرياتينين (mg/dL)
    :param age: عمر المريض (بالسنوات)
    :param gender: 'male' للذكر أو 'female' للأنثى
    :return: قيمة eGFR
    """
    
    # الثوابت للمعادلة
    if gender.lower() == 'female':
        k = 0.7
        alpha = -0.241 if creatinine <= k else -1.200
        a = 144
    else:  # للذكر
        k = 0.9
        alpha = -0.302 if creatinine <= k else -1.200
        a = 141
        
    # المعادلة
    egfr = a * ((creatinine / k) ** alpha) * (0.9938 ** age)
    return round(egfr, 2)

# مثال على استخدام الدالة بناءً على بيانات المريض في 2106.jpg:
# الذكر، 88 سنة، الكرياتينين 0.98
result = calculate_egfr(creatinine=0.98, age=88, gender='male')
print(f"معدل eGFR المقدر: {result} مل/دقيقة/1.73م²")

                           
    
    





    

    
    
    
    



