import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64

# API KEY'ini buraya yapıştır
API_KEY = "BURAYA_KENDI_API_KEYINI_YAPISTIR" 

st.set_page_config(page_title="Karacaardıç Hızlı Hafıza", page_icon="⚡")

def asistan_konussun(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("hizli.mp3")
        with open("hizli.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass

st.title("⚡ Karacaardıç Köyü Canlı Bilgi Hattı")

soru = st.text_input("Bir konu yaz (Örn: Köyün tarihi, Yaylalar, Turna avı):", placeholder="Lafı uzatmadan anlatayım Eren Usta...")

if st.button("Anlat Bakalım"):
    if soru:
        with st.spinner('Hemen anlatıyorum...'):
            try:
                genai.configure(api_key=API_KEY)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Talimat: Kısa, öz, teknik değil ama samimi, asla soru sorma.
                komut = f"Sen Karacaardıç köyünün bilge hafızasısın. Eren Usta'ya şu konu hakkında soru sormadan, doğrudan ve hızlı bilgi ver: {soru}"
                
                response = model.generate_content(komut)
                cevap = response.text
                
                # Yanıtı göster ve seslendir
                st.success(cevap)
                asistan_konussun(cevap)
                
            except Exception as e:
                st.error(f"Hata: {e}")
    else:
        st.warning("Eren Usta, önce bir konu başlığı girmen lazım.")
