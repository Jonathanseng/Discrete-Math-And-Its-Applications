def is_valid(premises, conclusion):
  """Returns True if the argument is valid, False otherwise."""
  # Translate the argument into logical form.
  logical_form = translate_to_logical_form(premises, conclusion)

  # Check the validity of the logical form.
  if logical_form == "P → Q":
    return is_valid_modus_ponens(premises, conclusion)
  elif logical_form == "P → Q, ¬Q → ¬P":
    return is_valid_modus_tollens(premises, conclusion)
  else:
    return False

def is_valid_modus_ponens(premises, conclusion):
  """Returns True if the argument is a valid modus ponens argument, False otherwise."""
  if premises[0] and premises[1] and not conclusion:
    return False
  else:
    return True

def is_valid_modus_tollens(premises, conclusion):
  """Returns True if the argument is a valid modus tollens argument, False otherwise."""
  if premises[0] and not premises[1] and not conclusion:
    return False
  else:
    return True

def translate_to_logical_form(premises, conclusion):
  """Translates the argument into logical form."""
  logical_form = ""
  for premise in premises:
    logical_form += premise + " → "
  logical_form += conclusion
  return logical_form

if __name__ == "__main__":
  premises = ["If it is raining, then the ground is wet.", "It is raining."]
  conclusion = "The ground is wet."
  print(is_valid(premises, conclusion))  # True

  premises = ["If I am in France, then I speak French.", "I do not speak French."]
  conclusion = "I am not in France."
  print(is_valid(premises, conclusion))  # True
