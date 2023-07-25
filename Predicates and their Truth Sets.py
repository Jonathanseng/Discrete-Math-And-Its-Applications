def is_even(x):
  """Returns True if x is even, False otherwise."""
  return x % 2 == 0

def is_prime(x):
  """Returns True if x is prime, False otherwise."""
  if x <= 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

def is_real_number_greater_than_0(x):
  """Returns True if x is a real number greater than 0, False otherwise."""
  return x > 0

def truth_set(predicate):
  """Returns the truth set of the predicate."""
  truth_set = set()
  for x in range(-10, 10):
    if predicate(x):
      truth_set.add(x)
  return truth_set

if __name__ == "__main__":
  print(truth_set(is_even))  # {..., -2, 0, 2, 4, 6, ...}
  print(truth_set(is_prime))  # {2, 3, 5, 7, 11, 13, ...}
  print(truth_set(is_real_number_greater_than_0))  # {..., 1, 2, 3, 4, ...}
