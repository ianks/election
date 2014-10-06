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

  # Find the optimal min/max move
  def minimax(self, game_orig, depth, is_max, take_action = False):

    # Will take action after the first call of minimax
    if take_action:
      game_orig.add_district(take_action)

    # make a copy so we dont screw up the current game state
    game = copy.deepcopy(game_orig)

    # Max Depth of tree reached
    if depth == 0 or self.__is_terminal(game):
      return self.__utility(game, take_action)

    # Player is Max:
    if is_max:
      best_value = Move(False, float("-inf"))
      for action in self.__actions(game):
        value = self.minimax(game, depth-1, False, action)
        best_value = max([value, best_value], key = lambda move: move.value)

      return best_value

    # Player is Min:
    else:
      best_value = Move(False, float("-inf"))
      for action in self.__actions(game):
        value = self.minimax(game, depth-1, True, action)
        best_value = min([value, best_value], key = lambda move: move.value)
      return best_value

  # Returns a list of actions or moves given the game game
  def __actions(self,game):
    neighborhood = game.neighborhood

    actions_list = []
    for district in neighborhood.as_matrix():
      action = game_elements.District([])
      for block in district:
        action.append(block)
      if game.is_legal_move(action):
        actions_list.append(action)

    return actions_list

  # Returns the utility of an end game (who is winning at that point)
  def __utility(self, game, action):
    # needs to return a move object

    # TODO: Fix so it is not hard coded
    max_player_party = "R"
    min_player_party = "D"

    value = 0
    for district in game.districts:
      if game.district_winner(district) == max_player_party:
        value += 1
      elif game.district_winner(district) == min_player_party:
        value -= 1

    return Move(action, value)

  # Returns true when game is complete
  def __is_terminal(self, game):
    return game.evaluate_game_state()


class Max(Player):
  def get_move(self):
    move = self.minimax(self.game, 3, True)
    # return a district (action)
    return move.action


class Min(Player):
  def get_move(self):
    move = self.minimax(self.game, 3, False)
    # return a district (action)
    return move.action

class Move(object):
  def __init__(self, action, value):
    self.action = action
    self.value = value

def convert_copy_action_to_original_action(self,game_copy,original_game,action):


