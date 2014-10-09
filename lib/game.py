try:
    from IPython import embed
except:
    pass

class Game(object):
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood
        self.board = self.neighborhood.graph
        self.district_size = len(self.neighborhood.matrix)
        self.districts = []

    def is_legal_move(self, district):
        valid_size = self.__is_district_valid_size(district)
        available = self.__is_district_available(district)
        contiguous = self.__is_district_contiguous(district)
        valid_placement = self.__is_district_valid_placement(district)

        return valid_size and available and contiguous and valid_placement

    def add_district(self, district):
        if self.is_legal_move(district):
            self.districts.append(district)

            for block in district.blocks:
                vertex = self.board.get_vertex(block)
                block = vertex.get_block()
                block.owned = True
            return True

        return False

    def evaluate_game_state(self):
        return self.__is_finished()

    def inspect(self):
        arr = []

        for district in self.districts:
            arr.append(district.inspect())

        return arr

    def inspect_blocks(self):
        arr = []
        for vert in self.board.get_vertices():
            arr.append((vert.get_block().location, vert.get_block().owned))
        return arr

    def inspect_available_moves(self):
        arr = []
        for vert in self.board.get_vertices():
            block = vert.get_block()
            if not block.owned:
                arr.append(vert.get_block().location)
        return arr

    def inspect_taken_moves(self):
        arr = []
        for vert in self.board.get_vertices():
            block = vert.get_block()
            if block.owned:
                arr.append(vert.get_block().location)
        return arr

    def district_winner(self, district):
        parties = [block.party for block in district.blocks]

        if parties.count("R") > parties.count("D"):
            return "R"
        elif parties.count("R") < parties.count("D"):
            return "D"
        else:
            return None

    def __is_district_valid_placement(self, district):
        explored_area = []

        for vertex in self.board.get_vertices():
            if vertex in explored_area:
                continue

            # Run search on not owned blocks
            block = vertex.get_block()
            if block.owned or block in district.blocks:
                continue

            stack = []
            visited = []
            stack.append(vertex)

            while len(stack) != 0:
                current_vertex = stack.pop()

                if current_vertex not in visited:
                    visited.append(current_vertex)
                    explored_area.append(current_vertex)

                    for connection in current_vertex.get_connections():
                        if connection.get_block() not in district.blocks:
                            if not connection.get_block().owned and connection not in visited:
                                stack.append(connection)

            # Check for area that we cannot split into districts
            if len(visited) % self.district_size != 0:
                return False

        return True

    def __is_district_available(self, district):
        for block in district.blocks:
            vertex = self.board.get_vertex(block)
            game_block = vertex.get_block()
            if game_block.owned:
                return False

        return True

    def __is_district_contiguous(self, district):
        block = district.blocks[0]
        game_block = self.board.get_vertex(block)
        stack = []
        visited = []
        stack.append(game_block)

        while len(stack) != 0:
            current_vertex = stack.pop()

            if current_vertex not in visited:
                visited.append(current_vertex)

                for connection in current_vertex.get_connections():
                    if connection.get_block() in district.blocks:
                        if connection not in visited:
                            stack.append(connection)

        return len(visited) == len(district.blocks)

    def __is_district_valid_size(self, district):
        return self.district_size == len(district.blocks)

    def __is_finished(self):
        return len(self.districts) == self.district_size
