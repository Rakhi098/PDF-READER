import PyPDF2
import pyttsx3

book = open('a.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print('number of pages in pdf:',pages)
speaker = pyttsx3.init()
for num in range(3, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
