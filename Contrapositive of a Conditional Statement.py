def contrapositive(statement):
  """
  Returns the contrapositive of the conditional statement.

  Args:
    statement: A string representing a conditional statement.

  Returns:
    A string representing the contrapositive of the conditional statement.
  """

  hypothesis, _ = statement.split("then")
  negation_of_hypothesis = "not " + hypothesis
  negation_of_conclusion = "not " + _

  return negation_of_conclusion + " then " + negation_of_hypothesis

def main():
  print(contrapositive("If it is raining, then the ground is wet"))  # "If the ground is not wet, then it is not raining"
  print(contrapositive("If I am a cat, then I have fur"))  # "If I do not have fur, then I am not a cat"
  print(contrapositive("If I am a student, then I go to school"))  # "If I do not go to school, then I am not a student"

if __name__ == "__main__":
  main()
