def is_rational(number):
  """Returns True if number is rational, False otherwise."""

  try:
    fractions.Fraction(number)
    return True
  except:
    return False


def main():
  statement = "The square root of 2 is irrational."

  # Assume the opposite of the statement.
  assume_rational = True

  # Derive a contradiction from the assumption.
  if assume_rational:
    if is_rational(2 ** 0.5):
      print(f"The statement '{statement}' is false.")
    else:
      print(f"The statement '{statement}' is true.")


if __name__ == "__main__":
  main()
