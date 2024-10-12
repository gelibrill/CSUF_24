# Define the DFS function to solve the given maze

def dfs_maze_solver(maze_graph, start, destination, path=None, visited=None):
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
    for neighbor in maze_graph.get(start, []):
        # If neighbor has not been visited, then perform DFS recursively
        if neighbor not in visited:
            # Recursively call on DFS for the neighbor
            result_path = dfs_maze_solver(maze_graph, neighbor, destination, path + [neighbor], visited)

            # If a valid path towards destination is found, we are returning here
            if result_path:
                return result_path
    # If no path found, return None
    return None

# Predefined Maze graph using an adjaceny list

maze_graph = {
    'Start': ['A', 'B'], # Start node connected to A and B
    'A': ['Start', 'C'], # A node connected to Start and C
    'B': ['Start', 'D'], # B node connected to Start and D
    'C': ['A', 'Exit'], # C node connected to A and Exit
    'D': ['B'], # D node connected to B
    'Exit': ['']
}

start = 'Start'
destination = 'Exit'

path = dfs_maze_solver(maze_graph, start, destination)

# Output of the result
if path:
    print(f"Path to exit the maze: { ' --> '.join(path)}")
else:
    print(f"No Path found from {start} to {destination}")