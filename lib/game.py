class Game(object):
    def __init__(self, neighborhood):
        self.neighborhood = neighborhood
        self.board = neighborhood.initialize_graph()
        self.game_state = initialize_game_state(self)
        self.district_size = size(neighborhood.matrix)
        self.districts = []

    def is_legal_move(self, district):
        a = self.__is_district_available(district)
        c = self.__is_district_coniguous(district)
        vs = self.__is_district_valid_size(district)
        vp = self.__is_district_valid_placement(district)
        if a && c && vs && vp:
            return True
        else:
            return False

    def add_district(self, district):
        self.districts.append(district)
        for block in district:
            game_block = board.get_vertex(block.location)
            game_block.owned = True

    def evaluate_game_state(self):
        return

    def __is_district_valid_placement(self, district):
        explored_area = []
        for vertex in self.board.get_vertices()
            #if vertex in an explored Area:
            if vertex in explored_area:
                continue
            block = vertex.get_block()
            if not vertex.owned && block.location not in district.locations:
                # RUN search on not owned blocks
                stack = []
                visited = []
                stack.push( vertex )
                while not stack.isEmpty():
                    current_vertex = stack.pop()
                    visited.append(current_vertex)
                    for v in current_vertex.get_connections():
                        v_block = v.get_block()
                        if not v_block.owned and v not in visited:
                            stack.push(v)
                # check for area that we cannot split into districts
                if not size(visited) % self.district_size:
                    return False
        return True

    def __is_district_available(self, district):
        for block in district.blocks:
            game_block = board.get_vertex(block.location)
            if game_block.owned:
                return False
        return True


    def __is_district_contiguous(self, district):
        block = district.blocks[0]
        game_block = board.get_vertex(block.location)
        stack = []
        visited = []
        stack.push( game_block )
        while not stack.isEmpty():
            current_vertex = stack.pop()
            visited.append(current_vertex)
            if size(visited) == size(district.blocks):
                return True
            for vertex in current_vertex.get_connections():
                if vertex.get_block().location in district.blocks
                    if vertex not in visited:
                        stack.push(vertex)
        return False

    def __is_district_valid_size(self, district):
        if district_size == size(district.blocks):
            return True
        return False

    def __is_finished(self):
        return size(self.districts) == self.district_size
