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
        b1 = game.neighborhood.block_at_location(0,1)
        b2 = game.neighborhood.block_at_location(0,2)
        b3 = game.neighborhood.block_at_location(0,3)
        b4 = game.neighborhood.block_at_location(1,3)
        district = game_elements.district.District([b1,b2,b3,b4])

        self.assertTrue(game.is_legal_move(district))

    def test_is_legal_move(self):
        n = self.initialize_neighborhood('smallNeighborhood.txt')
        ref = lib.Referee(n)
        game = ref.game
        b1 = game.neighborhood.block_at_location(1,0)
        b2 = game.neighborhood.block_at_location(1,1)
        b3 = game.neighborhood.block_at_location(0,1)
        b4 = game.neighborhood.block_at_location(0,2)
        district = game_elements.district.District([b1,b2,b3,b4])

        self.assertFalse(game.is_legal_move(district))

if __name__ == '__main__':
    unittest.main()
