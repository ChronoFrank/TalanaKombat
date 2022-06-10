from .base import GameChampion, Player
from typing import List, Any
from .utils import BASE_JSON_CHAMPION_FILE_PATH, read_json_file


class Game:
    players: List[Player] = []
    game_champion_list: List[GameChampion] = []
    end_game = False
    victory = None

    def __init__(self, game_data: dict):
        print("Welcome to TalanaKombat")
        print("Loading champions data")
        self.load_champions()
        print("Creating match")
        self.create_game(game_data)

    def load_champions(self) -> None:
        data = read_json_file(file_path=BASE_JSON_CHAMPION_FILE_PATH)
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

    def define_players_order(self):
        player1_moves = self.players[0].count_first_move()
        player2_moves = self.players[1].count_first_move()
        if player1_moves.get("combinations") == player2_moves.get("combinations"):
            if player1_moves.get("movements") == player2_moves.get("movements"):
                if (
                        player1_moves.get("attacks") != player2_moves.get("attacks")
                        and
                        player1_moves.get("attacks") > player2_moves.get("attacks")
                ):
                    self.players.reverse()
            elif player1_moves.get("movements") > player2_moves.get("movements"):
                self.players.reverse()
        elif player1_moves.get("combinations") > player2_moves.get("combinations"):
            self.players.reverse()
        print(player1_moves, player2_moves)
        print(f"Player {self.players[0]} will start the match")

    def play_game(self):
        self.define_players_order()


