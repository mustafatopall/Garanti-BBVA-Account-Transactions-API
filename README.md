# 💼 Garanti BBVA İşlem Sorgulama Uygulaması

Bu proje, **Garanti BBVA API** üzerinden belirli hesaplara ait işlem geçmişini sorgulamak ve kullanıcıya tablo şeklinde sunmak için geliştirilmiştir.

## 🚀 Özellikler

- 🔐 Garanti BBVA API üzerinden **OAuth 2.0** ile access token alımı
- 💳 Belirli bir hesap için **işlem geçmişi sorgulama**
- 📊 JSON ile gelen verilerin **Tkinter** arayüzünde tablo halinde gösterilmesi
- 🧩 Temiz ve **modüler yapı** ile kolay genişletilebilirlik

---

## 🛠️ Kurulum

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/kullaniciadi/garantibbva-islem-sorgulama.git
cd garantibbva-islem-sorgulama
```

### 2. Sanal Ortam 

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# veya
.venv\Scripts\activate     # Windows
```

### 3. Gerekli Python Paketlerini Yükleyin

```bash
pip install -r requirements.txt
```

#### `requirements.txt` içeriği:

```
certifi==2025.4.26
charset-normalizer==3.4.2
idna==3.10
requests==2.32.4
tabulate==0.9.0
urllib3==2.4.0
```

---

## ⚙️ Yapılandırma

`config.py` dosyasını **kendi API uygulama bilgilerinize göre** düzenleyin 
(https://www.garantibbva.com.tr/isim-icin/dijital-bankacilik/garanti-bbva-api-store buradan gerekli bilgiyi edinebilirsiniz) :

```python
# config.py
CLIENT_ID = "UYGULAMA_CLIENT_IDINIZ"
CLIENT_SECRET = "UYGULAMA_CLIENT_SECRETINIZ"
REDIRECT_URL = "https://sizin_kendi_sunucunuz/callback_endpointiniz"
TOKEN_URL = "https://apis.garantibbva.com.tr/auth/oauth/v2/token"
API_URL = "https://apis.garantibbva.com.tr/balancesandmovements/accountinformation/transaction/v1/gettransactions"
SCOPE = "oob"
```

---

## ▶️ Kullanım

```bash
python main.py
```

Uygulama:

1. API'den token alır
2. Belirttiğiniz hesap bilgileriyle işlem sorgulaması yapar
3. Gelen verileri bir **Tkinter arayüzünde** tablo şeklinde gösterir

---

## 📁 Proje Yapısı

```
garantibbva-islem-sorgulama/
│
├── main.py              # Uygulamanın başlangıç dosyası
├── config.py            # API yapılandırma bilgileri
├── token_manager.py     # Token alma işlemleri
├── api_client.py        # API çağrıları
├── json_parser.py       # Gelen JSON verisini işler
├── data_display.py      # Verileri Tkinter tablosunda gösterir
├── requirements.txt     # Bağımlılık listesi
```

---

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz!

- Bug bildirin 🐛
- Özellik önerin ✨
- Fork + Pull Request gönderin ✅

---

## 📝 Lisans

MIT Lisansı altında sunulmuştur. Detaylar için `LICENSE` dosyasına göz atabilirsiniz.
