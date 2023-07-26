def spot_reflexivity(r):
  """Returns True if a relation R on set A is reflexive, False otherwise."""
  for a in A:
    if (a, a) not in R:
      return False
  return True

def spot_symmetry(r):
  """Returns True if a relation R on set A is symmetric, False otherwise."""
  for a, b in R:
    if (b, a) not in R:
      return False
  return True

def spot_transitivity(r):
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
  print("Reflexive:", spot_reflexivity(r))
  print("Symmetric:", spot_symmetry(r))
  print("Transitive:", spot_transitivity(r))

if __name__ == "__main__":
  main()
