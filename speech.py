import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speech speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

    return query.lower()

def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if "time" in query:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_str}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            topic = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("Sorry, I couldn't find that on Wikipedia.")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I don't understand that command.")

if _name_ == "_main_":
    run_assistant

