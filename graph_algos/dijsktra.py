from graph_algos.linked_adts import LinkedQueue
from graph_algos.graph import UndirectedGraph

def dijkstra(graph, start):
    # Initialize distances and previous vertices
    for vertex_key in graph.get_vertices():
        vertex = graph.get_vertex(vertex_key)
        vertex.set_distance(float('inf'))
        vertex.set_previous(None)
    
    # Set start vertex distance to 0
    start_vertex = graph.get_vertex(start)
    start_vertex.set_distance(0)
    
    # Create a set of unvisited vertices
    unvisited = set(graph.get_vertices())
    
    while unvisited:
        # Find the unvisited vertex with the smallest distance
        current_key = min(unvisited, key=lambda x: graph.get_vertex(x).distance)
        current_vertex = graph.get_vertex(current_key)
        unvisited.remove(current_key)
        
        # Check all neighbors
        for neighbor, weight in current_vertex.get_connections():
            neighbor_key = neighbor.get_id()
            if neighbor_key in unvisited:
                # Calculate new distance
                new_distance = current_vertex.distance + weight
                
                # If we found a shorter path, relax the edge
                if new_distance < neighbor.distance:
                    print(f"Relaxing edge: {current_key} -> {neighbor_key} (weight: {weight})")
                    neighbor.set_distance(new_distance)
                    neighbor.set_previous(current_vertex)
    
    return graph

def get_shortest_path(graph, end):
    path = []
    current_vertex = graph.get_vertex(end)
    while current_vertex is not None:
        path.append(current_vertex.get_id())
        current_vertex = current_vertex.get_previous()
    path.reverse()
    return path

def get_shortest_distance(graph, end):
    return graph.get_vertex(end).distance
