import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import webbrowser
import datetime
import subprocess
import re
import sys
import time
import tempfile
import random
import string

class ModernSesliAsistan:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mikrofonlu_dinleyici = sr.Microphone()
        self.temp_dir = tempfile.gettempdir()
        
        # Pygame mixer'ı başlat
        pygame.mixer.init()
        
        # Arka plan gürültüsünü ayarla
        with self.mikrofonlu_dinleyici as source:
            print("🎤 Arka plan gürültüsü ayarlanıyor...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
        # Komut tanımlama
        self.komutlar = {
            'aç': self.uygulama_ac,
            'başlat': self.uygulama_ac,
            'çalıştır': self.uygulama_ac,
            'kapat': self.uygulama_kapat,
            'google': self.google_ara,
            'youtube': self.youtube_ara,
            'saat': self.saat_soyler,
            'tarih': self.tarih_soyler,
            'not': self.not_al,
            'yardım': self.yardim_goster,
            'çıkış': self.cikis,
            'kapat': self.cikis
        }
        
        # Karşılama mesajları
        self.karsilama_mesajlari = [
            "Merhaba! Size nasıl yardımcı olabilirim?",
            "Hoş geldiniz! Ne yapmak istersiniz?",
            "Buyurun, sizi dinliyorum!",
            "Emrinizdeyim, ne yapabilirim?",
            "Size yardımcı olmak için buradayım!"
        ]
        
        # Test sesi çal
        self.test_ses()
        
    def test_ses(self):
        """Ses sistemini test eder"""
        try:
            test_metin = "Ses sistemi test ediliyor"
            print("\n🔊 Ses testi yapılıyor...")
            
            # Test ses dosyası oluştur
            test_file = os.path.join(self.temp_dir, 'test_ses.mp3')
            tts = gTTS(text=test_metin, lang='tr', slow=False)
            tts.save(test_file)
            
            # Ses dosyasını çal
            pygame.mixer.music.load(test_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            # Dosyayı temizle
            pygame.mixer.music.unload()
            os.remove(test_file)
            print("✅ Ses testi başarılı!")
        except Exception as e:
            print(f"❌ Ses testi başarısız: {e}")
            print("⚠️ Ses sistemi çalışmıyor olabilir. Lütfen şunları kontrol edin:")
            print("  1. Bilgisayarınızın sesi açık mı?")
            print("  2. Varsayılan ses çıkış cihazı doğru ayarlanmış mı?")
            print("  3. Başka bir uygulama sesi kullanıyor olabilir mi?")
    
    def konusma(self, metin):
        """Metni daha doğal bir Türkçe ses ile seslendirir."""
        try:
            # Benzersiz bir dosya adı oluştur
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            temp_file = os.path.join(self.temp_dir, f'asistan_ses_{random_string}.mp3')
            
            # Metni sese çevir
            tts = gTTS(text=metin, lang='tr', slow=False)
            tts.save(temp_file)
            
            print(f"🤖 Asistan: {metin}")
            
            # Ses dosyasını çal
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            # Temizlik
            pygame.mixer.music.unload()
            os.remove(temp_file)
        except Exception as e:
            print(f"❌ Ses oluşturma hatası: {e}")
            print(f"🤖 Asistan: {metin}")
            print("⚠️ Ses çalınamadı, lütfen ses ayarlarınızı kontrol edin.")
    
    def dinle(self):
        """Mikrofonu dinler ve sesi yazıya çevirir."""
        with self.mikrofonlu_dinleyici as source:
            print("\n👂 Dinleniyor...")
            ses = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            komut = ""
            
            try:
                komut = self.recognizer.recognize_google(ses, language="tr-TR")
                print(f"🎯 Siz: {komut}")
            except sr.UnknownValueError:
                self.konusma("Sizi anlayamadım, lütfen tekrar eder misiniz?")
            except sr.RequestError:
                self.konusma("Üzgünüm, ses tanıma servisi şu anda çalışmıyor.")
            except Exception as e:
                print(f"❌ Hata: {e}")
                self.konusma("Bir hata oluştu, tekrar deneyebilir misiniz?")
                
            return komut.lower()
    
    def komut_islet(self, komut_metni):
        """Alınan komutu işler ve uygun fonksiyonu çağırır."""
        if not komut_metni:
            return
            
        for anahtar_kelime, fonksiyon in self.komutlar.items():
            if anahtar_kelime in komut_metni:
                return fonksiyon(komut_metni)
        
        self.konusma("Bu komutu anlayamadım. Size nasıl yardımcı olabileceğimi görmek için 'yardım' diyebilirsiniz.")
    
    def uygulama_ac(self, komut):
        """Bilgisayardaki uygulamaları açar."""
        uygulama_isimleri = {
            "not defteri": "notepad",
            "hesap makinesi": "calc",
            "hesap makinası": "calc",
            "paint": "mspaint",
            "çizim": "mspaint",
            "tarayıcı": "msedge",
            "internet": "msedge",
            "edge": "msedge",
            "chrome": "chrome",
            "word": "winword",
            "excel": "excel",
            "powerpoint": "powerpnt",
            "komut satırı": "cmd",
            "cmd": "cmd",
            "terminal": "cmd",
            "dosya gezgini": "explorer",
            "klasör": "explorer",
        }
        
        try:
            for uygulama_ismi, uygulama_komutu in uygulama_isimleri.items():
                if uygulama_ismi in komut:
                    self.konusma(f"{uygulama_ismi} açılıyor")
                    subprocess.Popen(uygulama_komutu)
                    return
            
            self.konusma("Maalesef bu uygulamayı açamıyorum veya desteklemiyorum.")
        except Exception as e:
            self.konusma(f"Uygulama açılırken bir sorun oluştu: {e}")
    
    def uygulama_kapat(self, komut):
        """Çalışan uygulamaları kapatır."""
        uygulama_isimleri = {
            "not defteri": "notepad.exe",
            "hesap makinesi": "Calculator.exe",
            "hesap makinası": "Calculator.exe",
            "paint": "mspaint.exe",
            "tarayıcı": "msedge.exe",
            "edge": "msedge.exe",
            "chrome": "chrome.exe",
            "word": "WINWORD.EXE",
            "excel": "EXCEL.EXE",
            "powerpoint": "POWERPNT.EXE",
            "komut satırı": "cmd.exe",
            "cmd": "cmd.exe",
        }
        
        try:
            for uygulama_ismi, uygulama_sureci in uygulama_isimleri.items():
                if uygulama_ismi in komut:
                    self.konusma(f"{uygulama_ismi} kapatılıyor")
                    os.system(f"taskkill /f /im {uygulama_sureci}")
                    return
                    
            self.konusma("Maalesef bu uygulamayı kapatamıyorum veya desteklemiyorum.")
        except Exception as e:
            self.konusma(f"Uygulama kapatılırken bir sorun oluştu: {e}")
    
    def google_ara(self, komut):
        """Google'da arama yapar."""
        arama_sorgusu = komut.replace('google', '').strip()
        if not arama_sorgusu:
            self.konusma("Ne aramak istediğinizi söyler misiniz?")
            return
            
        self.konusma(f"Google'da {arama_sorgusu} için arama yapıyorum")
        webbrowser.open(f"https://www.google.com/search?q={arama_sorgusu}")
    
    def youtube_ara(self, komut):
        """YouTube'da arama yapar."""
        arama_sorgusu = komut.replace('youtube', '').strip()
        if not arama_sorgusu:
            self.konusma("YouTube'da ne aramak istediğinizi söyler misiniz?")
            return
            
        self.konusma(f"YouTube'da {arama_sorgusu} için arama yapıyorum")
        webbrowser.open(f"https://www.youtube.com/results?search_query={arama_sorgusu}")
    
    def saat_soyler(self, komut):
        """Mevcut saati söyler."""
        saat = datetime.datetime.now().strftime("%H:%M")
        self.konusma(f"Şu anda saat {saat}")
    
    def tarih_soyler(self, komut):
        """Bugünün tarihini söyler."""
        tarih = datetime.datetime.now().strftime("%d %B %Y")
        self.konusma(f"Bugün {tarih}")
    
    def not_al(self, komut):
        """Not defterine not alır."""
        not_metni = komut.replace('not', '').strip()
        if not not_metni:
            self.konusma("Not içeriğini söyler misiniz?")
            return
            
        try:
            with open("notlar.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"{datetime.datetime.now().strftime('%d.%m.%Y %H:%M')} - {not_metni}\n")
            self.konusma("Notunuzu başarıyla kaydettim.")
        except Exception as e:
            self.konusma(f"Not kaydedilirken bir sorun oluştu: {e}")
    
    def yardim_goster(self, komut):
        """Kullanılabilir komutları listeler."""
        yardim_metni = """
        🎯 Kullanabileceğiniz komutlar:
        
        📱 Uygulama Kontrolü:
        - 'Aç' veya 'Başlat' veya 'Çalıştır' + uygulama adı
          Örnek: "not defteri aç", "hesap makinesi çalıştır"
        - 'Kapat' + uygulama adı
          Örnek: "not defteri kapat"
        
        🔍 Arama:
        - 'Google' + arama sorgusu
          Örnek: "google hava durumu"
        - 'YouTube' + arama sorgusu
          Örnek: "youtube en son haberler"
        
        ⏰ Zaman:
        - 'Saat' - mevcut saati söyler
        - 'Tarih' - bugünün tarihini söyler
        
        📝 Not:
        - 'Not' + not metni
          Örnek: "not toplantı yarın saat 15:00'te"
        
        ℹ️ Diğer:
        - 'Yardım' - bu menüyü gösterir
        - 'Çıkış' veya 'Kapat' - programı sonlandırır
        """
        print(yardim_metni)
        self.konusma("Size yardımcı olabilecek tüm komutları gösterdim. Başka bir konuda yardıma ihtiyacınız var mı?")
    
    def cikis(self, komut):
        """Programdan çıkış yapar."""
        self.konusma("Görüşmek üzere! İyi günler dilerim!")
        sys.exit()
    
    def baslat(self):
        """Asistanı başlatır."""
        # Rastgele bir karşılama mesajı seç
        karsilama = random.choice(self.karsilama_mesajlari)
        self.konusma(karsilama)
        
        while True:
            try:
                komut = self.dinle()
                self.komut_islet(komut)
            except KeyboardInterrupt:
                self.konusma("Program sonlandırılıyor. Hoşça kalın!")
                break
            except Exception as e:
                print(f"❌ Hata oluştu: {e}")
                self.konusma("Bir sorun oluştu, tekrar deniyorum.")

if __name__ == "__main__":
    print("""
    🤖 Modern Sesli Asistan
    ----------------------
    👋 Hoş geldiniz!
    🎤 Mikrofon açık ve sizi dinliyorum...
    ❓ Yardım için 'yardım' diyebilirsiniz.
    """)
    
    asistan = ModernSesliAsistan()
    asistan.baslat() 