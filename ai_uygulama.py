import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64

st.set_page_config(page_title="Karacaardıç Hafızası", page_icon="🌳")

# --- ANAHTAR KONTROLÜ ---
if "GEMINI_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        anahtar_hazir = True
    except:
        anahtar_hazir = False
else:
    anahtar_hazir = False

def asistan_konussun(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("ses.mp3")
        with open("ses.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
            st.markdown(md, unsafe_allow_html=True)
    except: pass

st.title("🌳 Karacaardıç Köyü Dijital Sayfası")

if not anahtar_hazir:
    st.warning("⚠️ Eren Usta, anahtar (API Key) henüz Secrets kısmına takılmadı.")
else:
    st.success("✅ Karacaardıç'ın dijital beyni aktif!")

soru = st.text_input("Bir konu yazın (Örn: Köyün geçmişi):")

if st.button("Anlat ve Seslendir"):
    if soru and anahtar_hazir:
        komut = f"Karacaardıç köyü bilge asistanı olarak soru sormadan şu konuyu Eren Usta'ya anlat: {soru}"
        response = model.generate_content(komut)
        st.info(response.text)
        asistan_konussun(response.text)
    elif not anahtar_hazir:
        st.error("Beyin (model) aktif değil, anahtarı kontrol et usta!")
