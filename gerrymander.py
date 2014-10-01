#! /usr/bin/env python

try:
    from IPython import embed
except:
    True

import sys, imp

neighborhood = imp.load_source('Neighborhood', 'lib/game_elements/neighborhood.py')
district     = imp.load_source('District', 'lib/game_elements/district.py')
block        = imp.load_source('Block', 'lib/game_elements/block.py')
players      = imp.load_source('District', 'lib/players/players.py')


def main():
    try:
        n = neighborhood.Neighborhood(sys.argv[1]).as_matrix()
        print n
    except:
        print "File import failed."
        exit()

if __name__ == "__main__":
    main()
