import speech_recognition as sr
import pyautogui
import time

# Map voice commands to game actions (keys)
voice_to_key = {
    "jump": "space",
    "shoot": "ctrl",
    "reload": "r",
    "crouch": "c",
    "sprint": "shift",
    "pause": "esc",
    "forward": "w",
    "backward": "s",
    "left": "a",
    "right": "d"
}

def recognize_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"✅ You said: {command}")
        return command
    except sr.UnknownValueError:
        print("⚠️ Couldn't understand. Try again.")
    except sr.RequestError as e:
        print(f"⚠️ Error from recognition service: {e}")
    return ""

def handle_command(command):
    for voice_cmd, key in voice_to_key.items():
        if voice_cmd in command:
            pyautogui.press(key)
            print(f"🎮 Action performed: {voice_cmd} ➜ {key}")
            return
    print("❌ No matching command.")

# 🚀 Start listening loop
print("🕹️ Voice Command Controller Ready!")
time.sleep(1)

while True:
    spoken = recognize_command()
    if "exit" in spoken or "quit" in spoken:
        print("👋 Exiting...")
        break
    handle_command(spoken)
