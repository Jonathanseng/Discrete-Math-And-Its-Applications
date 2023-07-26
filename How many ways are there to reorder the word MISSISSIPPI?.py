def permutations_with_repeating_elements(word):
  """Returns the number of permutations of the letters in word, where letters can repeat."""
  n = len(word)
  if n == 0:
    return 1
  else:
    return n * permutations_with_repeating_elements(word[1:])

def main():
  """Prints the number of ways to reorder the word MISSISSIPPI."""
  word = "MISSISSIPPI"
  print("Number of ways to reorder the word MISSISSIPPI:", permutations_with_repeating_elements(word))

if __name__ == "__main__":
  main()
