def is_divisible_by_3(n):
  """Returns True if n is divisible by 3, False otherwise."""
  if n % 3 == 0:
    return True
  else:
    return False

def main():
  """Prints whether or not the statement holds for the first 10 natural numbers."""
  for i in range(1, 11):
    print(is_divisible_by_3(i))

if __name__ == "__main__":
  main()
