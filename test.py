import unittest
import utility
import lib
from lib import players
from lib import game_elements

from IPython import embed


class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        self.n= self.initialize_neighborhood('smallNeighborhood.txt')
        self.game = lib.Game(self.n)
        self.players = [players.Max(self.game, "R"), players.Min(self.game, "D")]
        self.ref = lib.Referee(self.n, self.game, self.players)

        # Row 1
        b1 = self.game.neighborhood.block_at_location(0,0)
        b2 = self.game.neighborhood.block_at_location(0,1)
        b3 = self.game.neighborhood.block_at_location(0,2)
        b4 = self.game.neighborhood.block_at_location(0,3)
        # Row 2
        b5 = self.game.neighborhood.block_at_location(1,0)
        b6 = self.game.neighborhood.block_at_location(1,1)
        b7 = self.game.neighborhood.block_at_location(1,2)
        b8 = self.game.neighborhood.block_at_location(1,3)
        # Row 3
        b9 = self.game.neighborhood.block_at_location(2,0)
        b10 = self.game.neighborhood.block_at_location(2,1)
        b11 = self.game.neighborhood.block_at_location(2,2)
        b12 = self.game.neighborhood.block_at_location(2,3)
        # Row 4
        b13 = self.game.neighborhood.block_at_location(3,0)
        b14 = self.game.neighborhood.block_at_location(3,1)
        b15 = self.game.neighborhood.block_at_location(3,2)
        b16 = self.game.neighborhood.block_at_location(3,3)

        # valid districts
        self.valid_district_1 = game_elements.district.District([b1,b2,b3,b4])
        self.valid_district_2 = game_elements.district.District([b1,b5,b6,b9])
        self.valid_district_3 = game_elements.district.District([b7,b8,b6,b12])
        self.valid_district_4 = game_elements.district.District([b9,b10,b13,b14])
        self.valid_district_5 = game_elements.district.District([b10,b11,b12,b7])
        self.valid_district_6 = game_elements.district.District([b1,b2,b3,b4])
        self.valid_district_7 = game_elements.district.District([b5,b6,b7,b8])
        self.valid_district_8 = game_elements.district.District([b9,b10,b11,b12])
        self.valid_district_9 = game_elements.district.District([b13,b14,b15,b16])


        # inValid District (not connected)
        self.invalid_district_1 = game_elements.district.District([b2,b3,b4,b16])

        # inValid District (leaves a hole)
        self.invalid_district_2  = game_elements.district.District([b2,b3,b7,b8])
        self.invalid_district_3  = game_elements.district.District([b2,b6,b7,b8])

        # inValid District (too small)
        self.invalid_district_4 = game_elements.district.District([b1,b2,b3])

        # inValid District (too big)
        self.invalid_district_5 = game_elements.district.District([b1,b2,b3,b4,b5])

    def initialize_neighborhood(self, file):
        matrix = []
        file = open(file).read()

        for i, line in enumerate(file.splitlines()):
            row = []
            line = line.replace(' ', '')

            for j, element in enumerate(line):
                attrs = { 'party': element, 'location': (i ,j), 'owned': False }
                blk = game_elements.Block(attrs)
                row.append(blk)

            matrix.append(row)

        return game_elements.Neighborhood({ 'matrix': matrix })

    def test_is_legal_move(self):
        # Valid Districts
        self.assertTrue(self.game.is_legal_move(self.valid_district_1))
        self.assertTrue(self.game.is_legal_move(self.valid_district_2))
        self.assertTrue(self.game.is_legal_move(self.valid_district_3))
        self.assertTrue(self.game.is_legal_move(self.valid_district_4))
        self.assertTrue(self.game.is_legal_move(self.valid_district_5))


    def test_is_illegal_districts(self):
        # Illegal Districts
        self.assertFalse(self.game.is_legal_move(self.invalid_district_1))
        self.assertFalse(self.game.is_legal_move(self.invalid_district_2))
        self.assertFalse(self.game.is_legal_move(self.invalid_district_3))
        self.assertFalse(self.game.is_legal_move(self.invalid_district_4))
        self.assertFalse(self.game.is_legal_move(self.invalid_district_5))

    def test_is_illegal_district_combinations(self):
        # Test Combinations of districts
        self.game.add_district(self.valid_district_1)
        # Cannot add to already owned
        self.assertFalse(self.game.add_district(self.valid_district_2))
        # Cannot leave a hole (at b8)
        self.assertFalse(self.game.add_district(self.valid_district_5))

    def test_game_will_finish_with_valid_moves(self):
        # fill game board
        self.assertTrue(self.game.add_district(self.valid_district_6))
        self.assertTrue(self.game.add_district(self.valid_district_7))
        self.assertTrue(self.game.add_district(self.valid_district_8))
        self.assertTrue(self.game.add_district(self.valid_district_9))
        # should end game
        self.assertTrue(self.game.evaluate_game_state())

if __name__ == '__main__':
    unittest.main()
