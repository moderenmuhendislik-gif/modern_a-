import streamlit as st
import json
import os
from gtts import gTTS
import base64
from streamlit_mic_recorder import speech_to_text

st.set_page_config(page_title="Moderen AI Sesli", page_icon="🎙️")
st.title("🎙️ Moderen Mühendislik Sesli Asistan")

# --- SESLENDİRME FONKSİYONU ---
def seslendir(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # Otomatik çalması için HTML kodu
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)

# --- HAFIZA ---
if 'hafiza' not in st.session_state:
    if os.path.exists("hafiza.json"):
        with open("hafiza.json", "r", encoding="utf-8") as f:
            st.session_state.hafiza = json.load(f)
    else:
        st.session_state.hafiza = {"merhaba": "Selam Eren Usta, Moderen Mühendislik emrinde!"}

# --- SESLİ KOMUT SİSTEMİ ---
st.write("🎙️ Konuşmak için butona bas, bitince durdur:")
# Burası sesi doğrudan yazıya (text) çevirir
text = speech_to_text(language='tr', start_prompt="🎙️ Dinlemeyi Başlat", stop_prompt="⏹️ Bitirdim/Cevapla", key='speech_input')

if text:
    soru = text.lower()
    st.info(f"Söylediğin: {soru}")
    
    # Hafızada cevap ara
    if soru in st.session_state.hafiza:
        cevap = st.session_state.hafiza[soru]
        st.success(f"AI: {cevap}")
        seslendir(cevap)
    elif "kaydet" in soru:
        # Kaydet komutu gelirse son konuşulanı hatırlar
        seslendir("Tamam Eren Usta, neyi kaydedeyim?")
    else:
        bilmiyorum = "Bunu henüz öğrenmedim Eren Usta."
        st.error(bilmiyorum)
        seslendir(bilmiyorum)
