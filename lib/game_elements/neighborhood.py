import utility

class Neighborhood(object):
    # initialize with { party, location, owned}
    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])

    # Returns the matrix itself
    def as_matrix(self):
        return self.matrix

    # Returns block at a given location
    def block_at_location(self, i, j):
        return self.matrix[i][j]

    def vertex_at_location(self, i,j):
        return self.vertex_matrix[i][j]


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

    def initialize_vertices(self):
        matrix = []

        for i, row in enumerate(self.matrix):
            _row = []

            for j, col in enumerate(row):
                blk = self.block_at_location(i,j)
                _row.append(utility.Vertex(blk))

            matrix.append(_row)

        self.vertex_matrix = matrix
        return True

    def initialize_graph(self):
        self.initialize_vertices()
        graph = utility.Graph()

        for i, row in enumerate(self.vertex_matrix):
            prev_element = False

            for j, element in enumerate(row):
                if prev_element:
                    graph.addEdge(element, prev_element)
                    prev_element = element

                else:
                    prev_element = element

                if i != 0:

                    graph.addEdge(self.vertex_at_location(i-1, j), self.vertex_at_location(i, j))

        self.graph = graph
        return self.graph


