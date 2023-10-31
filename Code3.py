class Graph:
  """A class that represents a graph."""

  def __init__(self):
    """Initializes the Graph object."""
    self.nodes = []
    self.edges = []

  def add_node(self, node):
    """Adds a node to the graph."""
    self.nodes.append(node)

  def add_edge(self, node1, node2):
    """Adds an edge between two nodes in the graph."""
    self.edges.append((node1, node2))

  def get_neighbors(self, node):
    """Returns a list of all the nodes that are connected to the given node."""
    neighbors = []
    for edge in self.edges:
      if edge[0] == node:
        neighbors.append(edge[1])
    return neighbors

  def bfs(self, start_node):
    """Performs a breadth-first search on the graph starting from the given node."""
    visited = set()
    queue = [start_node]
    while queue:
      node = queue.pop(0)
      visited.add(node)
      for neighbor in self.get_neighbors(node):
        if neighbor not in visited:
          queue.append(neighbor)
          visited.add(neighbor)

  def dfs(self, start_node):
    """Performs a depth-first search on the graph starting from the given node."""
    visited = set()
    stack = [start_node]
    while stack:
      node = stack.pop()
      visited.add(node)
      for neighbor in self.get_neighbors(node):
        if neighbor not in visited:
          stack.append(neighbor)
          visited.add(neighbor)
