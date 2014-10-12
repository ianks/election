import copy
import random
import logging
import subprocess
from .. import game_elements

logging.basicConfig(filename='log/development.log', filemode='w', level=logging.DEBUG)

class Player(object):
  def __init__(self, game, party):
    self.party = party
    self.game = game
    self.max_player_party = "R"
    self.min_player_party = "D"

  # Find the optimal min/max move
  def minimax(self, game_orig, depth, is_max, take_action = None):

    empty_district = game_elements.District([])

    # Will take action after the first call of minimax
    if take_action:
      logging.info('District: '+ str(take_action.inspect()))
      logging.info('*******')
      logging.info("before take action:" + str(game_orig.inspect()))
      logging.info('*******')

      game_orig.add_district(take_action)

      logging.info("after take action:" + str(game_orig.inspect()))
    else:
       take_action = empty_district

    # Make a copy so we dont screw up the current game state
    game = copy.deepcopy(game_orig)

    # Max Depth of tree reached
    if depth == 0 or self.__is_terminal(game):
      return self.__utility(game, take_action)

    # Player is Max:
    if is_max:
      best_value = Move(empty_district, float("-inf"))
      for action in self.__actions(game):
        value = self.minimax(game, depth-1, False, action)
        best_value = max([value, best_value], key = lambda move: move.value)

      best_value.action = self.convert_action_to_original_game(game_orig, best_value.action)
      return best_value

    # Player is Min:
    else:
      best_value = Move(empty_district, float("inf"))
      actions = self.__actions(game)

      for action in actions:
        value = self.minimax(game, depth-1, True, action)
        best_value = min([value, best_value], key = lambda move: move.value)

      best_value.action = self.convert_action_to_original_game(game_orig, best_value.action)
      return best_value

  # Returns a list of actions or moves given the game game
  def __actions(self,game):

    actions_list = []
    # select a random node in the game
    count = 0
    # Select 9 actions
    while len(actions_list) < 10:
      if (len(actions_list) != 0 and count >= 100):
        break

      if count > 10000:
        subprocess.call(["python", "gerrymander.py", "largeNeighborhood.txt"])
        exit()

      count += 1
      vertex = random.choice(game.board.get_vertices())

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

            random_stack = []
            for connection in current_vertex.get_connections():
              if (not connection.get_block().owned) and (connection not in visited):
                  random_stack.append(connection)
              if len(random_stack) > 0:
                random.shuffle(random_stack)
                for item in random_stack:
                  stack.append(item)

      # Make sure move is legal before adding it to actions list
      if game.is_legal_move(district):
        actions_list.append(district)

    return actions_list

  # Returns true when game is complete
  def __is_terminal(self, game):
    return game.evaluate_game_state()

  # Since we used a deep copy each time, we need to reference the
  # original game by using block location instead of reference
  def convert_action_to_original_game(self, original_game, action):
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

  # Returns the utility of an end game (who is winning at that point)
  def __utility(self, game, action):
    value = 0

    # Here, we gauge the utility of the move using heuristics
    for district in game.districts:
      value += self._winner_value(game, district)
      value += self._party_ratio_value(game, district)

    return Move(action, value)

  def _winner_value(self, game, district):
    # Assign a value of the move based on the winner of the district
    # Positive value for max player, negative value for min player
    if game.district_winner(district) == self.max_player_party:
        return game.district_size / 2

    elif game.district_winner(district) == self.min_player_party:
        return -1 * game.district_size / 2

    else:
        return 0  # Tie

  def _party_ratio_value(self, game, district):
    parties = [block.party for block in district.blocks]

    # Return a higher value if your move ends up using more of
    # your opponent's blocks.
    if parties.count(self.max_player_party) > game.district_size / 2:
      return parties.count(self.min_player_party)

    elif parties.count(self.min_player_party) > game.district_size / 2:
      return -1 * parties.count(self.max_player_party)

    else:
      return 0


class Max(Player):
  def get_move(self):
    # game = self.game, depth = 3, is_max = True
    move = self.minimax(self.game, 3, True)
    return move.action


class Min(Player):
  def get_move(self):
    # Give max advantage by making depth shorter for min
    # game = self.game, depth = 1, is_max = False
    move = self.minimax(self.game, 1, False)
    return move.action

# Move object which holds the action we take, and the value of said action.
class Move(object):
  def __init__(self, action, value):
    self.action = action
    self.value = value
