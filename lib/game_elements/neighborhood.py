import utility

class Neighborhood(object):
    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])

        self.graph = self.initialize_graph()

    # Returns the matrix itself
    def as_matrix(self):
        return self.matrix

    # Returns block at a given location
    def block_at_location(self, i, j):
        return self.matrix[i][j]

    # Returns an array of parties from the matrix
    def inspect(self):
        matrix = []

        for i, row in enumerate(self.matrix):
            _row = []

            for j, col in enumerate(row):
                blk_prty = self.block_at_location(i,j).party
                _row.append(blk_prty)

            matrix.append(_row)

        return matrix

    def initialize_graph(self):
        graph = utility.Graph()

        for i, row in enumerate(self.matrix):
            prev_element = False

            for j, element in enumerate(row):
                if prev_element:
                    graph.add_edge(element, prev_element)
                    prev_element = element

                else:
                    prev_element = element

                if i != 0:
                    graph.add_edge(self.block_at_location(i-1, j), self.block_at_location(i, j), 1)

        self.graph = graph
        return self.graph
