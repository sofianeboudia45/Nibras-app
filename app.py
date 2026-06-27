import math
def calculate_egfr(creatinine, age, gender):
    # تحويل الكرياتينين لـ mg/dL إذا كان بوحدة أخرى (هذه المعادلة تفترض mg/dL)
    # المعادلة المعتمدة CKD-EPI 2021
    if gender == "أنثى":
        kappa = 0.7
        alpha = -0.241
        gender_factor = 1.012
    else: # ذكر
        kappa = 0.9
        alpha = -0.302
        gender_factor = 1.0

    # المعادلة الرياضية
    eGFR = 142 * (min(creatinine/kappa, 1)**alpha) * (max(creatinine/kappa, 1)**-1.200) * (0.9938**age) * gender_factor
    
    return round(eGFR, 2)
    

    
    
    
    
    





    

    
    
    
    



