def generalization(premises, conclusion):
  """Returns True if the argument is a valid generalization argument, False otherwise."""
  if all(premises) and conclusion:
    return True
  else:
    return False

def specialization(premises, conclusion):
  """Returns True if the argument is a valid specialization argument, False otherwise."""
  if conclusion and all(premises):
    return True
  else:
    return False

def contradiction(premises, conclusion):
  """Returns True if the argument is a valid contradiction argument, False otherwise."""
  if premises and not conclusion:
    return True
  elif not premises and conclusion:
    return True
  else:
    return False

if __name__ == "__main__":
  print(generalization(["All dogs I have met are friendly", "This dog is friendly"], "All dogs are friendly"))  # True
  print(generalization(["All dogs I have met are friendly", "This dog is not friendly"], "All dogs are friendly"))  # False
  print(specialization(["All mammals have four legs", "This animal has four legs"], "This animal is a mammal"))  # True
  print(specialization(["All mammals have four legs", "This animal does not have four legs"], "This animal is a mammal"))  # False
  print(contradiction(["The cat is on the mat", "The cat is not on the mat"], "One of these statements must be false"))  # True
  print(contradiction(["The cat is on the mat", "The cat is on the floor"], "One of these statements must be false"))  # False
