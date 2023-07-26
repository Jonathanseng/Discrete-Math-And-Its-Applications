def union(set1, set2):
  """
  Returns the union of two sets.

  Args:
    set1: The first set.
    set2: The second set.

  Returns:
    The union of the two sets.
  """

  union_set = set()
  union_set.update(set1)
  union_set.update(set2)
  return union_set


if __name__ == "__main__":
  set1 = {1, 2, 3, 4, 5}
  set2 = {2, 3, 4, 6, 7}
  print(union(set1, set2))
