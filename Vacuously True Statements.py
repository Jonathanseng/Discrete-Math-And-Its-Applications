def is_vacuously_true(statement):
  """
  Returns True if the statement is vacuously true, False otherwise.

  Args:
    statement: A string representing a logical statement.

  Returns:
    True if the statement is vacuously true, False otherwise.
  """

  if statement == "True":
    return True

  if not isinstance(statement, str):
    return False

  # Check if the hypothesis of the statement is false.
  hypothesis, _ = statement.split("then")
  if not hypothesis:
    return False

  # If the hypothesis is false, then the statement is vacuously true.
  return not eval(hypothesis)

def main():
  print(is_vacuously_true("If the moon is made of cheese, then I am the King of France"))  # True
  print(is_vacuously_true("If 0 = 1, then 2 = 3"))  # True
  print(is_vacuously_true("If the square root of 2 is rational, then I am the Pope"))  # True
  print(is_vacuously_true("If there are an infinite number of prime numbers, then I am the Queen of England"))  # True
  print(is_vacuously_true("If unicorns exist, then I am a billionaire"))  # True

if __name__ == "__main__":
  main()
