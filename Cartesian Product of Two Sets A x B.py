def cartesian_product(A, B):
  """
  Returns the Cartesian product of two sets A and B.

  Args:
    A: A set.
    B: A set.

  Returns:
    A list of all pairs (a, b) where a is in A and b is in B.
  """

  product = []
  for a in A:
    for b in B:
      product.append((a, b))
  return product


if __name__ == "__main__":
  A = {1, 2, 3}
  B = {"a", "b", "c"}
  print(cartesian_product(A, B))
