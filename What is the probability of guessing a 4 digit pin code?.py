def probability_of_guessing_pin(digits):
  """Returns the probability of guessing a 4-digit PIN code."""
  n = 10 ** digits
  return 1 / n

def main():
  """Prints the probability of guessing a 4-digit PIN code."""
  print("Probability of guessing a 4-digit PIN code:", probability_of_guessing_pin(4))

if __name__ == "__main__":
  main()
