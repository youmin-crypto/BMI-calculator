import streamlit as st
import time

st.title("🔢 Number Counter (0 to 1M)")

# Start Button
if st.button("ရေတွက်မှုကို စတင်ပါ"):
    start_time = time.time()  # စတင်ချိန်ကို မှတ်သားသည်
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # ရေတွက်ခြင်း Process
    # မှတ်ချက် - ၁ သန်းအထိ တစ်ခုချင်းစီ screen ပေါ်တင်ပြရင် browser လေးသွားနိုင်လို့ 
    # အဆင့်လိုက်ပြပေးပါမယ်
    count = 0
    limit = 100000000
    
    for i in range(0, limit + 1, 100000): # ၁ သောင်းစီ ခုန်ပြီး progress ပြပါမယ်
        count = i
        percent_complete = i / limit
        progress_bar.progress(percent_complete)
        status_text.text(f"လက်ရှိအရေအတွက်: {i:,}")
    
    end_time = time.time()  # ပြီးဆုံးချိန်ကို မှတ်သားသည်
    duration = end_time - start_time # ကြာချိန်ကို တွက်သည်
    st.success(f"✅ ရေတွက်လို့ ပြီးပါပြီ!")
    st.balloons() # အောင်မြင်မှု အထိမ်းအမှတ် မိုးပျံပူဖောင်းလေးများ
    
    # ရလဒ်များကို ပြသခြင်း
    col1, col2 = st.columns(2)
    col1.metric("စုစုပေါင်းအရေအတွက်", f"{limit:,}")
    col2.metric("ကြာမြင့်ချိန် (စက္ကန့်)", f"{duration:.4f} s")
