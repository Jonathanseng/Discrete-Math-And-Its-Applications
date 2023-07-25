def is_reflexive(relation):
  """Returns True if the relation is reflexive, False otherwise."""
  for x in relation:
    if (x, x) not in relation:
      return False
  return True

def is_symmetric(relation):
  """Returns True if the relation is symmetric, False otherwise."""
  for x, y in relation:
    if (y, x) not in relation:
      return False
  return True

def is_transitive(relation):
  """Returns True if the relation is transitive, False otherwise."""
  for x, y in relation:
    for z in relation:
      if (y, z) in relation and not ((x, z) in relation):
        return False
  return True

def main():
  relation = {(0, 0), (2, 2), (4, 4), (0, 2), (2, 4)}
  print(is_reflexive(relation))  # True
  print(is_symmetric(relation))  # True
  print(is_transitive(relation))  # True

if __name__ == "__main__":
  main()
