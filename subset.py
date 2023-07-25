def is_subset(set1, set2):
  """
  Returns True if set1 is a subset of set2, False otherwise.
  """
  for element in set1:
    if element not in set2:
      return False
  return True

def main():
  set1 = {1, 2, 3}
  set2 = {1, 2, 3, 4, 5}
  print(is_subset(set1, set2))

if __name__ == '__main__':
  main()
