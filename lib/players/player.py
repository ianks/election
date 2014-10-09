try:
    from IPython import embed
except:
    pass

import copy
import random

from .. import game_elements


class Player(object):
  def __init__(self, game, party):
    self.party = party
    self.game = game

  # Find the optimal min/max move
  def minimax(self, game_orig, depth, is_max, take_action = None):

    emptyDistrict = game_elements.District([])
    # Will take action after the first call of minimax
    if take_action:
      #print 'District: ', take_action.inspect()
      #print '*******'
      #print "before take action:", game_orig.inspect()
      #print '*******'
      game_orig.add_district(take_action)
      #print "after take action:", game_orig.inspect()
      #print '*******'
    else:
       take_action = emptyDistrict

    # make a copy so we dont screw up the current game state
    game = copy.deepcopy(game_orig)
    # embed()

    # Max Depth of tree reached
    if depth == 0 or self.__is_terminal(game):
      return self.__utility(game, take_action)

    # Player is Max:
    if is_max:
      best_value = Move(emptyDistrict, float("-inf"))
      for action in self.__actions(game):
        value = self.minimax(game, depth-1, False, action)
        best_value = max([value, best_value], key = lambda move: move.value)

      #convert new instance of action to old
      best_value.action = self.__convert_action_to_original_game(game_orig,best_value.action)

      return best_value

    # Player is Min:
    else:
      best_value = Move(emptyDistrict, float("inf"))
      actions = self.__actions(game)

      for action in actions:
        value = self.minimax(game, depth-1, True, action)
        best_value = min([value, best_value], key = lambda move: move.value)
      #convert new instance of action to old
      best_value.action = self.__convert_action_to_original_game(game_orig,best_value.action)

      return best_value

  # Returns a list of actions or moves given the game game
  def __actions(self,game):

    actions_list = []
    # select a random node in the game
    count = 0
    while len(actions_list) < 5:
      if (len(actions_list) != 0 and count >= 100):
       break

      count += 1
      vertex = random.sample(game.board.get_vertices(), 1)[0]

      if vertex.get_block().owned:
        continue

      stack = []
      visited = []
      stack.append(vertex)
      district = game_elements.District([])

      while len(stack) != 0:
        current_vertex = stack.pop()

        if current_vertex not in visited:
            visited.append(current_vertex)
            district.append(current_vertex.get_block())

            if len(district.blocks) == game.district_size:
              break

            for connection in current_vertex.get_connections():
              if (not connection.get_block().owned) and (connection not in visited):
                  stack.append(connection)


      if game.is_legal_move(district):
        #print "True, ", district.inspect(), " is a valid move"
        actions_list.append(district)

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

  def __convert_action_to_original_game(self, original_game,action):
    original_vertices = original_game.board.get_vertices()
    original_blocks_list = []
    for vertex in original_vertices:
      original_blocks_list.append(vertex.get_block())
    original_action = game_elements.District([])

    for block in action.blocks:
      for original_block in original_blocks_list:
        if block.location == original_block.location:
          original_action.append(original_block)

    return original_action

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




