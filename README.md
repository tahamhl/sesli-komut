# 🤖 Sesli-Komut Asistanı

Modern ve Türkçe konuşabilen bir sesli komut asistanı. Bilgisayarınızı sesli komutlarla kontrol edebilir, Google ve YouTube aramaları yapabilir, notlar alabilir ve daha fazlasını yapabilirsiniz.

## 🌟 Özellikler

- 🎯 Türkçe sesli komut algılama
- 🗣️ Doğal Türkçe konuşma (Google TTS)
- 💻 Uygulama kontrolü (açma/kapama)
- 🔍 Google ve YouTube aramaları
- ⏰ Saat ve tarih bilgisi
- 📝 Not alma
- 🎨 Modern ve kullanıcı dostu arayüz
- 🔊 Yüksek kaliteli ses çıkışı

## 🚀 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Çalışan bir mikrofon
- İnternet bağlantısı

### Adımlar

1. Repoyu klonlayın:
```bash
git clone https://github.com/tahamhl/sesli-komut.git
cd sesli-komut
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Programı çalıştırın:
```bash
python sesli_asistan.py
```

## 💡 Kullanım

Asistan başladığında aşağıdaki komutları kullanabilirsiniz:

### 📱 Uygulama Kontrolü
- "not defteri aç"
- "hesap makinesi çalıştır"
- "paint başlat"
- "tarayıcı kapat"

### 🔍 Arama
- "google hava durumu"
- "youtube en son haberler"

### ⏰ Zaman
- "saat kaç"
- "bugün günlerden ne"

### 📝 Not Alma
- "not toplantı yarın saat 3'te"

### ℹ️ Yardım
- "yardım" - tüm komutları listeler
- "çıkış" - programı sonlandırır

## 🛠️ Teknik Detaylar

- **Ses Tanıma**: Google Speech Recognition API
- **Ses Sentezi**: Google Text-to-Speech (gTTS)
- **Ses Çalma**: Pygame
- **Dil Desteği**: Türkçe

## ⚠️ Gereksinimler

```
SpeechRecognition==3.12.0
gTTS==2.5.4
pygame==2.5.2
pyaudio==0.2.14
```

## 🐛 Sorun Giderme

Ses tanıma sorunları için:
- Mikrofonunuzun doğru bağlandığından emin olun
- Sessiz bir ortamda çalıştırın
- İnternet bağlantınızı kontrol edin

Ses çıkışı sorunları için:
- Bilgisayar sesinin açık olduğundan emin olun
- Varsayılan ses çıkış cihazını kontrol edin
- Başka uygulamaların sesi kullanmadığından emin olun

## 👨‍💻 Geliştirici

- **Taha Mehel**
  - GitHub: [github.com/tahamhl](https://github.com/tahamhl)
  - Website: [tahamehel.tr](https://tahamehel.tr)

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın. 