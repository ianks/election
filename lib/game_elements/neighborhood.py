class Neighborhood(object):
    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])

    def as_matrix(self):
        return self.matrix

    def block_at_location(self, i, j):
        return self.matrix[i][j]

    def inspect(self):
        matrix = []

        for i, row in enumerate(self.matrix):
            _row = []

            for j, col in enumerate(row):
                blk_prty = self.block_at_location(i,j).party
                _row.append(blk_prty)

            matrix.append(_row)

        return matrix
