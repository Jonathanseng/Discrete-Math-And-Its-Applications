import turtle

def draw_polygon(sides, side_length):
  """
  Draws a polygon with the given number of sides and side length.
  """

  for i in range(sides):
    turtle.forward(side_length)
    turtle.left(360 / sides)

def main():
  sides = 6
  side_length = 100
  draw_polygon(sides, side_length)

if __name__ == "__main__":
  main()
