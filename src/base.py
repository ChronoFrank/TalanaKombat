from typing import Protocol, List

MOVES = ('W', 'A', 'S', 'D')
ACTIONS = ('P', 'K')


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


class GameChampion:
    """Basic representation of a game character."""

    name: str = 'N.N'
    techniques: List[ChampionTechniques] = []

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        for tech in kwargs.get('techniques'):
            new_technique = ChampionTechniques(**tech)
            self.techniques.append(new_technique)


class Player:
    """Basic representation of a game player."""

    name: str
    life_points: int = 6
    selected_champion: GameChampion
    moves: List[str] = []

    def __init__(self, name: str, champion: GameChampion, moves: List[str]):
        self.name = name
        self.selected_champion = champion
        self.moves = moves
        print(f"{name} selects champion {champion.name}")

    def check_life_points(self) -> int:
        return self.life_points

    def take_damage(self, hit_points: int) -> int:
        remaining_points = self.life_points - hit_points
        if remaining_points < 0:
            self.life_points = 0
        else:
            self.life_points = remaining_points

        return self.life_points
