# 1. عند الضغط على تحليل الحالة، قم بتخزين النتائج في session_state
if st.sidebar.button("تحليل الحالة"):
    gender_en = 'male' if gender == "ذكر" else 'female'
    egfr_val = calculate_egfr(creatinine, age, gender_en)
    
    # تخزين القيم في session_state للوصول إليها لاحقاً
    st.session_state['last_egfr'] = egfr_val
    st.session_state['last_gender'] = gender
    st.session_state['last_age'] = age
    st.session_state['last_creatinine'] = creatinine
    st.session_state['last_glucose'] = glucose
    # ... (عرض النتائج كما في الكود السابق)

# 2. عند الضغط على زر الحفظ، استرجع القيم من session_state
if st.sidebar.button("حفظ النتيجة في السجل"):
    if 'last_egfr' in st.session_state:
        save_record(
            st.session_state['last_gender'],
            st.session_state['last_age'],
            st.session_state['last_creatinine'],
            st.session_state['last_glucose'],
            st.session_state['last_egfr']
        )
        st.sidebar.success("تم الحفظ!")
    else:
        st.sidebar.error("يرجى إجراء التحليل أولاً قبل الحفظ.")
        
