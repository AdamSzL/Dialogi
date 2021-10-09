from character import State
import enemy
import friend


class Neutral(State):
    def __init__(self):
        self.texts = ["It's ok. What about you?", "Ok. By the way the weather is really good",
                      "I have to go to the blacksmith", "Ok.", "Bye!"]

    def speak(self, counter) -> None:
        print(f'NEUTRAL: {self.texts[counter]}')