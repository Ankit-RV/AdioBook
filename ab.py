'''Installation:
we will require two libraries (pyttsx3, PyPDF2) to develop an audiobook.
You can install the libraries from PyPl,
pip install PyPDF2
pip install pyttsx3'''

'''1) Read the PDF file:
Python has library PyPDF2 which is built as a PDF toolkit. It allows pdf manipulation in memory. 
This library is capable of:
extracting document information, such as title, author, etc
splitting documents by page
merging documents by page
cropping pages
merging multiple pages into a single page
encrypting and decrypting PDF files
and more!
We are using this library to split the pdf file page by page, 
read the text on each page, and send the text to the next layer/step.'''
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('BookName.pdf', 'rb'))

'''2) Initialize Speaker:
Python has a library pyttsx3, that is capable to convert text-to-speech offline.
Text that we are reading from a pdf file using the pypdf2 library is fed as an input to the text-to-speech engine.'''
import pyttsx3
speaker = pyttsx3.init()

'''3) Play the Audiobook:
Extract the text from the pdf file page by page using the PyPDF2 implementation.
Loop through each page, by reading the text and feeding it to the pyttsx3 speaker engine.
It will read out loud the text from the pdf page.
Loop the process for every page in the pdf file and stop the pyttsx3 speaker engine as last.'''
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

'''Changing Voice, Rate, and Volume of pyttsx3 speaker:
You can tune the speed and volume of speech, and change the voice-over from male to female and vice-versa, depending on your requirements.
Rate of Speed:
Initialize the pyttsx3 library, and use getProperty(‘rate’)
to get the current speaking rate. Change the rate of speaking using setProperty(‘rate’, x), where x=100 being normal speed (1x).'''
# Initialize the speaker
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
print(rate)
speaker.setProperty('rate', 125)

'''Voice:
Initialize the pyttsx3 library, and use getProperty(‘voice’) to get the current gender of the speaker. 
Change the speaker's gender using setProperty(‘voice’, voice[x].id), where x=0 for male and x=1 for female.'''

voices = speaker.getProperty('voices')
print(voices)
#changing index, changes voices, 0 for male
speaker.setProperty('voice', voices[0].id)
#changing index, changes voices, 1 for female
speaker.setProperty('voice', voices[1].id)

'''Volume:
Initialize the pyttsx3 library, and use getProperty(‘volume’) to get the current volume. Use setProperty(‘volume’, x) to change the speaker’s volume.
The volume ranges from 0 to 1, where 0 is the min volume and 1 being the max volume.'''
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)

'''Saving Voice to Audio file:
Use the below method to save the audio output (audiobook) to the mp3 file.'''
engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()

'''Conclusion:
In this project, I have covered the implementation of a basic audiobook, that can read the entire pdf book using a few lines of python code.
For better audio results you can also tune the voice, rate, and volume of the speaker library.
The end audio result of the audiobook is not that good, as the text needs some preprocessing before feeding to the speaker engine.'''
