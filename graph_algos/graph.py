from graph_algos.linked_adts import LinkedQueue, LinkedStack

class Vertex:
    def __init__(self, key):
        self.id = key
        self.distance = float('inf')
        self.previous = None
        self.connections = []

    def add_neighbor(self, neighbor, distance):
        self.connections.append((neighbor, distance))

    def get_connections(self):
        return self.connections
    
    def get_distance(self):
        return self.distance
    
    def get_id(self):
        return self.id
    
    def get_previous(self):
        return self.previous

    def set_distance(self, distance):
        self.distance = distance

    def set_previous(self, previous):
        self.previous = previous

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x[0].get_id() for x in self.connections]) 
    
class UndirectedGraph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def get_vertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        return None
    
    def add_edge(self, from_key, to_key, distance):
        if from_key not in self.vertList:
            self.add_vertex(from_key)
        if to_key not in self.vertList:
            self.add_vertex(to_key)
        self.vertList[from_key].add_neighbor(self.vertList[to_key], distance)
        self.vertList[to_key].add_neighbor(self.vertList[from_key], distance)
   
    def get_vertices(self):
        return self.vertList.keys()
    
    def get_edges(self):
        edgeList=[]
        for v in self.vertList.values():
            for n in v.get_connections():
                edgeList.append((v.get_id(), n[0].get_id(), v.get_distance()))
        return edgeList
    
    def clear(self):
        self.vertList = {}
        self.numVertices = 0

    def is_empty(self):
        return self.numVertices == 0
    
    def size(self):
        return self.numVertices
    
    def breadth_first_search(self, start):
        start.set_distance(0)
        start.set_previous(None)
        vertQueue = LinkedQueue()
        vertQueue.enqueue(start)
        while not vertQueue.is_empty():
            current_vertex = vertQueue.dequeue()
            for neighbor in current_vertex.get_connections():
                if neighbor[0].get_distance() == float('inf'):
                    neighbor[0].set_distance(current_vertex.get_distance() + 1)
                    neighbor[0].set_previous(current_vertex)
                    vertQueue.enqueue(neighbor[0])
        return current_vertex  
    
    def traverse(self, start):
        x = self.breadth_first_search(start)
        while x.get_previous():
            print(x.get_id())
            x = x.get_previous()
        print(x.get_id())

    def depth_first_search(self, start):
        start.set_distance(0)
        start.set_previous(None)
        vertStack = LinkedStack()
        vertStack.push(start)
        while not vertStack.is_empty():
            current_vertex = vertStack.pop()
            for neighbor in current_vertex.get_connections():
                if neighbor[0].get_distance() == float('inf'):
                    neighbor[0].set_distance(current_vertex.get_distance() + 1)
                    neighbor[0].set_previous(current_vertex)
                    vertStack.push(neighbor[0])
        return current_vertex

                    
    
class DirectedGraph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def get_vertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        return None
    
    def add_edge(self, from_key, to_key, distance):
        if from_key not in self.vertList:
            self.add_vertex(from_key)
        if to_key not in self.vertList:
            self.add_vertex(to_key)
        self.vertList[from_key].add_neighbor(self.vertList[to_key], distance)

    def get_vertices(self):
        return self.vertList.keys()
    
    def get_edges(self):
        edgeList=[]
        for v in self.vertList.values():
            for n, w in v.get_connections():
                edgeList.append((v.get_id(), n.get_id(), w)) 
        return edgeList
    
    def clear(self):
        self.vertList = {}
        self.numVertices = 0
        
    def is_empty(self):
        return self.numVertices == 0
    
    def size(self):
        return self.numVertices
    
    def breadth_first_search(self, start):
        start.set_distance(0)
        start.set_previous(None)
        vertQueue = LinkedQueue()
        vertQueue.enqueue(start)
        while not vertQueue.is_empty():
            current_vertex = vertQueue.dequeue()
            for neighbor in current_vertex.get_connections():
                if neighbor.get_distance() == float('inf'):
                    neighbor.set_distance(current_vertex.get_distance() + 1)
                    neighbor.set_previous(current_vertex)
                    vertQueue.enqueue(neighbor) 
        return current_vertex
    
    def traverse(self, start):
        x = self.breadth_first_search(start)
        while x.get_previous():
            print(x.get_id())
            x = x.get_previous()    
        print(x.get_id())

    def depth_first_search(self, start):
        start.set_distance(0)
        start.set_previous(None)
        vertStack = LinkedStack()
        vertStack.push(start)
        while not vertStack.is_empty():
            current_vertex = vertStack.pop()
            for neighbor in current_vertex.get_connections():
                if neighbor.get_distance() == float('inf'):
                    neighbor.set_distance(current_vertex.get_distance() + 1)
                    neighbor.set_previous(current_vertex)
                    vertStack.push(neighbor)
        return current_vertex
    