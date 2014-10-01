class Neighborhood(object):
    def __init__(self, file):
        self.file = file
        self.matrix = self._initialize_matrix(file)

    def as_matrix(self):
        return self.matrix

    def _initialize_matrix(self, file):
        arr = []

        for line in open(file).read().splitlines():
            arr.append(line.split())

        return arr
