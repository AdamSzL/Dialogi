from neutral import Neutral
from enemy import Enemy
from friend import Friend
from player import Player
from character import Character


if __name__ == '__main__':
    player = Player()

    # dialog z wrogiem
    # character = Character(Enemy())
    # player.startConversation(character)

    # dialog z przyjazną podstacią
    # character = Character(Friend())
    # player.startConversation(character)

    # dialog z neutralną postacią
    character = Character(Neutral())
    player.startConversation(character)

    # zmiana stanu
    character.setState(Enemy())
    player.startConversation(character)


