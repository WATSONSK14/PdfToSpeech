## PDF to Speech (Python)

### Summary
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
