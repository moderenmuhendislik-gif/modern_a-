import streamlit as st
import json
import os
from gtts import gTTS
import base64
from streamlit_mic_recorder import speech_to_text

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Moderen AI", page_icon="🎙️")
st.title("🎙️ Moderen Mühendislik Sesli Komut")

# --- SESLENDİRME FONKSİYONU ---
def seslendir(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)

# --- HAFIZA ---
if 'hafiza' not in st.session_state:
    if os.path.exists("hafiza.json"):
        with open("hafiza.json", "r", encoding="utf-8") as f:
            st.session_state.hafiza = json.load(f)
    else:
        st.session_state.hafiza = {"merhaba": "Selam Eren Usta!"}

# --- SESLİ KOMUT BUTONU ---
st.write("Aşağıdaki mikrofona bas ve konuş Eren Usta:")
text = speech_to_text(language='tr', start_prompt="🎙️ Konuşmak için bas", stop_prompt="⏹️ Durdur", key='speech')

if text:
    st.info(f"Söylediğin: {text}")
    soru = text.lower()
    
    if soru in st.session_state.hafiza:
        cevap = st.session_state.hafiza[soru]
        st.success(f"AI: {cevap}")
        seslendir(cevap)
    else:
        st.warning("Bunu henüz bilmiyorum.")
        seslendir("Bunu henüz bilmiyorum Eren Usta.")
