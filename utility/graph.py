# Modified from source: http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html

class Vertex:
    def __init__(self,key):
        self.block = key
        self.connectedTo = {}

    def add_neighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.block) + ' connectedTo: ' + str([x.block for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_block(self):
        return self.block

    def get_weight(self,nbr):
        return self.connectedTo[nbr]


#
# Graph Stores Vertices in dictionary by location index
# Vertex must be a block for this to work
#

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, value):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(value)
        key = value.location
        self.vertList[key] = newVertex
        return newVertex

    def get_vertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def get_vertex_at_location(self,i,j):
        if (i,j) in self.vertList:
            return self.vertList[(i,j)]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def add_edge(self,f,t,cost=0):
        fLoc = f.location
        tLoc = t.location
        if fLoc not in self.vertList:
            self.add_vertex(f)
        if tLoc not in self.vertList:
            self.add_vertex(t)

        self.vertList[fLoc].add_neighbor(self.vertList[tLoc], cost)
        self.vertList[tLoc].add_neighbor(self.vertList[fLoc], cost)

    def get_vertices(self):
        return self.vertList.values()

    def __iter__(self):
        return iter(self.vertList.values())
