try:
    from IPython import embed
except:
    pass

from game import Game
import players


class Referee(object):
    def __init__(self, neighborhood, game, players):
        self.neighborhood = neighborhood
        self.game = game
        self.players = players
        self.current_player = players[0]

    def start_game(self):
        while not self.__is_game_finished():
            self.players_next_move()

        # evalutate winner
        winner = self.__determine_winner()

        print winner
        # print output!!!!
        print "game over!"

    def players_next_move(self):
        # get the next move
        district = self.current_player.get_move()
        # submit the move
        self.__add_move_to_game_board(district)
        # change the player
        self.__change_player()

    def __change_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
        return

    def __add_move_to_game_board(self, district):
        return self.game.add_district(district)

    def __is_game_finished(self):
        return self.game.evaluate_game_state()

    def __player_from_party(self, party):
        for player in self.players:
            if player.party == party:
                return player

        return None

    def __determine_winner(self):
        p0_counter = 0
        p1_counter = 0
        for district in self.game.districts:
            if self.__determine_district_winner(district) == self.players[0]:
                p0_counter +=1
            elif self.__determine_district_winner(district) == self.players[1]:
                p1_counter +=1
            else:
                continue

        if p0_counter > p1_counter:
            return self.players[0]
        elif p0_counter < p1_counter:
            return self.players[1]
        else:
            return None

    def __determine_district_winner(self, district):
        r_count = 0
        d_count = 0
        for block in district.blocks:
            if block.party == "R":
                r_count += 1
            else:
                d_count += 1

        if r_count > d_count:
            return self.__player_from_party("R")
        elif r_count < d_count:
            return self.__player_from_party("D")
        else:
            return None
