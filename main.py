import pyttsx3                      # Text-to-speech library
from pypdf import PdfReader         # PDF text extraction library
from tkinter.filedialog import *    # For the file open dialog window

file = askopenfilename()            

# Load the selected PDF and get its total page count
pdfreader = PdfReader(file)
pages = len(pdfreader.pages)

# Initialize the TTS engine
speaker = pyttsx3.init()

# Read through book pages
for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()     
    
    speaker.say(text)               
    speaker.runAndWait()     
           