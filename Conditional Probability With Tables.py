def conditional_probability_with_tables(e1, e2, s):
  """Returns the conditional probability of event e1 given event e2 in sample space s."""
  table = [[0] * len(s) for _ in range(len(s))]
  for i in range(len(s)):
    for j in range(len(s)):
      if (i in e1 and j in e2) or (i not in e1 and j not in e2):
        table[i][j] = 1
      else:
        table[i][j] = 0
  return table[e1][e2] / sum(table[e2])

def main():
  """Prints the conditional probability of event A given event B in a table."""
  s = {'A', 'B', 'C'}
  e1 = {'A', 'B'}
  e2 = {'B'}
  print("Conditional probability of A given B:", conditional_probability_with_tables(e1, e2, s))

if __name__ == "__main__":
  main()
