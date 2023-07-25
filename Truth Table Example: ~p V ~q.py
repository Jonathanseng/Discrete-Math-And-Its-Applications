def truth_table(statement1, statement2):
  """Returns a truth table for the given statements."""
  table = []
  for p in [True, False]:
    for q in [True, False]:
      table.append((p, q, not p, not q, not p or not q))
  return table

def main():
  print(truth_table(True, True))  # [[True, True, False, False, False]]
  print(truth_table(True, False))  # [[True, False, False, True, True]]
  print(truth_table(False, True))  # [[False, True, True, False, True]]
  print(truth_table(False, False))  # [[False, False, True, True, True]]

if __name__ == "__main__":
  main()
