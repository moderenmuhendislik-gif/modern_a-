import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64

# --- YAPILANDIRMA ---
# Buraya Google AI Studio'dan aldığın API anahtarını yapıştır
API_KEY = "BURAYA_API_KEY_GELECEK" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Moderen Mühendislik AI", page_icon="⚙️")

def asistan_konussun(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
        st.markdown(md, unsafe_allow_html=True)

# --- ARAYÜZ ---
st.title("⚙️ Moderen Mühendislik Canlı Asistan")
st.write("Eren Usta, sorunu sor, yapay zekan cevaplasın ve konuşsun.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Soru Girişi
soru = st.text_input("Bana bir şey sor (Örn: Lazer kesimde dross nasıl önlenir?):")

if st.button("Soruyu Sor ve Dinle"):
    if soru:
        # Yapay zekaya kimlik kazandırıyoruz (Prompt Engineering)
        ozel_kom
