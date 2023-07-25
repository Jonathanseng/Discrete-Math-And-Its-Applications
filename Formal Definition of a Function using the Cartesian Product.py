def is_function(set_of_ordered_pairs):
  """Returns True if set_of_ordered_pairs is a function, False otherwise."""
  for x, y in set_of_ordered_pairs:
    if (x, y) in set_of_ordered_pairs:
      return False
  return True

def main():
  set_of_ordered_pairs = {(1, 1), (2, 4), (3, 9)}
  print(is_function(set_of_ordered_pairs))  # True

if __name__ == "__main__":
  main()
