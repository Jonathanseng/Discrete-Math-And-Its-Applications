import fractions


def is_rational(number):
  """Returns True if number is a rational number, False otherwise."""

  try:
    fractions.Fraction(number)
    return True
  except:
    return False


def main():
  print("1/2 is a rational number:", is_rational(1/2))
  print("3.14 is a rational number:", is_rational(3.14))
  print("-5/6 is a rational number:", is_rational(-5/6))
  print("1 1/2 is a rational number:", is_rational(1 1/2))
  print("1/0 is not a rational number:", is_rational(1/0))


if __name__ == "__main__":
  main()
