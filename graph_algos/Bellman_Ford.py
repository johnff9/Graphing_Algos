from graph_algos.graph import DirectedGraph

def bellman_ford(graph, start):
    # Initialize distances and previous vertices
    for vertex_key in graph.get_vertices():
        vertex = graph.get_vertex(vertex_key)
        vertex.set_distance(float('inf'))
        vertex.set_previous(None)
    
    # Set start vertex distance to 0
    start_vertex = graph.get_vertex(start)
    start_vertex.set_distance(0)

    # Relax edges |V| - 1 times
    for i in range(graph.size() - 1):
        for edge in graph.get_edges():
            u = graph.get_vertex(edge[0])
            v = graph.get_vertex(edge[1])   
            weight = edge[2]
            if u.get_distance() + weight < v.get_distance():
                print(f"Relaxing edge: {edge[0]} -> {edge[1]} (weight: {weight})")
                v.set_distance(u.get_distance() + weight)
                v.set_previous(u)

    # Check for negative weight cycles
    for edge in graph.get_edges():
        u = graph.get_vertex(edge[0])
        v = graph.get_vertex(edge[1])
        weight = edge[2]
        if u.get_distance() + weight < v.get_distance():
            print("Negative weight cycle detected!")
            return False
    return True

def get_shortest_path(graph, end):
    path = []
    current_vertex = graph.get_vertex(end)
    while current_vertex is not None:
        path.append(current_vertex.get_id())
        current_vertex = current_vertex.get_previous()
    path.reverse()
    return path

def get_shortest_distance(graph, end):
    return graph.get_vertex(end).get_distance()

def main():
    g = DirectedGraph()
    g.add_vertex('S')
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')

    g.add_edge('S', 'B', 2)
    g.add_edge('S', 'A', 1)
    g.add_edge('A', 'C', 1)
    g.add_edge('A', 'E', 5)
    g.add_edge('B', 'D', 7)
    g.add_edge('B', 'C', 3)
    g.add_edge('C', 'F', 1)
    g.add_edge('D', 'C', 9)
    g.add_edge('D', 'F', 8)
    g.add_edge('E', 'C', -2)
    g.add_edge('E', 'F', -2)

    # Run Bellman-Ford algorithm
    has_shortest_path = bellman_ford(g, 'S')
    
    if has_shortest_path:
        print("\nShortest path to F:", get_shortest_path(g, 'F'))
        print("Shortest distance to F:", get_shortest_distance(g, 'F'))
        
        # Print all vertex distances for debugging
        print("\nAll vertex distances:")
        for vertex_key in g.get_vertices():
            vertex = g.get_vertex(vertex_key)
            prev_id = vertex.get_previous().get_id() if vertex.get_previous() else None
            print(f"Vertex {vertex_key}: distance = {vertex.get_distance()}, previous = {prev_id}")
    else:
        print("No shortest path exists due to negative weight cycle")

if __name__ == "__main__":
    main() 
    
