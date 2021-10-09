from __future__ import annotations
from abc import ABC, abstractmethod
"""korzystam z bibliotek, które implementują zagadnienia nie dostępne bezpośrednio w języku python 
(takie jak metody abstrakcyjne, interfejsy itp.) """


class Character:
    pass


class State(ABC):
    @property
    def character(self) -> Character:
        return self._character

    @character.setter
    def character(self, character: Character) -> None:
        self._character = character

    @abstractmethod
    def speak(self) -> None:
        pass


class Character:

    _state = None

    def __init__(self, state: State) -> None:
        self.setState(state)

    def setState(self, state: State) -> None:
        self._state = state
        self._state.character = self

    def currentState(self):
        return type(self._state).__name__

    def speak(self) -> None:
        self._state.speak()