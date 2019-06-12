#pip install SpeechRecognition; pip install pyaudio
import speech_recognition as sr
from googlesearch import search
import time
r = sr.Recognizer()
with sr.Microphone(device_index=9) as source:
    print("Speak Anything :")
    r.adjust_for_ambient_noise(source)
    audio = r.record(source, duration=2.8)
    try:
        text = r.recognize_google(audio)
        print("You said : {}"+text)
    except:
        print("Sorry could not recognize your voice")
web=input("Please enter topic to be searched: ")
url=[i for i in search(web,stop=10)]
print(url," \n")
