# Implementing City Graph (Street Map) and finding shortest path via Dijkstra Algorithm

# Import heap
import heapq

# Define algorithm function
def dijkstra(graph, source, destination):

    # Step 1: Initialize distances to infinity & set source distance
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Priority queue to store distance and node information
    priority_queue = [(0, source)]

    # Dictionary to keep track of shortest path
    previous_nodes = {node: None for node in graph}

    # Step 2: while priority queue is NOT empty, process each node
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == destination:
            break
        # if current distance is already higher than recorded one, skip it
        if current_distance > distances[current_node]:
            continue

    # Step 3: Check all neighbors of current node
        for neighbor, weight in graph[current_node].items():
            # Calculate new distance to neighbor
            distance = current_distance + weight

            # If new distance is shorter, update distance & path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Step 4: Reconstruct the shortest path from source to destination
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse() # Reversing the path to start from the source node.

    # Step 5: Returning the shortest distance and path.
    return distances[destination], path

# Sample Street Map
def build_city_graph():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 5},
        'C': {'A': 2, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 4},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 4, 'E': 3}
    }
    return graph

# Function for user interaction
def main():
    city_graph = build_city_graph()

    # Display available nodes to user
    print("\nAvailable Cities / Intersections", list(city_graph.keys()), "\n")

    # Get User Input
    source = input ("Enter the Starting Point: ")
    destination = input("Enter the destination point: ")

    # Validate User input
    if source not in city_graph or destination not in city_graph:
        print("\nInvalid Selection, please enter valid entry.")
        return
    
    # Call Dijsktra Algorithm
    distance, path = dijkstra(city_graph, source, destination)

    # Print outcome
    if distance == float('inf'):
        print(f"No Path Found from {source} to {destination}.\n")
    else:
        print(f'Shortest path from {source} to {destination}: {' --> '.join(path)}\n')
        print(f'Total Distance: {distance} cost\n')
if __name__ == "__main__":
    main()
