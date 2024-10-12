from collections import deque
# Function to perform BFS to find the shortest path in given city map

def bfs_shortest_path(city_graph, start, destination):
    # Queue for BFS paths to explore
    queue = deque([start])
    # Set to track visted intersections
    visited = set()

    # Continue BFS until all paths are explored
    while queue:
        # Dequeue the current path to explore
        path = queue.popleft() #popleft from collections

        current_intersection = path[-1]
        # Check is destination has been reached
        if current_intersection == destination:
            return path
        
        # If not visited, explore neighbors
        if current_intersection not in visited:
            visited.add(current_intersection)

            # Add all neighbors to queue as a new path
            for neighbor in city_graph.get(current_intersection, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    # If no path found, return None
    return None
    
# Example of UNWEIGHTED city graph
city_graph = {
    # Harcoding for class purposes, but can be very dynamic in real applications
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

# Call our BFS to find the shortest path
start = 'A'
destination = 'E'

path = bfs_shortest_path(city_graph, start, destination)

# Print output result

if path:
    print(f"Shortest path from {start} to {destination}: {' -> '.join(path)}")
else:
    print(f"Shortest path from {start} to {destination} is Not Found")
