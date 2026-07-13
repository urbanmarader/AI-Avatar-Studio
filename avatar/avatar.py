from avatar.voice import speak


class Avatar:
    def __init__(self, name):
        self.name = name

    def talk(self, text):
        print(f"{self.name}: {text}")
        speak(text)


if __name__ == "__main__":
    my_avatar = Avatar("AI Avatar")
    my_avatar.talk("Привет! Я ваш говорящий искусственный интеллект.")
