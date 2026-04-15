import streamlit as st
from gtts import gTTS
import base64

# Sayfa Yapılandırması
st.set_page_config(page_title="Moderen Mühendislik Sesli Asistan", page_icon="🎙️")

def asistan_konussun(metin):
    # Metni sese çevir
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    
    # Sesi otomatik oynatmak için HTML/JavaScript hilesi
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

st.title("🎙️ Moderen Mühendislik Sesli Asistan")

# Örnek hazır butonlar (Hızlı komutlar)
if st.button("Beni Karşıla"):
    mesaj = "Selam Eren Usta! Moderen Mühendislik sistemine hoş geldin. Bugün tezgahın başında mıyız yoksa yeni tasarımlar mı yapıyoruz?"
    st.info(mesaj)
    asistan_konussun(mesaj)

if st.button("Lazer Durumunu Sor"):
    mesaj = "Bodor lazer kesim makinesi 6 kilowatt güçle hazır bekliyor. Parametreler senin komutuna göre optimize edilecek."
    st.info(mesaj)
    asistan_konussun(mesaj)

# Serbest metin girişi
kullanici_mesaji = st.text_input("Bana bir şey yaz, sana sesli cevap vereyim:")
if st.button("Cevapla ve Konuş"):
    if kullanici_mesaji:
        st.success(f"Seslendiriliyor: {kullanici_mesaji}")
        asistan_konussun(kullanici_mesaji)
