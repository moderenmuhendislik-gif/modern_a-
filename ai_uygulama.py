from gtts import gTTS
import os

# Senin yapay zekanın söyleyeceği söz
metin = "Selam Eren! Moderen Mühendislik için bugün hangi projeyi hayata geçiriyoruz? Lazer hazır, komutlarını bekliyorum."

# Ses dosyasını oluşturma (Türkçe dil desteğiyle)
tts = gTTS(text=metin, lang='tr')

# Ses dosyasını kaydetme
ses_dosyası = "yapay_zeka_ses.mp3"
tts.save(ses_dosyası)

# Dosyayı otomatik oynatma
os.system(f"start {ses_dosyası}") 

print("Yapay zekan şu an konuşuyor...")
