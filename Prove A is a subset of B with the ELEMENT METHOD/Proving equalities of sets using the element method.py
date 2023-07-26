def are_equal_element_method(A, B):
  """Returns True if A and B are equal using the element method, False otherwise."""
  for x in A:
    if x not in B:
      return False
  for x in B:
    if x not in A:
      return False
  return True


A = {1, 2, 3}
B = {2, 3, 1}

print(are_equal_element_method(A, B))
