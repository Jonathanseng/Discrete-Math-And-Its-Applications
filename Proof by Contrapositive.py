def is_even(number):
  """Returns True if number is even, False otherwise."""

  if number % 2 == 0:
    return True
  else:
    return False


def main():
  statement = "If a number is even, then it is divisible by 2."

  # Negate the conclusion of the statement.
  negation_of_conclusion = "The number is not divisible by 2 or the number is not even."

  # Assume the negation of the conclusion.
  assume_not_divisible_by_2 = True

  # Derive the negation of the hypothesis.
  if assume_not_divisible_by_2:
    if is_even(2):
      print(f"The statement '{statement}' is true.")
    else:
      print(f"The statement '{statement}' is false.")


if __name__ == "__main__":
  main()
