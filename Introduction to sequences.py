def arithmetic_sequence(first_term, common_difference, n):
  """Returns an arithmetic sequence."""
  sequence = []
  for i in range(n):
    sequence.append(first_term + i * common_difference)
  return sequence

def geometric_sequence(first_term, common_ratio, n):
  """Returns a geometric sequence."""
  sequence = []
  for i in range(n):
    sequence.append(first_term * common_ratio**i)
  return sequence

def quadratic_sequence(first_term, common_difference, n):
  """Returns a quadratic sequence."""
  sequence = []
  for i in range(n):
    sequence.append(first_term + i * common_difference * i)
  return sequence

def main():
  """Prints the first 10 terms of an arithmetic, geometric, and quadratic sequence."""
  print("Arithmetic sequence:")
  print(arithmetic_sequence(1, 2, 10))
  print("Geometric sequence:")
  print(geometric_sequence(2, 2, 10))
  print("Quadratic sequence:")
  print(quadratic_sequence(1, 3, 10))

if __name__ == "__main__":
  main()
