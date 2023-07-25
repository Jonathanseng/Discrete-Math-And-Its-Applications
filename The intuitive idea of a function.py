def square(x):
  """Returns the square of x."""
  return x * x

def length(word):
  """Returns the length of word."""
  return len(word)

def mean(numbers):
  """Returns the mean of numbers."""
  sum = 0
  for number in numbers:
    sum += number
  return sum / len(numbers)

def main():
  print(square(2))  # 4
  print(length("hello"))  # 5
  print(mean([1, 2, 3, 4, 5]))  # 3

if __name__ == "__main__":
  main()
