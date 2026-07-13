import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Привет! Я ваш искусственный интеллект аватар.")
