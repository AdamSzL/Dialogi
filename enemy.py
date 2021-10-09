from character import State
import json


class Enemy(State):
    def __init__(self, name):
        file = open('texts.json')
        self.allTexts = json.load(file)
        self.texts = []
        self.name = name
        self.counter = 0
        for statement in self.allTexts:
            if 'enemy' in statement:
                for subStatement in statement['enemy']:
                    if self.name in subStatement:
                        self.texts.append(subStatement[self.name])

    def speak(self) -> None:
        print(f'{self.name.upper()}: {self.texts[self.counter]}')
        self.counter += 1