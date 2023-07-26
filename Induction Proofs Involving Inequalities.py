def is_less_than_square(n):
  """Returns True if n is less than n^2, False otherwise."""
  if n == 1:
    return True
  else:
    return n < n**2

def main():
  """Prints whether or not the inequality holds for the first 10 natural numbers."""
  for i in range(1, 11):
    print(is_less_than_square(i))

if __name__ == "__main__":
  main()
