import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

#  This function will say the text which
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def greetUser():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        say("Good morning, sir!")
    elif current_hour < 18:
        say("Good evening, sir!")
    else:
        say("Good night, sir!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(query)
            return query
        except Exception as e:
            return "Sorry! I cannot understand."


# Initialize greeting based on the current time
greetUser()

say("I am Jarvis! How can I help you?")
while True:
    text = takeCommand()
    sites = [
        ['open google', 'https://www.google.com'],
        ['open youtube', 'https://www.youtube.com'],
        ['open facebook', 'https://www.facebook.com']
    ]
    for site in sites:
        if site[0] in text.lower():
            webbrowser.open(site[1])

    if 'open wikipedia' in text.lower():
        say("What should I search on Wikipedia, sir?")
        search_query = takeCommand()
        if search_query:
            results = wikipedia.summary(search_query, sentences=2)
            say(f"According to Wikipedia, {results}")

    elif 'open music' in text.lower():
        os.startfile("Jhol.mp3")

    elif 'tell time' in text.lower():
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        say(f"Sir, the time is {current_time}")

    elif 'open id' in text.lower():
        os.system('C:\\Users\\hp\\Documents\\prakhar\\C++\\ambiguity.cpp')

    elif text.lower() == 'stop':
        break

    # Repeat the user's command
    say(text)
