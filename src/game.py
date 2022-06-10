from .base import GameChampion, Player
from typing import List, Any


class Game:
    players: List[Player]
    game_champion_list = List[GameChampion]

    def __init__(self, game_data: dict):
        print("Welcome to TalanaKombat")
        print("Loading champions data")
        self.load_champions()
        print("Creating match")
        self.create_game(game_data)

    def load_champions(self, data: List[dict[str, Any]]) -> None:
        for item in data:
            self.game_champion_list.append(GameChampion(**item))
        print("Champions information successfully loaded")

    def find_selected_champion(self, champion_name: str):
        selected_champion = next(filter(lambda x: x.name == champion_name, self.game_champion_list), None)
        if not selected_champion:
            raise ValueError(f"champion {champion_name} does not exists")
        return selected_champion

    def add_player(self, name: str, **kwargs):
        moves = [' '.join(x) for x in zip(kwargs.get('movements'), kwargs.get('hits'))]
        selected_champ = self.find_selected_champion(kwargs.get('character_name'))
        player = Player(
            name=name,
            champion=selected_champ,
            moves=moves
        )
        self.players.append(player)

    def create_game(self, data: dict[str, Any]):
        player1 = data.get("player1")
        self.add_player(name='Player1', **player1)
        player2 = data.get("player2")
        self.add_player(name='Player2', **player2)

    def play_game(self):
        pass
