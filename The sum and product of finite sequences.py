def sum_of_sequences(A, B):
  """Returns the sum of two finite sequences."""
  sum_sequence = []
  for i in range(len(A)):
    sum_sequence.append(A[i] + B[i])
  return sum_sequence

def product_of_sequences(A, B):
  """Returns the product of two finite sequences."""
  product_sequence = []
  for i in range(len(A)):
    product_sequence.append(A[i] * B[i])
  return product_sequence

def main():
  """Prints the sum and product of two finite sequences."""
  A = (1, 2, 3, 4)
  B = (5, 6, 7, 8)
  print("Sum:", sum_of_sequences(A, B))
  print("Product:", product_of_sequences(A, B))

if __name__ == "__main__":
  main()
