import speech_recognition as sr
import pyttsx3
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-in')
                f1=open('speech.txt','a')
                f1.write(query)
            except Exception as e:
                return "Sorry! I cannot understand."
take_command()