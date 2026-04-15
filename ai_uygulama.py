import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64
import os

# --- 1. AYARLAR ---
# BURAYA DİKKAT: Alttaki tırnak içine kendi API Key'ini yapıştırmalısın.
# Key almak için: https://aistudio.google.com/app/apikey
API_KEY = "SENİN_BURAYA_API_KEY_YAPIŞTIRMAN_LAZIM" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API Key eksik veya hatalı! Lütfen geçerli bir anahtar girin.")

st.set_page_config(page_title="Moderen Mühendislik AI", page_icon="⚙️")

# --- 2. SES FONKSİYONU ---
def asistan_konussun(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("cevap.mp3")
        with open("cevap.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Ses oluşturma hatası: {e}")

# --- 3. ARAYÜZ ---
st.title("⚙️ Moderen Mühendislik Canlı Asistan")
st.write(f"Eren Usta, sorunu sor, yapay zekan cevaplasın ve konuşsun.")

# Kullanıcı Girişi
soru = st.text_input("Bana bir şey sor (Örn: Lazerde dross nasıl önlenir?):", "")

if st.button("Soruyu Sor ve Dinle"):
    if soru:
        with st.spinner('Yapay zeka düşünüyor ve konuşmaya hazırlanıyor...'):
            # Prompt: Yapay zekaya kimlik veriyoruz
            ozel_komut = f"Sen Eren Usta'nın asistanısın. Eren, Konya'da Moderen Mühendislik'in sahibi uzman bir mühendistir. Soruya kısa, teknik ve samimi bir cevap ver. Soru: {soru}"
            
            try:
                # Cevap Üretme
                response = model.generate_content(ozel_komut)
                cevap_metni = response.text
                
                # Ekrana Yazma
                st.info(f"Asistanın Diyor Ki: {cevap_metni}")
                
                # SESLİ KONUŞMA
                asistan_konussun(cevap_metni)
                
            except Exception as e:
                st.error("Bir hata oluştu. Muhtemelen API Key girmedin veya geçersiz.")
    else:
        st.warning("Lütfen önce bir soru yaz Eren Usta.")
        
