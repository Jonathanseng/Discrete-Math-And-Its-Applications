def if_p_then_q(p, q):
  """
  Returns True if the conditional statement "if p then q" is true, False otherwise.

  Args:
    p: A boolean expression.
    q: A boolean expression.

  Returns:
    True if the conditional statement is true, False otherwise.
  """

  if p:
    return q
  else:
    return False

def main():
  print(if_p_then_q(True, True))  # True
  print(if_p_then_q(False, True))  # False
  print(if_p_then_q(True, False))  # False

if __name__ == "__main__":
  main()
