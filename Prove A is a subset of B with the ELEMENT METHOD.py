def is_subset_element_method(A, B):
  """Returns True if A is a subset of B using the element method, False otherwise."""
  for x in A:
    if x not in B:
      return False
  return True


A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(is_subset_element_method(A, B))
