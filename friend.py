from character import State
import enemy
import neutral


class Friend(State):
    def __init__(self):
        self.texts = ["Hello!", "Unfortunately, my sword was destroyed a few days ago :(",
                      "Ahh, I don't have much money", "Wow! That's cute!", "See you!"]

    def speak(self, counter) -> None:
        print(f'FRIEND: {self.texts[counter]}')