from src.game import Game
from src.utils import read_json_file

if __name__ == '__main__':

    data = read_json_file()
    g = Game(game_data=data)
