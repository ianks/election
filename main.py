#! /usr/bin/env python

from IPython import embed
import numpy as np
import sys, imp

neighborhood = imp.load_source('Neighborhood', 'lib/neighborhood.py')

def main():
    try:
        n = neighborhood.Neighborhood(sys.argv[1]).as_matrix()
        print n
    except:
        print "File import failed."
        exit()

if __name__ == "__main__":
    main()
