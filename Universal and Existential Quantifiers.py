def forall(predicate, values):
  """Returns True if predicate is true for all values in values."""
  for value in values:
    if not predicate(value):
      return False
  return True

def exists(predicate, values):
  """Returns True if predicate is true for at least one value in values."""
  for value in values:
    if predicate(value):
      return True
  return False

if __name__ == "__main__":
  print(forall(lambda x: x % 2 == 0, range(10)))  # True
  print(forall(lambda x: x % 2 == 0, range(11)))  # False
  print(exists(lambda x: x > 10, range(10)))  # True
  print(exists(lambda x: x > 10, range(5)))  # False
