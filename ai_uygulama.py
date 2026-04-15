import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64

# API KEY kısmını daha önce aldığın anahtarla doldurmayı unutma
API_KEY = "SENİN_API_KEYİN" 

st.set_page_config(page_title="Karacaardıç Köyü Hafızası", page_icon="🌳")

def asistan_konussun(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("koy_hikayesi.mp3")
    with open("koy_hikayesi.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(md, unsafe_allow_html=True)

st.title("🌳 Karacaardıç Köyü Dijital Hafızası")
st.write("Bozkır'ın bağrından, geçmişten günümüze Karacaardıç hikayeleri...")

# Yapay Zekayı Eğitiyoruz (Köy Bilgileri)
koy_bilgisi = """
Sen Karacaardıç köyünün en yaşlı ve bilge kişisinin sesisin. 
Konya Bozkır'a bağlı Karacaardıç köyünü çok iyi biliyorsun. 
Eski yayla göçlerinden, köyün geleneklerinden, o meşhur ardıç ağaçlarından ve Bozkır barajı çevresindeki turna avlarından bahset. 
Soruları cevaplarken bir köylü samimiyetiyle ve 'Eren Usta'ya hitaben konuş.
"""

soru = st.text_input("Köyümüzün geçmişine dair ne merak ediyorsun Eren Usta?")

if st.button("Hikayeyi Anlat"):
    if soru:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Bilgiyle soruyu birleştiriyoruz
        cevap = model.generate_content(f"{koy_bilgisi} \n\n Soru: {soru}")
        
        st.info(cevap.text)
        asistan_konussun(cevap.text)
        
