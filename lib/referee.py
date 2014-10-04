from game import Game

class Referee(object):
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood
        self.game = Game(self.neighborhood)

    def start_game(self):
        return

    def players_next_move(self):
        return

    def __current_turn(self):
        return

    def __add_move_to_game_board(self):
        return

    def __is_game_finished(self):
        return
