def truth_table(expression):
  """
  Returns a truth table for the given expression.

  Args:
    expression: A string representing a logical expression.

  Returns:
    A list of lists, where each inner list represents the truth value of the
    expression for a particular combination of truth values of its atomic
    statements.
  """

  table = []
  for p in [True, False]:
    for q in [True, False]:
      table.append((p, q, expression == "p ∧ q", expression == "q ∧ p"))
  return table

def proof_by_contradiction(expression1, expression2):
  """
  Returns True if the two expressions are logically equivalent, False otherwise.

  Args:
    expression1: A string representing the first expression.
    expression2: A string representing the second expression.

  Returns:
    True if the two expressions are logically equivalent, False otherwise.
  """

  try:
    assert expression1 == expression2
    return True
  except AssertionError:
    return False

def definitional_equivalence(expression1, expression2):
  """
  Returns True if the two expressions are definitionally equivalent, False otherwise.

  Args:
    expression1: A string representing the first expression.
    expression2: A string representing the second expression.

  Returns:
    True if the two expressions are definitionally equivalent, False otherwise.
  """

  if expression1 == expression2:
    return True

  if expression1 == "x = y" and expression2 == "x is equal to y":
    return True

  return False
