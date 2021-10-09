import json


def findStatementsByAuthor(author):
    file = open('texts.json')
    texts = []
    for statement in json.load(file):
        if author in statement:
            texts.append(statement[author])
        elif 'enemy' in statement:
            for subStatement in statement['enemy']:
                if author in subStatement:
                    texts.append(subStatement[author])
            for subStatement in statement['friend']:
                if author in subStatement:
                    texts.append(subStatement[author])
    return texts


def countStepsBetweenEnemyAndFriend(playerName):
    file = open('texts.json')
    count = 0
    for statement in json.load(file):
        if 'enemy' in statement:
            for subStatement in statement['enemy']:
                if playerName in subStatement:
                    count += 1
    return count