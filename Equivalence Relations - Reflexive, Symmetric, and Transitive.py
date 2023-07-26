def equivalence_relation(r):
  """Returns True if a relation R on set A is an equivalence relation, False otherwise."""
  return reflexive(r) and symmetric(r) and transitive(r)

def main():
  """Prints whether the relation {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)} is an equivalence relation."""
  A = set([1, 2, 3])
  r = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
  print("Equivalence relation:", equivalence_relation(r))

if __name__ == "__main__":
  main()
