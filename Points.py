class Point:
  """
  Represents a point in space.
  """

  def __init__(self, x, y):
    """
    Create a new point.

    Args:
      x: The x-coordinate of the point.
      y: The y-coordinate of the point.
    """

    self.x = x
    self.y = y

  def __repr__(self):
    """
    Return a string representation of the point.
    """

    return f"Point({self.x}, {self.y})"

def main():
  point = Point(3, 4)
  print(point)

if __name__ == "__main__":
  main()
