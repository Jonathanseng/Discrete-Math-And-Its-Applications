def combinations_formula(n, r):
  """Returns the number of ways to choose r items from n items."""
  if r > n:
    return 0
  else:
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))

def main():
  """Prints the number of ways to choose 3 items from 5 items."""
  n = 5
  r = 3
  print("Number of ways to choose 3 items from 5 items:", combinations_formula(n, r))

if __name__ == "__main__":
  main()
