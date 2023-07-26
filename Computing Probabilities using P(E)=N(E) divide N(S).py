def probability(e, s):
  """Returns the probability of event e in sample space s."""
  n = len(s)
  if event(s, e):
    return len(e) / n
  else:
    return 0

def main():
  """Prints the probability of getting heads when flipping a coin."""
  s = {'H', 'T'}
  e = {'H'}
  print("Probability of getting heads:", probability(e, s))

if __name__ == "__main__":
  main()
