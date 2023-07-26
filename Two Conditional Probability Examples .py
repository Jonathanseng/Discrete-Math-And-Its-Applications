def conditional_probability_example_1(s):
  """Returns the conditional probability of event A given event B in sample space s."""
  e1 = {'A', 'B'}
  e2 = {'B'}
  return probability(e1 & e2, s) / probability(e2, s)

def conditional_probability_example_2(s):
  """Returns the conditional probability of event B given event A in sample space s."""
  e1 = {'A', 'B'}
  e2 = {'A'}
  return probability(e1 & e2, s) / probability(e1, s)

def main():
  """Prints the conditional probabilities of events A and B in two different sample spaces."""
  s1 = {'A', 'B', 'C'}
  s2 = {'A', 'B'}
  print("Conditional probability of A given B in s1:", conditional_probability_example_1(s1))
  print("Conditional probability of B given A in s2:", conditional_probability_example_2(s2))

if __name__ == "__main__":
  main()
