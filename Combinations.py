import math

def combinations(n, r):
  """
  Returns the number of combinations of r items from a set of n items.
  """

  return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

def main():
  n = 5
  r = 3
  print(combinations(n, r))

if __name__ == "__main__":
  main()
