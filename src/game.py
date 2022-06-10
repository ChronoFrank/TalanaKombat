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
        moves = [''.join(x) for x in zip(kwargs.get('movements'), kwargs.get('hits'))]
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
        print(f"{self.players[0]} will start the match")

    def is_game_over(self):
        if True in [player.end_flag for player in self.players]:
            return True
        else:
            return False

    def play_game(self):
        self.define_players_order()
        player = self.players[0]
        other_player = self.players[1]
        while not self.is_game_over():
            print('-' * 30)
            print(f"{player.name}'s turn to move")
            attack = player.make_move()
            if attack:
                other_player.take_damage(attack.energy_points)
                print(f"{other_player.selected_champion.name} has"
                      f" {other_player.check_life_points()} life points remaining")
            if other_player.check_life_points() == 0:
                print('\n')
                print('-' * 30)
                print(f"Congratulations {player.name} you are the winner")
                break
            print('-'*30)
            print(f"{other_player.name}'s turn to move")
            attack = other_player.make_move()
            if attack:
                player.take_damage(attack.energy_points)
                print(f"{player.selected_champion.name} has"
                      f" {player.check_life_points()} life points remaining")

            if player.check_life_points() == 0:
                print('\n')
                print('-' * 30)
                print(f"Congratulations {other_player.name} you are the winner")

        if self.is_game_over() and player.check_life_points() > 0 and other_player.check_life_points() > 0:
            if player.check_life_points() == other_player.check_life_points():
                print('\n')
                print('-' * 30)
                print(f"The match is a tie")
            elif player.check_life_points() < other_player.check_life_points():
                print('\n')
                print('-' * 30)
                print(f"Congratulations {other_player.name}"
                      f" you are the winner because you have higher life points")
            else:
                print('\n')
                print('-' * 30)
                print(f"Congratulations {player.name} "
                      f"you are the winner because you have higher life points")
