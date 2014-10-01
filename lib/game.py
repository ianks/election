class Game(object):
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood
        self.game_state = initialize_game_state(self)
        self.current_player = initialize_current_player(self)
        self.district_size = size(neighborhood.matrix)

    def is_legal_move(self):
        return

    def evaluate_game_state(self):
        return

    def current_player(self):
        return

    def __is_district_contiguous(self, district):
        return

    def __is_district_valid_size(self, district):
        return

    def print_assigned_districts(self):
        return

    def print_awarded_districts(self):
        return

    def print_election_outcome(self):
        return

    def __is_finished(self):
        return
