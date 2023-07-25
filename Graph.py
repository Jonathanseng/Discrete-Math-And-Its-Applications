class Graph:
  """
  Represents a graph data structure.
  """

  def __init__(self):
    """
    Create a new graph.
    """

    self.nodes = set()
    self.edges = {}

  def add_node(self, node):
    """
    Add a node to the graph.

    Args:
      node: The node to add.
    """

    self.nodes.add(node)

  def add_edge(self, node1, node2):
    """
    Add an edge to the graph.

    Args:
      node1: The first node of the edge.
      node2: The second node of the edge.
    """

    if node1 not in self.nodes or node2 not in self.nodes:
      raise ValueError("The nodes must be in the graph")

    self.edges.setdefault(node1, set()).add(node2)
    self.edges.setdefault(node2, set()).add(node1)

  def __repr__(self):
    """
    Return a string representation of the graph.
    """

    return f"Graph(nodes={self.nodes}, edges={self.edges})"

def main():
  graph = Graph()
  graph.add_node("A")
  graph.add_node("B")
  graph.add_node("C")
  graph.add_edge("A", "B")
  graph.add_edge("B", "C")
  print(graph)

if __name__ == "__main__":
  main()
