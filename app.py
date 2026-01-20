import streamlit as st
import hashlib
import time

st.title("🔐 SHA-256 Hash Cracker (Simulation)")

# 1. Target နံပါတ်ကို သတ်မှတ်ပြီး Hash ပြောင်းထားမယ်
target_number = "1000000"
target_hash = hashlib.sha256(target_number.encode()).hexdigest()

st.info(f"ရှာဖွေမည့် Target Hash: \n\n **{target_hash}**")

if st.button("Hash ကို စတင်ရှာဖွေပါ"):
    start_time = time.time()
    found = False
    attempt = 0
    
    # 0 ကနေ စတင်ပြီး တစ်ခုချင်းစီ Hash လုပ်ကာ တိုက်စစ်ခြင်း
    # စက်အမြန်နှုန်းအတွက် loop ပတ်ရုံပဲလုပ်ပါမယ် (st.write မပါဘဲ)
    while not found:
        # လက်ရှိ နံပါတ်ကို Hash ပြောင်းသည်
        current_hash = hashlib.sha256(str(attempt).encode()).hexdigest()
        
        # တူ၊ မတူ စစ်ဆေးသည်
        if current_hash == target_hash:
            found = True
        else:
            attempt += 1
            
    end_time = time.time()
    duration = end_time - start_time

    st.success(f"✅ ရှာတွေ့သွားပါပြီ!")
    st.write(f"တွေ့ရှိခဲ့သည့် ကိန်းဂဏန်း: **{attempt}**")
    st.metric("ကြာမြင့်ချိန်", f"{duration:.4f} စက္ကန့်")
    st.metric("စမ်းသပ်ခဲ့သည့် အကြိမ်အရေအတွက်", f"{attempt:,}")
