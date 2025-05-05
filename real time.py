import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import tempfile

def speak(text, lang='fr'):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            playsound.playsound(fp.name)
    except Exception as e:
        print("TTS Error:", e)

def main():
    recognizer = sr.Recognizer()
    translator = Translator()
    target_lang = 'fr'  # Change to desired language code (e.g., 'hi', 'es', etc.)

    print("Speak something (say 'exit' to quit):")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("\nListening...")
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                print("You said:", text)

                if "exit" in text.lower():
                    print("Goodbye!")
                    break

                translated = translator.translate(text, dest=target_lang).text
                print("Translated:", translated)
                speak(translated, lang=target_lang)

            except sr.UnknownValueError:
                print("Didn't catch that. Try again.")
            except sr.RequestError:
                print("Network error. Check your internet.")
            except sr.WaitTimeoutError:
                print("Timeout. Speak faster!")

if _name_ == "_main_":
    main()
