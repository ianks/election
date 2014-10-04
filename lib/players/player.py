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


class Max(Player):
  pass


class Min(Player):
  pass
