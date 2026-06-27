import streamlit as st
from supabase import create_client

# --- إعدادات السحابة ---
# رابط مشروعك من Supabase
SUPABASE_URL = "https://olzkwdoavnymhohmggdv.supabase.co" 
# المفتاح السري (Service Role Key) الذي نسخته
SUPABASE_KEY = "Sb_secret_f5ix5yXXaMbi1-nIHQgpIg_i9BTFEzc" 

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- دالة الحساب ---
def calculate_egfr(creatinine, age, gender):
    return round(creatinine * 0.9, 2)

# --- واجهة المستخدم ---
st.title("🩺 منصة نبراس: عالمية")

with st.sidebar:
    name = st.text_input("اسم المريض")
    creat = st.number_input("الكرياتينين")
    age = st.number_input("العمر")
    gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
    
    if st.button("حفظ في السحابة 💾"):
        egfr = calculate_egfr(creat, age, gender)
        data = {
            "patient_name": name,
            "creatinine": creat,
            "age": age,
            "gender": gender,
            "egfr": egfr
        }
        try:
            supabase.table("patients_data").insert(data).execute()
            st.success("تم الحفظ عالمياً!")
        except Exception as e:
            st.error(f"خطأ في الاتصال: {e}")
            
    




            
    
    

    
        





        
    
        
    
    
    

    
    
    
    
    





    

    
    
    
    



