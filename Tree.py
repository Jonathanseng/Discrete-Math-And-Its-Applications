class Tree:
  """
  Represents a tree data structure.
  """

  def __init__(self, value):
    """
    Create a new tree.

    Args:
      value: The value of the root node.
    """

    self.value = value
    self.children = []

  def add_child(self, child):
    """
    Add a child to the tree.

    Args:
      child: The child node to add.
    """

    self.children.append(child)

  def __repr__(self):
    """
    Return a string representation of the tree.
    """

    return f"Tree({self.value}, {self.children})"

def main():
  root = Tree("root")
  child1 = Tree("child1")
  child2 = Tree("child2")
  root.add_child(child1)
  root.add_child(child2)
  print(root)

if __name__ == "__main__":
  main()
