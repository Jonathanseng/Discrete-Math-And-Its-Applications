def relation(s, t):
  """Returns the relation from set s to set t."""
  r = set()
  for x in s:
    for y in t:
      if x == y:
        r.add((x, y))
  return r

def inverse(r):
  """Returns the inverse of relation r."""
  inv = set()
  for x, y in r:
    inv.add((y, x))
  return inv

def main():
  """Prints the relation {(1, 1), (2, 2), (3, 3)} and its inverse."""
  s = {1, 2, 3}
  t = s
  r = relation(s, t)
  print(r)
  inv = inverse(r)
  print(inv)

if __name__ == "__main__":
  main()
