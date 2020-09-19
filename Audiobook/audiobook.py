import pyttsx3
import PyPDF2
book = open('critical_thinking.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

engine = pyttsx3.init()
engine.setProperty('rate',170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
for num in range(25, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
