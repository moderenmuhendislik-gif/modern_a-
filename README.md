import streamlit as st
import os

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Moderen Mühendislik", page_icon="⚙️", layout="wide")

# --- STİL (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .baslik {
        color: #1e3d59;
        text-align: center;
        font-family: 'Arial Black';
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BİLGİ (HEADER) ---
st.markdown("<h1 class='baslik'>⚙️ MODEREN MÜHENDİSLİK</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Endüstriyel Tasarım | Lazer Kesim | Mekanik Çözümler</p>", unsafe_allow_html=True)
st.divider()

# --- ANA İÇERİK (2 KOLON) ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🛠️ Hizmetlerimiz")
    st.write("- **SolidWorks Tasarım:** 3D modelleme ve teknik çizim.")
    st.write("- **Lazer Kesim:** Bodor 6kW ile hassas malzeme işleme.")
    st.write("- **Mekanik İmalat:** Özel makine parçaları üretimi.")
    
    st.image("https://via.placeholder.com/400x200.png?text=Lazer+Kesim+Gorseli", caption="Moderen Mühendislik Atölyesi")

with col2:
    st.header("🤖 Moderen AI Asistan")
    st.info("Eren Usta'nın dijital çırağına buradan seslenebilirsin.")
    
    # Buraya senin az önce yaptığımız sesli sistemi ekliyoruz
    import streamlit_mic_recorder as smr
    text = smr.speech_to_text(language='tr', start_prompt="🎙️ Asistanı Uyandır", key='web_mic')
    
    if text:
        st.success(f"Duyulan Komut: {text}")
        # Buraya Gemini bağlayacağız (Önceki kodu buraya ekleyebilirsin)

# --- ALT BİLGİ (FOOTER) ---
st.divider()
st.markdown("<p style='text-align: center;'>© 2026 Moderen Mühendislik - Konya / Türkiye</p>", unsafe_allow_html=True)
