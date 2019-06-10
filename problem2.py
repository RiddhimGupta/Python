#pip install SpeechRecognition; pip install pyaudio
import speech_recognition as sr
from googlesearch import search
import time
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        url=[i for i in search(text,stop=10)]
        print(url," \n")
    except:
        print("Sorry could not recognize your voice")
        web=input("Please enter topic to be searched: ")
        url=[i for i in search(web,stop=10)]
        print(url," \n")
