from src.game import Game
from src import utils

if __name__ == '__main__':

    data = utils.read_json_file(utils.BASE_JSON_GAME_FILE_PATH)
    g = Game(game_data=data)
    g.play_game()
