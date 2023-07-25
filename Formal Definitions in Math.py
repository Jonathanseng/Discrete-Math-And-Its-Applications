def is_natural_number(x):
  """Returns True if x is a natural number, False otherwise."""

  if x < 0:
    return False
  elif x == 0:
    return True
  else:
    return is_natural_number(x - 1)


def is_real_number(x):
  """Returns True if x is a real number, False otherwise."""

  try:
    float(x)
    return True
  except ValueError:
    return False


def is_function(f):
  """Returns True if f is a function, False otherwise."""

  if not callable(f):
    return False
  else:
    return True


def is_set(s):
  """Returns True if s is a set, False otherwise."""

  if isinstance(s, set):
    return True
  else:
    return False


def main():
  print("1 is a natural number:", is_natural_number(1))
  print("0 is a natural number:", is_natural_number(0))
  print("-1 is a natural number:", is_natural_number(-1))

  print("1.0 is a real number:", is_real_number(1.0))
  print("1 is a real number:", is_real_number(1))
  print("'hello' is a real number:", is_real_number('hello'))

  print("f(x) = x^2 is a function:", is_function(lambda x: x**2))
  print("f(x) = 'hello' is a function:", is_function(lambda x: 'hello'))

  print("{1, 2, 3} is a set:", is_set({1, 2, 3}))
  print("[1, 2, 3] is a set:", is_set([1, 2, 3]))


if __name__ == "__main__":
  main()
