def is_divisible(a, b):
  """Returns True if a is divisible by b, False otherwise."""

  if b == 0:
    return False
  else:
    return a % b == 0


def main():
  a = 6
  b = 2
  c = 1

  if is_divisible(a, b) and is_divisible(b, c):
    print("Divisibility is transitive.")
  else:
    print("Divisibility is not transitive.")


if __name__ == "__main__":
  main()
