#! /usr/bin/env python

import sys, imp

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
    n = initialize_neighborhood(sys.argv[1])
    print n.inspect()

if __name__ == "__main__":
    main()
