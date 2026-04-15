import streamlit as st
import json
import os
from gtts import gTTS
import base64
from streamlit_mic_recorder import speech_to_text

st.set_page_config(page_title="Moderen AI Mobil", page_icon="📱")
st.title("📱 Moderen AI Sesli Kayıt")

# SESLENDİRME
def seslendir(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)

# HAFIZA YÜKLEME
if 'hafiza' not in st.session_state:
    if os.path.exists("hafiza.json"):
        with open("hafiza.json", "r", encoding="utf-8") as f:
            st.session_state.hafiza = json.load(f)
    else:
        st.session_state.hafiza = {}

if 'gecici' not in st.session_state:
    st.session_state.gecici = ""

# SESLİ KOMUT ALANI
st.write("Eren Usta, söyleyeceklerini dinliyorum:")
konusulan = speech_to_text(language='tr', start_prompt="🎙️ Beni Dinle", stop_prompt="✅ Tamam", key='mobil_mic')

if konusulan:
    metin = konusulan.lower()
    st.info(f"Duyulan: {metin}")

    if "kaydet" in metin:
        if st.session_state.gecici != "":
            # İlk kelimeyi başlık yapar
            baslik = st.session_state.gecici.split()[0]
            st.session_state.hafiza[baslik] = st.session_state.gecici
            with open("hafiza.json", "w", encoding="utf-8") as f:
                json.dump(st.session_state.hafiza, f, ensure_ascii=False, indent=4)
            st.success("Bilgi kalıcı olarak kaydedildi!")
            seslendir("Kaydettim Eren Usta.")
            st.session_state.gecici = ""
        else:
            seslendir("Aklımda kaydedilecek bir şey yok.")
    else:
        # 'Kaydet' demediysen her şeyi aklında tutar
        st.session_state.gecici = metin
        st.warning("Bu bilgiyi aklımda tutuyorum, 'kaydet' dersen yazacağım.")
        seslendir("Anladım, kaydet dersen deftere yazacağım.")
