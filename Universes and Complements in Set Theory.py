def universe():
  """
  Returns the universal set.

  Returns:
    The universal set.
  """

  return set()


def complement(set1, universe):
  """
  Returns the complement of set1 in universe.

  Args:
    set1: The set to be complemented.
    universe: The universal set.

  Returns:
    The complement of set1 in universe.
  """

  complement_set = universe.copy()
  complement_set.difference_update(set1)
  return complement_set


if __name__ == "__main__":
  set1 = {1, 2, 3, 4, 5}
  universe = {1, 2, 3, 4, 5, 6, 7, 8, 9}
  print(complement(set1, universe))
