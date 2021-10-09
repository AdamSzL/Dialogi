from helper import findStatementsByAuthor


class Player:

    def __init__(self, name):
        file = open('texts.json', )
        self.name = name
        self.counter = 0
        self.texts = findStatementsByAuthor(name)

    def speak(self):
        print(f'{self.name.upper()}: {self.texts[self.counter]}')
        self.counter += 1