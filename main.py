import os 
from gtts import gTTS
from pypdf import PdfReader
from tkinter.filedialog import *

# Open pdf file 
book = askopenfilename()

pdf_reader = PdfReader(book)
number_of_pages = len(pdf_reader.pages)
page = pdf_reader.pages[0]
text = page.extract_text()

# Pass text to TTS
tts = gTTS(text)

# Save as a audio file
dir_path = os.path.dirname(os.path.realpath(__file__))
tts.save(dir_path + "\\test.mp3")