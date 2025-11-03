from PyPDF2 import PdfReader
from gtts import gTTS
import os
import re
import tkinter as tk
from tkinter import filedialog

class PdfToSound:
    def __init__(self, window):
        self.window = window
        self.window.withdraw()
        self.text = ""
        self.remaining_text= None
        self.convert()

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(
            title="Bir PDF dosyası seçin",
            filetypes=[("PDF Dosyaları", "*.pdf")]
        )

    def read_pdf(self):
        if self.pdf_path:
            reader = PdfReader(self.pdf_path)
            for page in reader.pages:
                page_text = page.extract_text() or ""
                if page_text:
                    self.text += page_text + "\n"
            pattern = r"^\s*(?:file://\S+\s+)?(?:\[[^\]]*\]\s*)?(.*)$"
            match = re.match(pattern, self.text, flags=re.DOTALL)
            self.remaining_text = (match.group(1) if match else self.text).strip()

    def tts(self):
        out_path = "output.mp3"
        if self.pdf_path:
            base, _ = os.path.splitext(self.pdf_path)
            out_path = base + ".mp3"
        self.sound = gTTS(self.remaining_text, lang='en')
        self.sound.save(out_path)

    def convert(self):
        self.select_pdf()
        self.read_pdf()
        if self.remaining_text:
            self.tts()

window = tk.Tk()
PdfToSound(window)
