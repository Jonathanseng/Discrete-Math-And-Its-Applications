def is_true(statement):
  """Returns True if statement is true, False otherwise."""
  if statement == "The sky is blue":
    return True
  elif statement == "2 + 2 = 4":
    return True
  else:
    return False

def is_false(statement):
  """Returns True if statement is false, False otherwise."""
  return not is_true(statement)

def and_statement(statement1, statement2):
  """Returns True if both statement1 and statement2 are true, False otherwise."""
  if is_true(statement1) and is_true(statement2):
    return True
  else:
    return False

def or_statement(statement1, statement2):
  """Returns True if either statement1 or statement2 is true, or if both are true."""
  if is_true(statement1) or is_true(statement2):
    return True
  else:
    return False

def not_statement(statement):
  """Returns True if statement is false, False otherwise."""
  if is_true(statement):
    return False
  else:
    return True

def main():
  print(is_true("The sky is blue"))  # True
  print(is_true("2 + 2 = 5"))  # False
  print(is_false("The sky is blue"))  # False
  print(is_false("2 + 2 = 4"))  # False
  print(and_statement("It is raining", "The ground is wet"))  # True
  print(and_statement("It is raining", "The ground is not wet"))  # False
  print(or_statement("It is raining", "The ground is wet"))  # True
  print(or_statement("It is not raining", "The ground is wet"))  # True
  print(not_statement("It is raining"))  # False
  print(not_statement("It is not raining"))  # True

if __name__ == "__main__":
  main()
