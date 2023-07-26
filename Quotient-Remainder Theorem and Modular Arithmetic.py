def quotient_remainder(dividend, divisor):
  """Returns the quotient and remainder of the division of dividend by divisor."""

  q = dividend // divisor
  r = dividend % divisor
  return q, r


def main():
  dividend = 1234
  divisor = 100
  q, r = quotient_remainder(dividend, divisor)
  print(f"The quotient is {q} and the remainder is {r}.")


if __name__ == "__main__":
  main()
