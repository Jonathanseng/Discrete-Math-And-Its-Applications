def conditional_probability(e1, e2, s):
  """Returns the conditional probability of event e1 given event e2 in sample space s."""
  return probability(e1 & e2, s) / probability(e2, s)

def main():
  """Prints the conditional probability of event H given event T in a coin flip."""
  s = {'H', 'T'}
  e1 = {'H'}
  e2 = {'T'}
  print("Conditional probability of H given T:", conditional_probability(e1, e2, s))

if __name__ == "__main__":
  main()
