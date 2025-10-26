import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import cv2  # For opening the camera

# Function to make the system speak
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the current time
def greetUser():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        say("Good morning, sir!")
    elif current_hour < 18:
        say("Good evening, sir!")
    else:
        say("Good night, sir!")

# Function to take voice commands from the user
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
            print("Sorry! I cannot understand.")
            return None

# Function to open the camera
def open_camera():
    try:
        cap = cv2.VideoCapture(0)  # Opens the default camera
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture video.")
                break
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to close the camera
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error opening camera: {e}")

# Function to open a particular value (e.g., retrieving specific key-value pairs)
def open_value(value):
    # For example, search a value from a dictionary
    my_data = {"name": "Prakhar", "age": 20, "city": "Muzaffarnagar"}
    if value in my_data:
        say(f"The value for {value} is {my_data[value]}")
        print(f"The value for '{value}' is: {my_data[value]}")
    else:
        say("The value is not available.")
        print("The value is not available.")

# Initialize greeting based on the current time
greetUser()

say("I am Jarvis! How can I help you?")
while True:
    text = takeCommand()
    if not text:
        continue

    # Opening predefined websites
    sites = [
        ['open google', 'https://www.google.com'],
        ['open youtube', 'https://www.youtube.com'],
        ['open facebook', 'https://www.facebook.com']
    ]
    for site in sites:
        if site[0] in text.lower():
            webbrowser.open(site[1])
            say(f"Opening {site[0].split()[1]} for you.")
            break

    if 'open wikipedia' in text.lower():
        say("What should I search on Wikipedia, sir?")
        search_query = takeCommand()
        if search_query:
            results = wikipedia.summary(search_query, sentences=2)
            say(f"According to Wikipedia, {results}")
            print(results)

    elif 'open music' in text.lower():
        os.startfile("Jhol.mp3")

    elif 'tell time' in text.lower():
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        say(f"Sir, the time is {current_time}")

    elif 'open id' in text.lower():
        os.system('C:\\Users\\hp\\Documents\\prakhar\\C++\\ambiguity.cpp')

    elif 'open camera' in text.lower():
        say("Opening the camera, sir.")
        open_camera()

    elif 'open value' in text.lower():
        say("What value should I open, sir?")
        value_query = takeCommand()
        if value_query:
            open_value(value_query.lower())

    elif text.lower() == 'stop':
        say("Goodbye, sir!")
        break

    # Repeat the user's command (for debugging purposes)
    say(text)
