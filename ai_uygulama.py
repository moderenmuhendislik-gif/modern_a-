import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64
import os
from streamlit_mic_recorder import speech_to_text

# --- GEMINI AYARI ---
# Buradaki 'API_ANAHTARIN' yazan yere kopyaladığın kodu yapıştır
os.environ["GEMINI_API_KEY"] = "boş"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Moderen AI Pro", page_icon="🚀")
st.title("🚀 Moderen Mühendislik (Gemini Gücüyle)")

# --- SESLENDİRME ---
def seslendir(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("cevap.mp3")
        with open("cevap.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# --- ANA AKIŞ ---
st.write("Eren Usta, mikrofonu aç ve sadece konuş. Gemini seni duyuyor:")

# Butonsuz mantığa en yakın: 'just_once=False'
konusulan = speech_to_text(language='tr', start_prompt="🎙️ Dinlemeyi Başlat", stop_prompt="⏹️ Cevapla", key='gemini_mic')

if konusulan:
    st.info(f"Sen: {konusulan}")
    
    # Gemini'ye talimat gönderiyoruz
    talimat = f"Sen Moderen Mühendislik'in asistanısın. Eren Usta ile konuşuyorsun. Kısa ve teknik cevaplar ver. Soru: {konusulan}"
    
    with st.spinner("Gemini düşünüyor..."):
        response = model.generate_content(talimat)
        cevap = response.text
        
    st.success(f"Moderen AI: {cevap}")
    seslendir(cevap)
