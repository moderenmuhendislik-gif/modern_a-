import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64

# --- GİZLİ ANAHTAR SİSTEMİ ---
# Anahtarı koda yazmıyoruz, Streamlit'in kendi hafızasından (secrets) alıyoruz.
try:
    API_KEY = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Anahtar henüz sisteme tanıtılmadı! (Secrets ayarını yapın)")

st.set_page_config(page_title="Karacaardıç Hafızası", page_icon="🌳")

def asistan_konussun(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("ses.mp3")
        with open("ses.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass

st.title("🌳 Karacaardıç Köyü Dijital Sayfası")
st.info("Eren Usta, bu sistem artık senin özel anahtarınla çalışıyor.")

soru = st.text_input("Bir konu yazın:")

if st.button("Anlat ve Seslendir"):
    if soru:
        # Karacaardıç bilgisiyle harmanlanmış özel komut
        komut = f"Sen Karacaardıç köyünün bilge asistanısın. Eren Usta'ya şu konuda kısa bilgi ver: {soru}"
        response = model.generate_content(komut)
        st.success(response.text)
        asistan_konussun(response.text)
