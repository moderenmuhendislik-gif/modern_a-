import streamlit as st
import json
import os
from gtts import gTTS
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Moderen AI - Sesli Asistan", page_icon="🔊")
st.title("🔊 Sesli Moderen Asistan")
st.write("Eren Usta, asistanın emirlerini bekliyor!")

# --- SES FONKSİYONU ---
def seslendir(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("cevap.mp3")
        with open("cevap.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # Otomatik oynatma için HTML kodu
            md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
            st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Ses çalma hatası: {e}")

# --- HAFIZA İŞLEMLERİ ---
HAF_DOSYASI = "hafiza.json"

def hafizayi_yukle():
    if os.path.exists(HAF_DOSYASI):
        with open(HAF_DOSYASI, "r", encoding="utf-8") as f:
            return json.load(f)
    # Eğer dosya yoksa ilk bilgileri oluştur
    return {"merhaba": "Selam Eren! Moderen Mühendislik asistanı yardıma hazır."}

def hafizaya_kaydet(yeni_hafiza):
    with open(HAF_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(yeni_hafiza, f, ensure_ascii=False, indent=4)

# Uygulama başladığında hafızayı yükle
if 'hafiza' not in st.session_state:
    st.session_state.hafiza = hafizayi_yukle()

# --- ARAYÜZ (SEKMELER) ---
tab1, tab2 = st.tabs(["🔊 Konuş ve Dinle", "✍️ Yeni Bilgi Öğret"])

with tab1:
    soru = st.text_input("Bana bir şey sor (Örn: Merhaba):").lower()
    if st.button("Cevap Ver"):
        if soru in st.session_state.hafiza:
            cevap = st.session_state.hafiza[soru]
            st.success(f"AI: {cevap}")
            seslendir(cevap) # Sesi duyurur
        else:
            bilmiyorum = "Bunu henüz öğrenmedim Eren. Yan taraftan bana öğretebilirsin."
            st.warning(bilmiyorum)
            seslendir(bilmiyorum)

with tab2:
    st.subheader("Bana Yeni Bir Şey Öğret")
    yeni_soru = st.text_input("Soru ne olsun?").lower()
    yeni_cevap = st.text_area("Cevabı ne olsun?")
    
    if st.button("Bilgiyi Kaydet"):
        if yeni_soru and yeni_cevap:
            st.session_state.hafiza[yeni_soru] = yeni_cevap
            hafizaya_kaydet(st.session_state.hafiza)
            st.success(f"Tamamdır Eren! '{yeni_soru}' dendiğinde ne diyeceğimi öğrendim.")
            st.balloons()