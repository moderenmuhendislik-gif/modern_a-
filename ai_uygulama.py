import streamlit as st
import json
import os
from gtts import gTTS
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Moderen AI", page_icon="🔊")
st.title("🔊 Moderen Mühendislik Sesli Asistan")

# --- SESLENDİRME FONKSİYONU ---
def seslendir(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("cevap.mp3")
    with open("cevap.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)

# --- HAFIZA İŞLEMLERİ ---
if 'hafiza' not in st.session_state:
    if os.path.exists("hafiza.json"):
        with open("hafiza.json", "r", encoding="utf-8") as f:
            st.session_state.hafiza = json.load(f)
    else:
        st.session_state.hafiza = {"merhaba": "Selam Eren Usta, Moderen Mühendislik emrinde!"}

# --- SEKMELİ ARAYÜZ (GİDEN ÖĞRETME KISMI BURADA) ---
tab1, tab2 = st.tabs(["💬 Asistanla Konuş", "🧠 Yeni Bilgi Öğret"])

with tab1:
    soru = st.text_input("Sorunu yaz:").lower()
    if st.button("Cevapla ve Seslendir"):
        if soru in st.session_state.hafiza:
            cevap = st.session_state.hafiza[soru]
            st.success(f"AI: {cevap}")
            seslendir(cevap)
        else:
            bilmiyorum = "Bunu henüz öğrenmedim Eren Usta. Diğer sekmeden bana öğretebilirsin."
            st.error(bilmiyorum)
            seslendir(bilmiyorum)

with tab2:
    st.subheader("Hafızayı Geliştir")
    y_soru = st.text_input("Soru (Örn: bodor lazer):").lower()
    y_cevap = st.text_area("Cevap:")
    if st.button("Bilgiyi Kaydet"):
        if y_soru and y_cevap:
            st.session_state.hafiza[y_soru] = y_cevap
            with open("hafiza.json", "w", encoding="utf-8") as f:
                json.dump(st.session_state.hafiza, f, ensure_ascii=False, indent=4)
            st.success("Bilgi hafızaya kazındı!")
            st.balloons()
