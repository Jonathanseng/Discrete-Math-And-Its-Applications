def is_necessary(condition, consequence):
  """Returns True if condition is necessary for consequence, False otherwise."""

  for value in [True, False]:
    if condition == value and consequence != value:
      return False

  return True


def is_sufficient(condition, consequence):
  """Returns True if condition is sufficient for consequence, False otherwise."""

  for value in [True, False]:
    if condition == value and consequence == value:
      return True

  return False


def is_necessary_and_sufficient(condition, consequence):
  """Returns True if condition is necessary and sufficient for consequence, False otherwise."""

  return is_necessary(condition, consequence) and is_sufficient(condition, consequence)


def main():
  print("Being a male is a necessary condition for being a brother.")
  print(is_necessary("is a male", "is a brother"))

  print("Having four sides is a sufficient condition for being a square.")
  print(is_sufficient("has four sides", "is a square"))

  print("Having four sides and all four sides being the same length is a necessary and sufficient condition for being a square.")
  print(is_necessary_and_sufficient("has four sides and all four sides are the same length", "is a square"))


if __name__ == "__main__":
  main()
