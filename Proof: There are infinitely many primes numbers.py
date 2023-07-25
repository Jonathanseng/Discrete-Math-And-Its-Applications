def is_prime(number):
  """Returns True if number is prime, False otherwise."""

  if number <= 1:
    return False

  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False

  return True


def main():
  """Prints the first 100 prime numbers."""

  primes = []
  for i in range(2, 100):
    if is_prime(i):
      primes.append(i)

  print(primes)


if __name__ == "__main__":
  main()
