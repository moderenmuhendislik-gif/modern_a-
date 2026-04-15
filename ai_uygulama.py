import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64

# API KEY'ini buraya yapıştır
API_KEY = "BURAYA_API_KEY_GELECEK" 

# Sayfa Yapılandırması ve Tasarımı
st.set_page_config(page_title="Karacaardıç Köyü Dijital Mirası", page_icon="🌳", layout="wide")

# CSS ile Görsel İyileştirme (Konya Bozkır Teması)
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    .header-text {
        color: #1b5e20;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BÖLÜM: KÖY TANITIMI ---
st.markdown("<h1 class='header-text'>🌳 Karacaardıç Köyü Dijital Mirası</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Bozkır'ın Bağrında Bir Kadim Hafıza</h4>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Köyümüz Hakkında")
    st.write("""
    Konya'nın Bozkır ilçesine bağlı olan Karacaardıç, tarihi ardıç ağaçları, sert ama mert insanları ve 
    zengin yayla kültürüyle bilinir. Bozkır Barajı'nın serinliği ve doğanın sessizliği ile huzurun adresidir.
    """)
    st.image("https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", caption="Karacaardıç Doğası (Temsili)")

with col2:
    st.subheader("Kültürel Miras")
    st.markdown("""
    * **Meşhur Ardıçlar:** Köye adını veren asırlık ağaçlar.
    * **Yaylacılık:** Yaz aylarında serin yayla göçleri.
    * **Av Kültürü:** Bozkır çevresindeki meşhur turna avları.
    * **Mühendislik Ruhu:** Moderen Mühendislik gibi vizyoner girişimler.
    """)

st.divider()

# --- ALT BÖLÜM: YAPAY ZEKA ASİSTANI ---
st.subheader("🎙️ Karacaardıç Bilge Hafızası (AI)")
st.info("Eren Usta, köyümüzün geçmişine veya doğasına dair merak ettiğin her şeyi aşağıya yaz, yapay zekan anlatsın.")

def asistan_konussun(metin):
    try:
        tts = gTTS(text=metin, lang='tr')
        tts.save("ses.mp3")
        with open("ses.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# Kullanıcı Girişi
soru = st.text_input("Bir konu başlığı girin:", placeholder="Örn: Yayla göçleri, Eski düğünler, Turna avı...")

if st.button("Hafızayı Canlandır ve Dinle"):
    if soru:
        try:
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            komut = f"Sen Karacaardıç köyünün bilge asistanısın. Eren Usta'ya şu konu hakkında soru sormadan, kısa ve öz bilgi ver: {soru}"
            
            response = model.generate_content(komut)
            cevap = response.text
            
            st.success(cevap)
            asistan_konussun(cevap)
        except Exception as e:
            st.error(f"Bağlantı hatası: {e}")
    else:
        st.warning("Eren Usta, anlatmam için bir konu yazmalısın.")

# Sayfa Alt Bilgisi
st.sidebar.title("Moderen Mühendislik")
st.sidebar.info("Bu proje Eren Usta tarafından Karacaardıç Köyü mirasını dijitalleştirmek için tasarlanmıştır.")
