## PDF to Speech (Python) — Türkçe / English

### Öz (TR)
- Bu betik, seçtiğiniz bir PDF dosyasından metni çıkarır ve gTTS ile MP3 ses dosyasına dönüştürür.
- Ücretsiz çalışır; API anahtarı gerektirmez.
- İnternet bağlantısı gereklidir (gTTS çevrimiçi hizmet kullanır).

#### Özellikler
- PDF seçme (dosya seçici), metin çıkarma, MP3 üretme
- Çıkış dosya adı, PDF adıyla aynıdır (ör. `example.pdf` → `example.mp3`).
- Basit arayüz (tkinter), tek tıkla dönüştürme

#### Sınırlamalar ve Notlar
- gTTS çevrimiçi servis kullandığından internet gerekir ve hız bağlantıya bağlıdır.
- Bazı PDF’lerde (özellikle taranmış/OCR’siz) metin çıkarımı boş dönebilir.
- Çok uzun metinlerde tek seferde TTS yavaşlayabilir veya kesintiye uğrayabilir.
- Gizlilik: Hassas içerikleri çevrimiçi TTS’e göndermeden önce değerlendirin.

#### Kurulum
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

`requirements.txt` içeriği:
```text
PyPDF2
gTTS
```

#### Kullanım
```bash
python main.py
```
1) PDF dosyasını seçin.
2) İşlem bittiğinde aynı klasörde `PDF_ADI.mp3` oluşur.

#### Dil (Language)
- Varsayılan dil: İngilizce (`en`).
- Türkçe çıktı için `main.py` içinde `gTTS(..., lang='en')` ifadesini `lang='tr'` olarak değiştirin.

#### Teknik Ayrıntılar
- Metin çıkarımı: PyPDF2 `extract_text()`
- Baş kısımdaki olası `file://...` ve `[...]` bloklarını güvenli regex ile temizleme
- Basit tkinter penceresi ile PDF seçimi

---

### Summary (EN)
- This script extracts text from a chosen PDF and converts it to an MP3 using gTTS.
- It’s free to use and does not require an API key.
- Internet connection is required (gTTS runs online).

#### Features
- File picker to select PDF, text extraction, MP3 generation
- Output filename mirrors PDF name (e.g., `example.pdf` → `example.mp3`).
- Minimal tkinter UI for quick conversion

#### Limitations and Notes
- Requires internet; performance depends on network conditions.
- Some PDFs (especially scanned without OCR) may not yield extractable text.
- Very long texts may be slow or interrupted in a single TTS call.
- Privacy: Avoid sending sensitive PDFs to online services.

#### Setup
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

`requirements.txt`:
```text
PyPDF2
gTTS
```

#### Usage
```bash
python main.py
```
1) Select a PDF.
2) When done, `PDF_NAME.mp3` is generated in the same folder.

#### Language
- Default language: English (`en`).
- For Turkish output, change `gTTS(..., lang='en')` to `lang='tr'` inside `main.py`.

#### Technical Details
- Text extraction via PyPDF2 `extract_text()`
- Safe regex cleanup for optional header like `file://...` and `[...]`
- Simple tkinter file chooser


