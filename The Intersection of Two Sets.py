def intersection(set1, set2):
  """
  Returns the intersection of two sets.

  Args:
    set1: The first set.
    set2: The second set.

  Returns:
    The intersection of the two sets.
  """

  intersection_set = set()
  for x in set1:
    if x in set2:
      intersection_set.add(x)
  return intersection_set


if __name__ == "__main__":
  set1 = {1, 2, 3, 4, 5}
  set2 = {2, 3, 4, 6, 7}
  print(intersection(set1, set2))
