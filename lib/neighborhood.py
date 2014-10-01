import numpy as np

class Neighborhood():
    def __init__(self, file):
        self.file = file
        self.matrix = self.__initialize_matrix(file)

    def as_matrix(self):
        return self.matrix

    def __initialize_matrix(self, file):
        arr = []

        for line in open(file).read().splitlines():
            arr.append(line.split())

        return np.matrix(arr)
