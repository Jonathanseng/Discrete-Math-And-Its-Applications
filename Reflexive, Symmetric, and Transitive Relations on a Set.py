def reflexive(r):
  """Returns True if a relation R on set A is reflexive, False otherwise."""
  for a in A:
    if (a, a) not in R:
      return False
  return True

def symmetric(r):
  """Returns True if a relation R on set A is symmetric, False otherwise."""
  for a, b in R:
    if (b, a) not in R:
      return False
  return True

def transitive(r):
  """Returns True if a relation R on set A is transitive, False otherwise."""
  for a in A:
    for b in A:
      if (a, b) in R:
        for c in A:
          if (b, c) in R and (a, c) not in R:
            return False
  return True

def main():
  """Prints whether the relation {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)} is reflexive, symmetric, and transitive."""
  A = set([1, 2, 3])
  r = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
  print("Reflexive:", reflexive(r))
  print("Symmetric:", symmetric(r))
  print("Transitive:", transitive(r))

if __name__ == "__main__":
  main()
