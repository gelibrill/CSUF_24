import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Class for creating GUI for Prim's Algorithm
class PrimsGUI:
    def __init__(self, root):
        self.root = root  # The main window for GUI
        self.root.title("Prim's Algorithm Visualization")
        self.graph = {}
        self.edges = []
        self.visited = set()
        self.mst = []
        self.edge_list = []

        self.setup_gui()

    # Method to create the GUI layout
    def setup_gui(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)  # adding extra padding

        # Input fields
        tk.Label(frame, text="Start Node:").grid(row=0, column=0)
        self.start_node_entry = tk.Entry(frame, width=5)
        self.start_node_entry.grid(row=0, column=1)

        # Input field for end node
        tk.Label(frame, text="End Node:").grid(row=0, column=2)
        self.end_node_entry = tk.Entry(frame, width=5)
        self.end_node_entry.grid(row=0, column=3)

        # Input field for edge weight
        tk.Label(frame, text="Weight:").grid(row=0, column=4)
        self.weight_entry = tk.Entry(frame, width=5)
        self.weight_entry.grid(row=0, column=5)

        # Button to add edge to the graph
        tk.Button(frame, text="Add Edge", command=self.add_edge).grid(row=0, column=6, padx=5)

        # Button to remove the last added edge
        tk.Button(frame, text="Back", command=self.remove_last_edge).grid(row=0, column=7, padx=5)
        # Button to Start Prim's Algorithm
        tk.Button(frame, text="Start Prim's", command=self.start_prims).grid(row=0, column=8, padx=5)

        # Input field for Prim's start node
        tk.Label(frame, text="Prim's Start Node:").grid(row=1, column=0)
        self.prims_start_node_entry = tk.Entry(frame, width=5)
        self.prims_start_node_entry.grid(row=1, column=1)

        # Button to move to the next step in Prim's Algorithm
        self.next_button = tk.Button(self.root, text="Next", command=self.next_step, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        # Create a canvas to display the graph using Matplotlib
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    # Method to add an edge
    def add_edge(self):
        start_node = self.start_node_entry.get()
        end_node = self.end_node_entry.get()
        weight = self.weight_entry.get()

        # Check for valid inputs
        if not start_node or not end_node or not weight:
            messagebox.showerror("Error", "Please enter a valid start and end node with the corresponding weight.")
            return
        try:
            weight = int(weight)
        except ValueError:
            messagebox.showerror("Error", "Weight must be an integer.")
            return

        # Add the edge to the graph adjacency list
        if start_node not in self.graph:
            self.graph[start_node] = []
        if end_node not in self.graph:
            self.graph[end_node] = []

        # Add the edge in both directions for an undirected graph
        self.graph[start_node].append((end_node, weight))
        self.graph[end_node].append((start_node, weight))

        # Add the edge to the list of edges
        self.edges.append((start_node, end_node, weight))

        # Clear input fields after adding edge
        self.start_node_entry.delete(0, tk.END)
        self.end_node_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)

        # Update the graph visualization
        self.update_graph()

    # Method to remove the last edge added
    def remove_last_edge(self):
        if not self.edges:
            messagebox.showinfo("Info", "No edges to remove.")
            return

        # Remove the last edge from the list
        last_edge = self.edges.pop()
        u, v, weight = last_edge

        # Remove edge from adjacency list
        self.graph[u].remove((v, weight))
        self.graph[v].remove((u, weight))

        # Update the graph visualization
        self.update_graph()

    # Method to update the graph visualization
    def update_graph(self, mst_edges=[]):
        self.ax.clear()
        G = nx.Graph()

        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                G.add_edge(node, neighbor, weight=weight)
        pos = nx.spring_layout(G)

        # Draw all the edges in the graph
        nx.draw(G, pos, ax=self.ax, with_labels=True, node_color='lightgray', node_size=500)
        nx.draw_networkx_edge_labels(G, pos, ax=self.ax,
                                     edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

        # Highlight the MST edges in red
        if mst_edges:
            mst_graph = nx.Graph()
            mst_graph.add_edges_from([(u, v) for u, v, _ in mst_edges])
            nx.draw(mst_graph, pos, ax=self.ax, with_labels=True, node_color='lightgreen',
                    node_size=500, edge_color='red', width=2)

        # Update the Canvas to show updated graph
        self.canvas.draw()

    # Method to start Prim's Algorithm
    def start_prims(self):
        start_node = self.prims_start_node_entry.get()

        # Check if the start node is valid
        if start_node not in self.graph:
            messagebox.showerror("Error", "Please enter a valid start node for Prim's Algorithm.")
            return

        # Initialize sets for the MST construction
        self.start_node = start_node
        self.visited = {self.start_node}
        self.edge_list = [(weight, self.start_node, neighbor) for neighbor, weight in self.graph[self.start_node]]
        self.edge_list.sort(key=lambda x: x[0])

        self.mst = []
        self.next_button.config(state=tk.NORMAL)

    # Method to execute the next step of Prim's Algorithm
    def next_step(self):
        # Check if MST is already completed
        if len(self.visited) == len(self.graph):
            messagebox.showinfo("Completed", "Prim's Algorithm is complete.")
            self.next_button.config(state=tk.DISABLED)
            return

        # Selecting the next smallest edge
        while self.edge_list:
            weight, u, v = self.edge_list.pop(0)
            if v not in self.visited:
                self.visited.add(v)
                self.mst.append((u, v, weight))

                for neighbor, w in self.graph[v]:
                    if neighbor not in self.visited:
                        self.edge_list.append((w, v, neighbor))
                self.edge_list.sort(key=lambda x: x[0])
                break
        else:
            messagebox.showinfo("Info", "No more edges to process. The graph might be disconnected.")
            self.next_button.config(state=tk.DISABLED)
            return

        self.update_graph(self.mst)

# Create the main window of GUI
root = tk.Tk()
app = PrimsGUI(root)
root.mainloop()