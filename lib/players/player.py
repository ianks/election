try:
    from IPython import embed
except:
    pass

import copy

from .. import game_elements


class Player(object):
  def __init__(self, game, party):
    self.party = party
    self.game = game

  def get_move(self):
    b1 = self.game.neighborhood.block_at_location(0,0)
    b2 = self.game.neighborhood.block_at_location(0,1)
    b3 = self.game.neighborhood.block_at_location(0,2)
    b4 = self.game.neighborhood.block_at_location(0,3)

    b5 = self.game.neighborhood.block_at_location(1,0)
    b6 = self.game.neighborhood.block_at_location(1,1)
    b7 = self.game.neighborhood.block_at_location(1,2)
    b8 = self.game.neighborhood.block_at_location(1,3)

    b9 = self.game.neighborhood.block_at_location(2,0)
    b10 = self.game.neighborhood.block_at_location(2,1)
    b11 = self.game.neighborhood.block_at_location(2,2)
    b12 = self.game.neighborhood.block_at_location(2,3)

    b13 = self.game.neighborhood.block_at_location(3,0)
    b14 = self.game.neighborhood.block_at_location(3,1)
    b15 = self.game.neighborhood.block_at_location(3,2)
    b16 = self.game.neighborhood.block_at_location(3,3)

    valid_district_1 = game_elements.district.District([b1,b2,b3,b4])
    valid_district_2 = game_elements.district.District([b5,b6,b7,b8])
    valid_district_3 = game_elements.district.District([b9,b10,b11,b12])
    valid_district_4 = game_elements.district.District([b13,b14,b15,b16])

    if self.game.is_legal_move(valid_district_1):
      return valid_district_1
    if self.game.is_legal_move(valid_district_2):
      return valid_district_2
    if self.game.is_legal_move(valid_district_3):
      return valid_district_3
    if self.game.is_legal_move(valid_district_4):
      return valid_district_4

  # Find the optimal min/max move
  # TODO: Refactor to return the value AND the action (which district to play)
  def __minimax(self, game_orig, depth, is_max, take_action = None):

    # make a copy so we dont screw up the current game state
    game = copy.deepcopy(game_orig)

    if take_action:
      game.add_district(take_action)

    # Max Depth of tree reached
    if depth == 0 or self.__is_terminal(game):
      return self.__utility(game)

    # Player is Max:
    if is_max:
      best_value = Move(None, float("-inf"))
      for action in self.__actions(game):
        value = self.__minimax(game, depth-1, False, action)
        best_value = max([value, best_value], key = lambda move: move.value)
      return best_value

    # Player is Min:
    else:
      best_value = Move(None, float("-inf"))
      for action in self.__actions(game):
        value = self.__minimax(game, depth-1, True, action)
        best_value = min([value, best_value], key = lambda move: move.value)
      return best_value

  # Returns a list of actions or moves given the game game
  def __actions(self,game):
    pass

  # Returns the utility of an end game (who is winning at that point)
  def __utility(self, game):
    # needs to return a move object

    # TODO: Fix so it is not hard coded
    max_player.party = "R"
    min_player.party = "D"

    value = 0
    for district in game.districts:
      if game.district_winner(district) == max_player.party:
        value += 1
      elif game.district_winner(district) == min_player.party:
        value -= 1

    return Move(None, value)

  # Returns true when game is complete
  def __is_terminal(self, game):
    return not game.evaluate_game_state()


class Max(Player):
  pass


class Min(Player):
  pass

class Move(object)
  def __init(self, action, value):
    self.action = action
    self.value = value


