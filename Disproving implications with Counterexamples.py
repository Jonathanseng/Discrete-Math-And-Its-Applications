def is_even(number):
  """Returns True if number is even, False otherwise."""

  if number % 2 == 0:
    return True
  else:
    return False


def main():
  implication = "If a number is even, then it is divisible by 2."
  counterexample = 2

  if is_even(counterexample) and not is_divisible(counterexample, 2):
    print(f"The implication '{implication}' is disproved by the counterexample {counterexample}.")
  else:
    print(f"The implication '{implication}' is not disproved by the counterexample {counterexample}.")


if __name__ == "__main__":
  main()
