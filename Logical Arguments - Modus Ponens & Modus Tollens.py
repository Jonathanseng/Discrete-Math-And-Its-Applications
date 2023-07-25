def modus_ponens(antecedent, consequent):
  """Returns True if the argument is a valid modus ponens argument, False otherwise."""
  if antecedent and consequent:
    return True
  else:
    return False

def modus_tollens(antecedent, consequent):
  """Returns True if the argument is a valid modus tollens argument, False otherwise."""
  if not antecedent and not consequent:
    return True
  else:
    return False

if __name__ == "__main__":
  print(modus_ponens("It is raining", "The ground is wet"))  # True
  print(modus_ponens("I am in France", "I speak French"))  # False
  print(modus_tollens("It is raining", "The ground is wet"))  # True
  print(modus_tollens("I am in France", "I speak French"))  # False
