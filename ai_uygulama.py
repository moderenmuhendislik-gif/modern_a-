import streamlit as st
import json
import os
from gtts import gTTS
import base64
from streamlit_mic_recorder import speech_to_text

st.set_page_config(page_title="Moderen AI Otomatik", page_icon="🎙️")

# --- SESLENDİRME ---
def seslendir(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # Otomatik çalma kodu
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)

# --- HAFIZA ---
if 'hafiza' not in st.session_state:
    if os.path.exists("hafiza.json"):
        with open("hafiza.json", "r", encoding="utf-8") as f:
            st.session_state.hafiza = json.load(f)
    else:
        st.session_state.hafiza = {"merhaba": "Selam Eren Usta, seni dinliyorum!"}

st.title("🎙️ Moderen AI (Eller Serbest)")
st.write("Eren Usta, herhangi bir butona basmana gerek yok. Sadece konuş, sistem otomatik algılayacaktır.")

# --- OTOMATİK DİNLEME ---
# 'just_once=False' ve 'callback' mantığıyla buton derdini bitiriyoruz
text = speech_to_text(
    language='tr', 
    start_prompt="🎙️ Dinleme Aktif (Konuşabilirsiniz)", 
    stop_prompt="⏹️ İşleniyor...", 
    just_once=False, 
    key='otomatik_dinleme'
)

if text:
    soru = text.lower()
    st.info(f"Duyulan: {soru}")
    
    if soru in st.session_state.hafiza:
        cevap = st.session_state.hafiza[soru]
        st.success(f"AI: {cevap}")
        seslendir(cevap)
    elif "kaydet" in soru:
        seslendir("Kaydetmek istediğin bilgiyi söyle Eren Usta.")
    else:
        bilmiyorum = "Bunu henüz öğrenmedim Eren Usta."
        st.error(bilmiyorum)
        seslendir(bilmiyorum)
