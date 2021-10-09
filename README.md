# 'State design pattern' - dialogi

### Pliki:
* *main.py* (plik zawierający główny skrypt aplikacji, importujący wszystkie pozostałe moduły)
* *character.py* (plik implementujący klasę Character, reprezentującą postać, z którą nasz gracz rozmawia,
zawiera ona podstawowe metody zmiany stanu, przechowuje referencje do aktualnego *State*, posiada również
funkcję currentState, która zwraca aktualny stan postaci oraz interfejs State, który jest później
implementowany przez każdy z konkretnych State'ów)
* *player.py* (klasa naszego gracza, zawiera funkcję startConversation i speakWith)
* *friend.py* (konkretna klasa odpowiedzialna za stan *Przyjaciel*, implementuje interfejs State)
* *enemy.py* (stan *Wróg*)
* *neutral.py* (stan *Neutralny*)
* *playerTexts.json* (zawiera przykładowe teksty, które różnią się w zależności, z jaką postacią gracz rozmawia)