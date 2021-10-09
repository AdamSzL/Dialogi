from character import State
import json


class Friend(State):
    def __init__(self, name):
        file = open('texts.json')
        self.allTexts = json.load(file)
        self.texts = []
        self.counter = 0
        self.name = name
        for statement in self.allTexts:
            if 'friend' in statement:
                for subStatement in statement['friend']:
                    if self.name in subStatement:
                        self.texts.append(subStatement[self.name])

    def speak(self) -> None:
        print(f'{self.name.upper()}: {self.texts[self.counter]}')
        self.counter += 1