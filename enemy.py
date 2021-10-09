from character import State
import neutral
import friend


class Enemy(State):
    def __init__(self):
        self.texts = ["What did you say?!", "You have no chance!", "Nice joke!", "From your death!", "I will get a revenge!"]

    def speak(self, counter) -> None:
        print(f'ENEMY: {self.texts[counter]}')