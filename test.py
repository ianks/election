import unittest
import utility
import lib
from lib import players
from lib import game_elements

from IPython import embed


class TestGameFunctions(unittest.TestCase):

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
        n = self.initialize_neighborhood('smallNeighborhood.txt')
        ref = lib.Referee(n)
        game = ref.game
        b1 = game.neighborhood.block_at_location(0,0)
        b2 = game.neighborhood.block_at_location(0,1)
        b3 = game.neighborhood.block_at_location(0,2)
        b4 = game.neighborhood.block_at_location(0,3)

        b5 = game.neighborhood.block_at_location(1,0)
        b6 = game.neighborhood.block_at_location(1,1)
        b7 = game.neighborhood.block_at_location(1,2)
        b8 = game.neighborhood.block_at_location(1,3)

        b9 = game.neighborhood.block_at_location(2,0)
        b10 = game.neighborhood.block_at_location(2,1)
        b11 = game.neighborhood.block_at_location(2,2)
        b12 = game.neighborhood.block_at_location(2,3)

        b13 = game.neighborhood.block_at_location(3,0)
        b14 = game.neighborhood.block_at_location(3,1)
        b15 = game.neighborhood.block_at_location(3,2)
        b16 = game.neighborhood.block_at_location(3,3)

        valid_district_1 = game_elements.district.District([b1,b2,b3,b4])
        valid_district_2 = game_elements.district.District([b1,b5,b6,b9])
        valid_district_3 = game_elements.district.District([b7,b8,b6,b12])
        valid_district_4 = game_elements.district.District([b9,b10,b13,b14])
        valid_district_5 = game_elements.district.District([b10,b11,b12,b7])

        self.assertTrue(game.is_legal_move(valid_district_1))
        self.assertTrue(game.is_legal_move(valid_district_2))
        self.assertTrue(game.is_legal_move(valid_district_3))
        self.assertTrue(game.is_legal_move(valid_district_4))
        self.assertTrue(game.is_legal_move(valid_district_5))


    def test_is_illegal_move(self):
        n = self.initialize_neighborhood('smallNeighborhood.txt')
        ref = lib.Referee(n)
        game = ref.game
        b1 = game.neighborhood.block_at_location(0,0)
        b2 = game.neighborhood.block_at_location(0,1)
        b3 = game.neighborhood.block_at_location(0,2)
        b4 = game.neighborhood.block_at_location(0,3)

        b5 = game.neighborhood.block_at_location(1,0)
        b6 = game.neighborhood.block_at_location(1,1)
        b7 = game.neighborhood.block_at_location(1,2)
        b8 = game.neighborhood.block_at_location(1,3)

        b9 = game.neighborhood.block_at_location(2,0)
        b10 = game.neighborhood.block_at_location(2,1)
        b11 = game.neighborhood.block_at_location(2,2)
        b12 = game.neighborhood.block_at_location(2,3)

        b13 = game.neighborhood.block_at_location(3,0)
        b14 = game.neighborhood.block_at_location(3,1)
        b15 = game.neighborhood.block_at_location(3,2)
        b16 = game.neighborhood.block_at_location(3,3)

        # valid districts
        valid_district_1 = game_elements.district.District([b1,b2,b3,b4])
        valid_district_2 = game_elements.district.District([b1,b5,b6,b9])
        valid_district_3 = game_elements.district.District([b7,b8,b6,b12])
        valid_district_4 = game_elements.district.District([b9,b10,b13,b14])
        valid_district_5 = game_elements.district.District([b10,b11,b12,b7])

        # inValid District (not connected)
        invalid_district_1 = game_elements.district.District([b2,b3,b4,b16])

        # inValid District (leaves a hole)
        invalid_district_2  = game_elements.district.District([b2,b3,b7,b8])
        invalid_district_3  = game_elements.district.District([b2,b6,b7,b8])

        # inValid District (too small)
        invalid_district_4 = game_elements.district.District([b1,b2,b3])

        # inValid District (too big)
        invalid_district_5 = game_elements.district.District([b1,b2,b3,b4,b5])

        self.assertFalse(game.is_legal_move(invalid_district_1))
        self.assertFalse(game.is_legal_move(invalid_district_2))
        self.assertFalse(game.is_legal_move(invalid_district_3))
        self.assertFalse(game.is_legal_move(invalid_district_4))
        self.assertFalse(game.is_legal_move(invalid_district_5))

        # Test Combinations of districts
        game.add_district(valid_district_1)
        # cannot add to already owned
        self.assertFalse(game.add_district(valid_district_2))
        # cannot leave a hole (at b8)
        self.assertFalse(game.add_district(valid_district_5))

if __name__ == '__main__':
    unittest.main()
