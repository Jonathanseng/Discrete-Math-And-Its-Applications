def sum_of_first_n_natural_numbers(n):
  """Returns the sum of the first n natural numbers."""
  if n == 1:
    return 1
  else:
    return sum_of_first_n_natural_numbers(n - 1) + n

def main():
  """Prints the sum of the first 10 natural numbers."""
  print(sum_of_first_n_natural_numbers(10))

if __name__ == "__main__":
  main()
