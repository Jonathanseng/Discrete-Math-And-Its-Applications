def biconditional_statement(p, q):
  """Returns True if p and q are logically equivalent, False otherwise."""
  return (p and q) or (not p and not q)


def main():
  print(biconditional_statement(True, True))  # True
  print(biconditional_statement(True, False))  # False
  print(biconditional_statement(False, True))  # False
  print(biconditional_statement(False, False))  # True


if __name__ == "__main__":
  main()
