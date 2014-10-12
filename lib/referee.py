from game import Game
import players
import sys

class Referee(object):
    def __init__(self, neighborhood, game, players):
        self.neighborhood = neighborhood
        self.game = game
        self.players = players
        self.current_player = players[0]

    def start_game(self):
        while not self.__is_game_finished():
            sys.stdout.write(".")
            sys.stdout.flush()
            self.players_next_move()

        #print Information
        print ""
        self.__print_players()
        self.__print_district_assigments()
        self.__print_district_winners()
        self.__print_election_outcome()

    def players_next_move(self):
        # Get the next move
        district = self.current_player.get_move()

        # Submit the move if valid
        assert(self.__add_move_to_game_board(district))

        # Change the player
        self.__change_player()

    def __change_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

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
        parties = [block.party for block in district.blocks]

        if parties.count("R") > parties.count("D"):
            return self.__player_from_party("R")
        elif parties.count("R") < parties.count("D"):
            return self.__player_from_party("D")
        else:
            return None

    def __print_players(self):
        self.__print_divider()
        for player in self.players:
            print player.__class__.__name__, "=", player.party
        self.__print_divider(True)

    def __print_district_assigments(self):
        self.__print_divider()
        for i, district in enumerate(self.game.districts):
            print "District", str(i+1) + ":", district.inspect()
        self.__print_divider(True)

    def __print_district_winners(self):
        self.__print_divider()
        for i, district in enumerate(self.game.districts):
            player = self.__determine_district_winner(district)
            if player == None:
                party = "Tie"
            else:
                party = player.party
            print "District", str(i+1) + ":", party
        self.__print_divider(True)

    def __print_election_outcome(self):
        self.__print_divider()
        winner = self.__determine_winner()
        if winner == None:
            party = "Tie"
        else:
            party = winner.party
        print "Election outcome:", party, "wins"
        self.__print_divider(True)

    def __print_divider(self, spacer = False):
        print "*" * 38
        if spacer:
            print ""
