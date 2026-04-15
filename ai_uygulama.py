import streamlit as st
from gtts import gTTS
import os

# Sayfa Ayarları
st.set_page_config(page_title="Moderen Mühendislik AI", page_icon="⚙️")

st.title("⚙️ Moderen Mühendislik Yapay Zeka")
st.write("Eren Usta, sisteme hoş geldin. Bugün hangi projeyi kesiyoruz?")

# Kullanıcıdan giriş al
input_text = st.text_input("Yapay zekaya bir mesaj yaz:", "Selam Eren! Lazer hazır, komutlarını bekliyorum.")

if st.button('Yapay Zekayı Konuştur'):
    if input_text:
        # Ses dosyasını oluşturma
        tts = gTTS(text=input_text, lang='tr')
        ses_dosyasi = "yapay_zeka_ses.mp3"
        tts.save(ses_dosyasi)
        
        # Sesi tarayıcıda çalma
        audio_file = open(ses_dosyasi, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        
        st.success(f"Ses oluşturuldu: {input_text}")
    else:
        st.warning("Lütfen bir metin girin.")

# Alt Bilgi
st.sidebar.markdown("---")
st.sidebar.write("👤 Mühendis: Eren Usta")
st.sidebar.write("📍 Konum: Konya / Karacaardıç")
