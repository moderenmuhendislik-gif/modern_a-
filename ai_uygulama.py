import streamlit as st
import json
import os
from gtts import gTTS
import base64
from streamlit_mic_recorder import mic_recorder

st.set_page_config(page_title="Moderen AI Telsiz", page_icon="🎙️")
st.title("🎙️ Moderen Mühendislik Telsiz")

# --- SESLENDİRME ---
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
        st.session_state.hafiza = {"merhaba": "Selam Eren Usta, Moderen Mühendislik emrinde!"}

# --- SÜREKLİ DİNLEME VE CEVAP ---
st.write("Eren Usta, mikrofonu aç ve konuşmaya başla:")

# Bu bileşen sesi alır ve hemen işler
audio = mic_recorder(
    start_prompt="🎙️ Telsizi Aç",
    stop_prompt="⏹️ Dinlemeyi Durdur",
    key='recorder'
)

if audio:
    # Not: Burada sesi yazıya çevirmek için Google API kullanılır
    # 'audio' içindeki veri işlenir
    st.audio(audio['bytes']) # Kendi sesini duymak istersen
    
    # Burası senin "kaydet" dediğin veya soru sorduğun yer
    # (Bu kısım için 'requirements.txt' içine 'SpeechRecognition' eklemelisin)
    st.success("Seni duydum Eren Usta! İşliyorum...")
    
    # Simülasyon: Seninle konuşması için
    seslendir("Seni duydum Eren Usta, kaydet dersen hemen deftere yazarım.")
