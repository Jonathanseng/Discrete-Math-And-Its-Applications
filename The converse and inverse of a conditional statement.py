def converse(statement):
  """
  Returns the converse of the conditional statement.

  Args:
    statement: A string representing a conditional statement.

  Returns:
    A string representing the converse of the conditional statement.
  """

  hypothesis, _ = statement.split("then")
  return _ + " then " + hypothesis

def inverse(statement):
  """
  Returns the inverse of the conditional statement.

  Args:
    statement: A string representing a conditional statement.

  Returns:
    A string representing the inverse of the conditional statement.
  """

  hypothesis, _ = statement.split("then")
  negation_of_hypothesis = "not " + hypothesis
  negation_of_conclusion = "not " + _

  return negation_of_hypothesis + " then " + negation_of_conclusion

def main():
  print(converse("If it is raining, then the ground is wet"))  # "If the ground is wet, then it is raining"
  print(inverse("If it is raining, then the ground is wet"))  # "If it is not raining, then the ground is not wet"

if __name__ == "__main__":
  main()
