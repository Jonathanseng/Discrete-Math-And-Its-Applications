def powerset(s):
  """Returns the power set of set s."""
  if not s:
    return {set()}
  else:
    ps = set()
    for x in s:
      ps.update([{x}, s - {x}])
    return ps

def main():
  """Prints the power set of set {1, 2, 3}."""
  s = {1, 2, 3}
  ps = powerset(s)
  print(ps)

if __name__ == "__main__":
  main()
