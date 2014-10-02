class Game(object):
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood
        self.game_state = initialize_game_state(self)
        self.district_size = size(neighborhood.matrix)

    def is_legal_move(self):
        return

    def evaluate_game_state(self):
        return

    def __is_district_contiguous(self, district):
        return

    def __is_district_valid_size(self, district):
        return

    def __is_finished(self):
        return
