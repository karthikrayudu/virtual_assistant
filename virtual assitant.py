import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

# Initialize Text-to-Speech Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Function
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your virtual assistant. How can I help you?")

# Listen Function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# Respond Function
def respond(text):
    print(text)
    speak(text)

# Main Function
if name == "main":
    wish()
    while True:
        query = listen().lower()
        if 'wikipedia' in query:
            respond('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            respond("According to Wikipedia")
            respond(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'hello' in query:
            respond("hi i am karthiks virtual assistent")
        elif "what is the use of you" in query:
            speak("i am here to reduce your time and your work easy")
        elif 'play' in query:
            respond(f"Playing {query}")
            pywhatkit.playonyt(query)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'song' in query or 'story' in query or "video" in query or "insta" in query:
            respond(f"Playing {query}")
            pywhatkit.playonyt(query)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"The time is {strTime}")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'open snapchat' in query:
            webbrowser.open("snapchat.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'take a picture' in query or 'take a photo' in query or 'click a picture' in query:
         camera = cv2.VideoCapture(0)
         ret, frame = camera.read()
         cv2.imshow('Image', frame)
         cv2.waitKey(0)
         cv2.destroyAllWindows()
         cv2.imwrite('captured_image.jpg', frame)
         respond("Picture taken!")
        elif 'navigate to' in query:
         query = query.replace('navigate to ', '')
         location = query
         webbrowser.open(f"https://www.google.com/maps/place/{location}")
         respond(f"Opening Google Maps and navigating to {location}")
        elif 'exit' in query:
            respond("Goodbye!")
            break