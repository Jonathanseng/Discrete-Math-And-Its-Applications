def is_function(relation):
  """Returns True if relation is a function, False otherwise."""
  first_set = set()
  for x, y in relation:
    if x in first_set:
      return False
    first_set.add(x)
  for x, y in relation:
    for x2, y2 in relation:
      if x == x2 and y != y2:
        return False
  return True

def main():
  relation = {(1, 2), (2, 4), (3, 6)}
  print(is_function(relation))  # True

  relation = {(1, 2), (2, 4), (2, 6)}
  print(is_function(relation))  # False

if __name__ == "__main__":
  main()
