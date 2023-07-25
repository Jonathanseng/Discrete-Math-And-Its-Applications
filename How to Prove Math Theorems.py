def prove_theorem(theorem, assumptions, steps):
  """Returns True if the theorem can be proven using the assumptions and steps, False otherwise."""

  if theorem not in steps:
    raise ValueError(f"Theorem {theorem} is not in the steps.")

  if not assumptions:
    if steps[theorem]:
      return True
    else:
      return False

  for assumption in assumptions:
    if not prove_theorem(assumption, assumptions - {assumption}, steps):
      return False

  if steps[theorem]:
    return True
  else:
    return False


def main():
  theorem = "If x is a natural number, then x + 1 is a natural number."
  assumptions = ["x is a natural number"]
  steps = {
    "x is a natural number": True,
    "x + 1 is a natural number": True,
  }

  if prove_theorem(theorem, assumptions, steps):
    print("Theorem can be proven.")
  else:
    print("Theorem cannot be proven.")


if __name__ == "__main__":
  main()
