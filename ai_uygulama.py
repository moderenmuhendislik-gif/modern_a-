import streamlit as st
import json
import os

# Sayfa Ayarları
st.set_page_config(page_title="Moderen AI - Öğrenen Asistan", page_icon="🧠")
st.title("🧠 Öğrenen Moderen Asistan")

# --- HAFIZA İŞLEMLERİ ---
HAF_DOSYASI = "hafiza.json"

def hafizayi_yukle():
    if os.path.exists(HAF_DOSYASI):
        with open(HAF_DOSYASI, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"merhaba": "Selam Eren! Ben senin öğrettiklerini hatırlayan asistanınım."}

def hafizaya_kaydet(yeni_hafiza):
    with open(HAF_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(yeni_hafiza, f, ensure_ascii=False, indent=4)

# Hafızayı başlat
if 'hafiza' not in st.session_state:
    st.session_state.hafiza = hafizayi_yukle()

# --- ARAYÜZ ---
tab1, tab2 = st.tabs(["🤖 AI ile Konuş", "✍️ Yeni Bilgi Öğret"])

with tab1:
    soru = st.text_input("Bana bir şey sor:").lower()
    if st.button("Cevap Ver"):
        if soru in st.session_state.hafiza:
            st.success(f"AI: {st.session_state.hafiza[soru]}")
        else:
            st.warning("Bu bilgiyi henüz öğrenmedim. Yan taraftaki 'Yeni Bilgi Öğret' kısmından bana öğretebilirsin!")

with tab2:
    st.subheader("Bana Yeni Bir Şey Öğret")
    yeni_soru = st.text_input("Soru ne olsun? (Örn: elma nedir)").lower()
    yeni_cevap = st.text_area("Cevabı ne olsun?")
    
    if st.button("Bilgiyi Kaydet"):
        if yeni_soru and yeni_cevap:
            st.session_state.hafiza[yeni_soru] = yeni_cevap
            hafizaya_kaydet(st.session_state.hafiza)
            st.success(f"Tamamdır Eren! Artık '{yeni_soru}' dendiğinde ne diyeceğimi biliyorum.")
            st.balloons()
