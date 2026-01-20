import streamlit as st
import hashlib
import time

st.title("⛏️ Crypto Mining Simulator")
st.write("Bitcoin Mining လုပ်တဲ့ သဘောတရားကို စမ်းသပ်ကြည့်ပါ။")

# Difficulty Level သတ်မှတ်ခြင်း (သုည ဘယ်နှစ်လုံး ပါရမလဲ)
difficulty = st.slider("Difficulty (ရှေ့ကပါရမယ့် သုညအရေအတွက်)", min_value=1, max_value=5, value=3)

if st.button("Mining စတင်ပါ"):
    prefix = '0' * difficulty
    found = False
    nonce = 0
    start_time = time.time()
    
    st.info(f"Target: ရှေ့မှာ **'{prefix}'** နဲ့ စတဲ့ Hash ကို ရှာနေပါပြီ...")
    
    # Mining Loop
    while not found:
        # Nonce (နံပါတ်တစ်ခု) ကို စာသားနဲ့တွဲပြီး Hash လုပ်သည်
        text = f"block_data_123_{nonce}"
        current_hash = hashlib.sha256(text.encode()).hexdigest()
        
        # သတ်မှတ်ထားတဲ့ သုည အရေအတွက်နဲ့ စသလား စစ်ဆေးသည်
        if current_hash.startswith(prefix):
            found = True
        else:
            nonce += 1
            
    end_time = time.time()
    duration = end_time - start_time

    st.success(f"🎊 Block ကို Mine လုပ်နိုင်ခဲ့ပါပြီ!")
    st.code(f"Hash: {current_hash}")
    st.write(f"ရှာဖွေခဲ့ရသော အကြိမ်ရေ (Nonce): **{nonce:,}**")
    st.metric("ကြာမြင့်ချိန်", f"{duration:.4f} စက္ကန့်")
