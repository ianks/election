try:
    from IPython import embed
except:
    pass

class Game(object):
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood
        self.board = neighborhood.initialize_graph()
        self.district_size = len(neighborhood.matrix)
        self.districts = []

    def is_legal_move(self, district):
        available = self.__is_district_available(district)
        contiguous = self.__is_district_contiguous(district)
        valid_size = self.__is_district_valid_size(district)
        valid_placement = self.__is_district_valid_placement(district)
        if available and contiguous and valid_size and valid_placement:
            return True
        else:
            return False

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

    def __is_district_valid_placement(self, district):
        explored_area = []
        for vertex in self.board.get_vertices():

            #if vertex in an explored Area:
            if vertex in explored_area:
                continue

            block = vertex.get_block()
            if block.owned or (block in district.locations):
                continue

            # RUN search on not owned blocks
            stack = []
            visited = []
            stack.append( vertex )

            while len(stack) != 0:
                current_vertex = stack.pop()
                if current_vertex not in visited:
                    visited.append(current_vertex)
                    explored_area.append(current_vertex)
                    for v in current_vertex.get_connections():
                        v_block = v.get_block()
                        if v_block not in district.locations:
                            if (not v_block.owned) and (v not in visited):
                                stack.append(v)
            # check for area that we cannot split into districts
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
        stack.append( game_block )
        while len(stack) != 0:
            current_vertex = stack.pop()
            visited.append(current_vertex)
            if len(visited) == len(district.blocks):
                return True
            for vertex in current_vertex.get_connections():
                if vertex.get_block().location in district.locations:
                    if vertex not in visited:
                        stack.append(vertex)
        return False

    def __is_district_valid_size(self, district):
        if self.district_size == len(district.blocks):
            return True
        return False

    def __is_finished(self):
        return len(self.districts) == self.district_size
