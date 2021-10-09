from character import State
import json


class Neutral(State):
    def __init__(self, name):
        file = open('texts.json')
        self.allTexts = json.load(file)
        self.texts = []
        self.name = name
        self.counter = 0
        for statement in self.allTexts:
            if 'enemy' not in statement and 'friend' not in statement and self.name in statement:
                self.texts.append(statement[self.name])

    def speak(self) -> None:
        print(f'{self.name.upper()}: {self.texts[self.counter]}')
        self.counter += 1