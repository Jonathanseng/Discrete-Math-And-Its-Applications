def truth_table(statement1, statement2):
  """Returns a truth table for the given statements."""
  table = []
  for p in [True, False]:
    for q in [True, False]:
      table.append((p, q, not p, p and q, p or q))
  return table

def main():
  print(truth_table("It is raining", "The ground is wet"))  # [[True, True, False, True, True], [True, False, True, False, True], [False, True, True, False, True], [False, False, True, False, False]]
  print(truth_table("It is raining", "The ground is not wet"))  # [[True, True, False, False, False], [True, False, True, False, False], [False, True, True, False, False], [False, False, True, False, True]]

if __name__ == "__main__":
  main()
