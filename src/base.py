from typing import List
from enum import Enum

MOVES = ('W', 'A', 'S', 'D')
ACTIONS = ('P', 'K')


class MovesMapping(Enum):
    W = "Moves one space up"
    A = "Moves one space to the left"
    S = "Moves one space down "
    D = "Moves one space to the right"


class ChampionTechniques:
    """Basic representation of a character techniques."""

    name: str = 'technique'
    energy_points: int = 1
    combination: str = ''

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.energy_points = kwargs.get('energy_points')
        check = any(action in kwargs.get('combination') for action in ACTIONS)
        if not check:
            raise ValueError('A combination must have at least one action P or K')
        self.combination = kwargs.get('combination')

    def __str__(self):
        return f"use {self.name} that deals {self.energy_points} damage"


class GameChampion:
    """Basic representation of a game character."""

    name: str = 'N.N'
    techniques: dict[str, ChampionTechniques] = {}

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        for tech in kwargs.get('techniques'):
            new_technique = ChampionTechniques(**tech)
            self.techniques.update({new_technique.combination: new_technique})

    def attack(self, move):
        if self.is_technique(move):
            return self.techniques.get(move)
        else:
            aux = None
            for _move in move:
                if self.techniques.get(_move):
                    aux = self.techniques.get(_move)
                else:
                    print(f"{self.name} {MovesMapping[_move].value}")
            return aux

    def is_technique(self, move):
        return True if self.techniques.get(move) else False


class Player:
    """Basic representation of a game player."""

    name: str
    life_points: int = 6
    end_flag: bool = False
    selected_champion: GameChampion
    moves: List[str] = []

    def __init__(self, name: str, champion: GameChampion, moves: List[str]):
        self.name = name
        self.selected_champion = champion
        self.moves = moves
        self.iter_moves = iter(self.moves)
        print(f"{name} selects champion {champion.name}")

    def __str__(self):
        return self.name

    def check_life_points(self) -> int:
        return self.life_points

    def take_damage(self, hit_points: int) -> int:
        remaining_points = self.life_points - hit_points
        if remaining_points <= 0:
            self.end_flag = True
            self.life_points = 0
        else:
            self.life_points = remaining_points
        return self.life_points

    def count_first_move(self) -> dict[str, int]:
        first_move = self.moves[0]
        # count combination
        combinations = len(first_move)
        # count movements
        movements = 0
        for item in MOVES:
            movements += first_move.count(item)
        # count attacks
        attacks = 0
        for item in ACTIONS:
            attacks += first_move.count(item)

        return {"combinations": combinations, "movements": movements, "attacks": attacks}

    def make_move(self):
        try:
            move = next(self.iter_moves)
            attack = self.selected_champion.attack(move)
            if attack:
                print(f'{self.selected_champion.name} {attack}')
                return attack
        except StopIteration:
            self.end_flag = True
