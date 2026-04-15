import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64
from PIL import Image
import io

# API KEY kısmını daha önce aldığın anahtarla doldurmayı unutma
# Görüntü oluşturma yeteneği olan bir model kullanacağız (Örn: gemini-1.5-flash veya pro)
API_KEY = "SENİN_API_KEYİN" 

st.set_page_config(page_title="Karacaardıç Köyü Görsel Hafızası", page_icon="🌳")

def asistan_konussun(metin):
    tts = gTTS(text=metin, lang='tr')
    tts.save("koy_hikayesi.mp3")
    with open("koy_hikayesi.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(md, unsafe_allow_html=True)

# Görüntü Oluşturma Fonksiyonu
def gorsel_olustur(istem):
    try:
        genai.configure(api_key=API_KEY)
        # Görüntü oluşturma modelini seçiyoruz
        gorsel_model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Görüntü istemini sanatsal bir dille güncelliyoruz
        gorsel_istem = f"Konya Bozkır Karacaardıç köyünün eski zamanlarını anlatan, nostaljik, yağlı boya tablo tarzında, detaylı ve duygusal bir sahne. Sahne şunları içermeli: {istem}"
        
        # Görüntüyü oluştur
        response = gorsel_model.generate_content(
            [gorsel_istem],
            generation_config={"mime_type": "image/jpeg"}
        )
        
        # Görüntüyü döndür
        gorsel_verisi = response.candidates[0].content.parts[0].inline_data.data
        return Image.open(io.BytesIO(gorsel_verisi))
    except Exception as e:
        st.error(f"Görsel oluşturma hatası: {e}")
        return None

st.title("🌳 Karacaardıç Köyü Görsel Hafızası")
st.write("Bozkır'ın bağrından, hem sesli hem görsel Karacaardıç hikayeleri...")

# Yapay Zekayı Eğitiyoruz (Köy Bilgileri - Görsel Odaklı)
koy_bilgisi = """
Sen Karacaardıç köyünün en yaşlı ve bilge kişisinin sesisin. 
Konya Bozkır'a bağlı Karacaardıç köyünü çok iyi biliyorsun. 
Eski yayla göçlerinden, köyün geleneklerinden, o meşhur ardıç ağaçlarından ve Bozkır barajı çevresindeki turna avlarından bahset. 
Soruları cevaplarken bir köylü samimiyetiyle ve 'Eren Usta'ya hitaben konuş.
Ayrıca, anlattığın hikayeye uygun, nostaljik ve sanatsal bir görsel tasvirini de (istemini) oluştur.
"""

soru = st.text_input("Köyümüzün geçmişine dair neyi görmek ve duymak istiyorsun Eren Usta?")

if st.button("Hikayeyi Göster ve Anlat"):
    if soru:
        with st.spinner('Karacaardıç'ın tozlu raflarından hikayeler ve görüntüler derleniyor...'):
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Bilgiyle soruyu birleştiriyoruz
            cevap = model.generate_content(f"{koy_bilgisi} \n\n Soru: {soru}")
            
            # Hikayeyi Anlat ve Seslendir
            st.info(cevap.text)
            asistan_konussun(cevap.text)
            
            # Görseli Oluştur ve Göster
            # Hikayeden görsel tasvirini çıkarıyoruz (Bu kısım modelin cevabına göre ayarlanabilir)
            gorsel_tasviri = cevap.text.split('\n')[0] # Örnek olarak ilk satırı alıyoruz
            gorsel = gorsel_olustur(gorsel_tasviri)
            if gorsel:
                st.image(gorsel, caption=f"Karacaardıç'tan bir kesit: {gorsel_tasviri}", use_column_width=True)
                
    else:
        st.warning("Henüz bir şey sormadın Eren Usta.")
