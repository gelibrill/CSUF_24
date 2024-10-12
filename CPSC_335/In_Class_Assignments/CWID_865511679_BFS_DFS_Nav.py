import pprint
from collections import deque

# BFS shortest path
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

# DFS Explore
def dfs_city_explore(city_graph, start, destination, path=None, visited=None):
    # Initialized the path and visited set during the first call
    if path is None:
        path = [start] #starting path is starting node/ defining starting node
    if visited is None:
        visited = set() # use set to store visiting nodes
    
    # Mark current node as visited node
    visited.add(start)

    #if current node is the destination (the exit), return path as result
    if start == destination:
        return path
    
    # Explore all the neighboring nodes of the current node
    for neighbor in city_graph.get(start, []):
        # If neighbor has not been visited, then perform DFS recursively
        if neighbor not in visited:
            # Recursively call on DFS for the neighbor
            result_path = dfs_city_explore(city_graph, neighbor, destination, path + [neighbor], visited)

            # If a valid path towards destination is found, we are returning here
            if result_path:
                return result_path
    # If no path found, return None
    return None

# Define the DFS function to explore the city road
def dfs_city_explore(city_graph, start, destination, path=None, visited=None):
    # Initialized the path and visited set during the first call
    if path is None:
        path = [start] #starting path is starting node/ defining starting node
    if visited is None:
        visited = set() # use set to store visiting nodes
    
    # Mark current node as visited node
    visited.add(start)

    #if current node is the destination (the exit), return path as result
    if start == destination:
        return path
    
    # Explore all the neighboring nodes of the current node
    for neighbor in city_graph.get(start, []):
        # If neighbor has not been visited, then perform DFS recursively
        if neighbor not in visited:
            # Recursively call on DFS for the neighbor
            result_path = dfs_city_explore(city_graph, neighbor, destination, path + [neighbor], visited)

            # If a valid path towards destination is found, we are returning here
            if result_path:
                return result_path
    # If no path found, return None
    return None

city_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'B']
}
print(f"\nCity Map: ")
pprint.pprint(city_graph)

# Starting Point
user_input = input(f"\nEnter the starting intersection: ").strip().upper()
if user_input.isalpha():
    start = user_input
else:
    print(f"Invalid Starting Point. Please specify 'A', 'B', 'C', or 'D'")

# Ending Point
user_input = input(f"Enter the destination intersection: ").strip().upper()
if user_input.isalpha():
    destination = user_input
else:
    print(f"Invalid Starting Point. Please specify 'A', 'B', 'C', or 'D'")

# Choice Input
choice_input = input(f"Choose Algorithm - BFS for shortest path or DFS for deep exploration: (BFS/DFS)  ").strip().lower()
if choice_input == "bfs":
    path = bfs_shortest_path(city_graph, start, destination)
   
    # Output of the result
    if path:
        print(f"\nShortest path from {start} to {destination}: {' -> '.join(path)}")
    else:
        print(f"\nShortest path from {start} to {destination} is Not Found")
elif choice_input == "dfs":
    path = dfs_city_explore(city_graph, start, destination)

    # Output of the result
    if path:
        print(f"\nPath to exit the city: { ' --> '.join(path)}")
    else:
        print(f"\nNo Path found from {start} to {destination}")
else:
    print("\nInvalid choice. Please specify 'BFS' or 'DFS'.")
print("\n")
