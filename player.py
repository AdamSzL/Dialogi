from character import State
import json


class Player:

    def __init__(self):
        file = open('playerTexts.json', )
        self.allTexts = json.load(file)
        self.texts = []

    def startConversation(self, character: State):
        # character.currentState() zwraca aktualny stan, na podstawie którego pobieram odpowiedni dialog z pliku json
        self.texts = self.allTexts[character.currentState()]
        print('---     Starting conversation    ---')
        print('--- Press X to stop conversation ---')
        print('--- Press 1, 2 or 3 to talk ---')
        print()
        self.speakWith(character)

    def speakWith(self, character: State):
        for i in range(len(self.texts)):
            print()
            for j, text in enumerate(self.texts[i]):
                print(f'{j + 1}. {text}')
            shouldStop = False
            while True:
                valid = False
                selectedOption = input('Enter your selection: ')
                if selectedOption == 'X':
                    shouldStop = True
                    break
                elif selectedOption.isnumeric():
                    if int(selectedOption) in [1, 2, 3]:
                        print(f'PLAYER: {self.texts[i][int(selectedOption) - 1]}')
                        character.speak(i)
                        valid = True
                if valid:
                    break
                else:
                    print('You entered an invalid selection')
            if shouldStop:
                break
        print()