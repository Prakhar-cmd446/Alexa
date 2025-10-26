import os
from time import strftime
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
from openai import audio


def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(query)
            return  query
        except Exception as e:
            return "Sorry ! I can not understand "
say('hello i am Jarvis ! how I can help u')
while True:
    print("listening ")
    text =takeCommand()
    sites=[['open google', 'https://www.google.com'],['open youtube','https://www.youtube.com'],['open facebook','https://www.facebook.com']]
    for site in sites:
        if site[0] in text.lower():
            webbrowser.open(site[1])
    if 'open music' in text.lower():
        os.startfile("Jhol.mp3")
    elif 'tell time' in text.lower():
        strftime=datetime.datetime.now().strftime('%H:%M:%S')
        say(f'SIR THE TIME IS {strftime}')
    elif 'open id' in text.lower():
        os.system(' C:\\Users\\hp\\Documents\\prakhar\\C++\\ambiguity.cpp')
    elif text=='stop':
        break
    say(text)
