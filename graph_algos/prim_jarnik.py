from graph_algos.graph import UndirectedGraph
from graph_algos.linked_adts import LinkedPriorityQueue

def print_priority_queue(pq):
    print("\nPriority Queue State:")
    print("Vertex | Distance | Path")
    print("-" * 40)
    # Create a copy of the queue to print without modifying it
    queue_copy = pq.queue.copy()
    # Sort by priority (distance) for display
    queue_copy.sort(key=lambda x: x[1])
    for vertex, distance in queue_copy:
        path = []
        current = vertex
        while current is not None:
            path.append(current.get_id())
            current = current.get_previous()
        path.reverse()
        path_str = " -> ".join(path) if path else "Start"
        print(f"{vertex.get_id():<6} | {distance:<8} | {path_str}")

def prim_jarnik(graph, start):
    # Initialize distances and previous vertices
    for vertex_key in graph.get_vertices():
        vertex = graph.get_vertex(vertex_key)
        vertex.set_distance(float('inf'))
        vertex.set_previous(None)
    
    start_vertex = graph.get_vertex(start)
    start_vertex.set_distance(0)

    pq = LinkedPriorityQueue()
    pq.enqueue(start_vertex, 0)  # Start vertex has priority 0
    print("\nInitial Priority Queue:")
    print_priority_queue(pq)

    # Keep track of processed vertices
    processed = set()

    while not pq.is_empty():
        current_vertex, _ = pq.dequeue()  # Unpack the vertex and its priority
        
        # Skip if we've already processed this vertex
        if current_vertex.get_id() in processed:
            continue
            
        processed.add(current_vertex.get_id())
        
        for neighbor, weight in current_vertex.get_connections():
            # Skip if we've already processed this neighbor
            if neighbor.get_id() in processed:
                continue
                
            if neighbor.get_distance() > weight:
                print(f"\nRelaxing edge: {current_vertex.get_id()} -> {neighbor.get_id()} (weight: {weight})")
                neighbor.set_distance(weight)
                neighbor.set_previous(current_vertex)
                pq.enqueue(neighbor, weight)  # Use the edge weight as priority
                print_priority_queue(pq)
    return graph

def get_minimum_spanning_tree(graph):
    mst = UndirectedGraph()
    for vertex_key in graph.get_vertices():
        vertex = graph.get_vertex(vertex_key)
        if vertex.get_previous():
            mst.add_edge(vertex.get_previous().get_id(), vertex.get_id(), vertex.get_distance())
    return mst

def main():
    g = UndirectedGraph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    g.add_vertex('G')
    g.add_vertex('S')

    g.add_edge('A', 'B', 7)
    g.add_edge('A', 'D', 4)
    g.add_edge('B', 'D', 2)
    g.add_edge('D', 'C', 5)
    g.add_edge('C', 'E', 2)
    g.add_edge('C', 'S', 8)
    g.add_edge('C', 'F', 5)
    g.add_edge('S', 'G', 8)
    g.add_edge('E', 'F', 10)
    g.add_edge('E', 'G', 10)
    g.add_edge('G', 'F', 2)

    # Run Prim-Jarnik algorithm
    prim_jarnik(g, 'A')
    
    # Get and print the minimum spanning tree
    mst = get_minimum_spanning_tree(g)
    print("\nMinimum Spanning Tree:")
    print(mst)
    
    print("\nMinimum Spanning Tree Edges:")
    for edge in mst.get_edges():
        print(f"{edge[0]} -- {edge[1]} (weight: {edge[2]})")
    
    # Print all vertex distances and previous vertices
    print("\nAll vertex distances:")
    for vertex_key in g.get_vertices():
        vertex = g.get_vertex(vertex_key)
        prev_id = vertex.get_previous().get_id() if vertex.get_previous() else None
        print(f"Vertex {vertex_key}: distance = {vertex.get_distance()}, previous = {prev_id}")

if __name__ == "__main__":
    main()
    