from neutral import Neutral
from enemy import Enemy
from friend import Friend
from player import Player
from character import Character
from conversation import Conversation


if __name__ == '__main__':
    player = Player('Lili')

    character = Character(Neutral('Peter'))

    conversation = Conversation(player, character)



