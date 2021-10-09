import json
from player import Player
from character import State
from enemy import Enemy
from friend import Friend
from helper import countStepsBetweenEnemyAndFriend


class Conversation:
    def __init__(self, player: Player, character: State):
        file = open('texts.json')
        conversation = json.load(file)
        self.player = player
        self.character = character
        self.startConversation(conversation)

    def startConversation(self, conversation):
        for statement in conversation:
            if 'Narrator' in statement:
                print(f'NARRATOR: {statement["Narrator"]}')
            elif self.player.name in statement:
                self.player.speak()
            elif self.character._state.name in statement:
                self.character.speak()
            elif 'enemy' in statement:
                print()
                print('--- WYBIERZ, CO POWIEDZIEC ---')
                print(f'--- 1. {statement["enemy"][0][self.player.name]}')
                print(f'--- 2. {statement["friend"][0][self.player.name]}')
                print(f'--- Wcisnij X, aby zakonczyc konwersacje ---')
                while True:
                    valid = False
                    selectedOption = input('Nacisnij 1, albo 2: ')
                    if selectedOption == 'X':
                        break
                    elif selectedOption.isnumeric():
                        if int(selectedOption) == 1:
                            self.character.setState(Enemy(self.character._state.name))
                            valid = True
                        elif int(selectedOption) == 2:
                            self.character.setState(Friend(self.character._state.name))
                            valid = True
                    if valid:
                        break
                    else:
                        print('You entered an invalid selection')
                if selectedOption == '1':
                    print()
                    self.startConversation(statement['enemy'])
                elif selectedOption == '2':
                    print()
                    self.player.counter += countStepsBetweenEnemyAndFriend(self.player.name)
                    self.startConversation(statement['friend'])