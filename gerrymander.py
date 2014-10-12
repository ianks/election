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

# Names: Ian Ker-Seymer and Brandon Mikulka
# Purpose: Create min-max gerrymander game
# Run program using "python gerrymander.py <GameBoard>" where Gameboard
#    is either smallNeighborhood.txt or largeNeighborhood.txt
# Implementation of Minimax function in lib/players/player.py
# Data structures (matrix/graph) stored in lib/game_elements/neighborhood.py
# Games state stored in lib/game.py
# Game controlled by referee.py
# Modified third party resources are located in utility/ (graph implimentation)

# EXTRA CREDIT OPPURTUNITIES:
# - Our board accepts all types of moves, not simply the
#   standard rows, columns, and sqaures
# - Also works on any sized square board, not just 4x4

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
    ref.start_game()

if __name__ == "__main__":
    main()
