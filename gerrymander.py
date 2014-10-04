#! /usr/bin/env python

import sys, imp

import utility

import lib
from lib import players
from lib import game_elements


try:
    from IPython import embed
except:
    pass


def initialize_neighborhood(file):
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

def main():
    neighborhood = initialize_neighborhood(sys.argv[1])
    game = lib.Game(neighborhood)
    game_players = [players.Max(game, "R"), players.Min(game, "D")]
    ref = lib.Referee(neighborhood, game, game_players)

    print ref.start_game()

if __name__ == "__main__":
    main()
