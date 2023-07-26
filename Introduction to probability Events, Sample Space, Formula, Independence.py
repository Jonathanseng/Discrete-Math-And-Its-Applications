def sample_space(s):
  """Returns the sample space of a set s."""
  if not s:
    return {set()}
  else:
    ps = set()
    for x in s:
      ps.update([{x}, s - {x}])
    return ps

def event(s, e):
  """Returns True if event e is in sample space s, False otherwise."""
  return e in sample_space(s)

def probability(e, s):
  """Returns the probability of event e in sample space s."""
  n = len(s)
  if event(s, e):
    return len(e) / n
  else:
    return 0

def independence(e1, e2, s):
  """Returns True if events e1 and e2 are independent in sample space s, False otherwise."""
  if not event(s, e1) or not event(s, e2):
    return True
  else:
    return probability(e1 & e2, s) == probability(e1, s) * probability(e2, s)

def main():
  """Prints the sample space, probability, and independence of events for a coin flip."""
  s = {'H', 'T'}
  e1 = {'H'}
  e2 = {'T'}
  print("Sample space:", sample_space(s))
  print("Probability of event H:", probability(e1, s))
  print("Probability of event T:", probability(e2, s))
  print("Independence of H and T:", independence(e1, e2, s))

if __name__ == "__main__":
  main()
