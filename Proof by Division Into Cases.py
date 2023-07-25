def is_even(number):
  """Returns True if number is even, False otherwise."""

  if number % 2 == 0:
    return True
  else:
    return False


def main():
  statement = "If a number is even, then it is divisible by 2."

  # Case 1: The number is positive.
  if number > 0:
    if number % 2 == 0:
      print(f"The statement '{statement}' is true for the case where the number is positive.")
    else:
      print(f"The statement '{statement}' is false for the case where the number is positive.")

  # Case 2: The number is negative.
  if number < 0:
    if number % 2 == 0:
      print(f"The statement '{statement}' is true for the case where the number is negative.")
    else:
      print(f"The statement '{statement}' is false for the case where the number is negative.")


if __name__ == "__main__":
  main()
