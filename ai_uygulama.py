import streamlit as st
import json
import os
from gtts import gTTS
import base64
import time

# --- SESİ OTOMATİK ÇALAN FONKSİYON ---
def otomatik_seslendir(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # Bu HTML kodu, sesi yüklediği an oynatması için tarayıcıya emir verir
        ses_kodu = f"""
            <audio autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(ses_kodu, unsafe_allow_html=True)

# --- HAFIZA VE ARAYÜZ ---
if 'hafiza' not in st.session_state:
    if os.path.exists("hafiza.json"):
        with open("hafiza.json", "r", encoding="utf-8") as f:
            st.session_state.hafiza = json.load(f)
    else:
        st.session_state.hafiza = {"merhaba": "Selam Eren Usta!"}

st.title("🔊 Otomatik Konuşan Moderen AI")

soru = st.text_input("Sorunu yaz ve Enter'a bas:").lower()

if soru: # Enter'a bastığın an çalışır
    if soru in st.session_state.hafiza:
        cevap = st.session_state.hafiza[soru]
        st.success(f"AI: {cevap}")
        otomatik_seslendir(cevap) # Burada butona basmana gerek kalmadan ses çalmalı
    else:
        st.warning("Bunu bilmiyorum Eren.")