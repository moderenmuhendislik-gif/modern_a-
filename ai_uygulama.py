import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64

# API KEY'ini buraya yapıştır
API_KEY = "BURAYA_API_KEY_GELECEK" 

st.set_page_config(page_title="Karacaardıç Hızlı Hafıza", page_icon="⚡")

def asistan_konussun(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("hizli.mp3")
    with open("hizli.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(md, unsafe_allow_html=True)

st.title("⚡ Karacaardıç Hızlı Bilgi Hattı")

soru = st.text_input("Konu nedir Eren Usta? (Geçmiş, doğa, anılar...)", placeholder="Kısa bir kelime yazman yeterli...")

if st.button("Anlat Bakalım"):
    if soru:
        try:
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # TALİMAT: Soru sorma, sadece anlat.
            ozel_komut = (
                f"Sen Karacaardıç köyünün hafızasısın. Eren Usta'ya kısa, öz ve net bilgiler ver. "
                f"Asla soru sorma, sadece anlatılan konuya odaklan ve hemen cevap ver. Konu: {soru}"
            )
            
            response = model.generate_content(ozel_komut)
            cevap = response.text
