import streamlit as st

st.title("BMI Calculator ⚖️")
st.write("သင့်ရဲ့ အရပ်နဲ့ ကိုယ်အလေးချိန်ကို ထည့်သွင်းပြီး BMI ကို တွက်ချက်ကြည့်ပါ။")

# Input ထည့်ရန် နေရာများ
weight = st.number_input("ကိုယ်အလေးချိန် (kg)", min_value=1.0, step=0.1)
height_cm = st.number_input("အရပ်အမြင့် (cm)", min_value=1.0, step=0.1)

if st.button("Calculate BMI"):
    if weight > 0 and height_cm > 0:
        # BMI Formula: weight (kg) / [height (m)]^2
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        
        st.subheader(f"သင့်ရဲ့ BMI ကတော့ {bmi:.2f} ဖြစ်ပါတယ်။")
        
        # ရလဒ်အဖြေကို ခွဲခြားပြခြင်း
        if bmi < 18.5:
            st.warning("ကိုယ်အလေးချိန် နည်းပါးနေသည် (Underweight)")
        elif 18.5 <= bmi < 25:
            st.success("ကိုယ်အလေးချိန် ပုံမှန်ရှိသည် (Healthy Weight)")
        elif 25 <= bmi < 30:
            st.info("ကိုယ်အလေးချိန် များနေသည် (Overweight)")
        else:
            st.error("အဝလွန်နေသည် (Obesity)")
    else:
        st.error("ကျေးဇူးပြု၍ မှန်ကန်သော တန်ဖိုးများ ထည့်သွင်းပါ။")
