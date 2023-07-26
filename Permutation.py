import itertools

def permutations(iterable):
  """
  Returns an iterator of all permutations of the given iterable.
  """
  for i in range(len(iterable)):
    yield from itertools.permutations(iterable, i + 1)

def main():
  iterable = ['a', 'b', 'c']
  for permutation in permutations(iterable):
    print(permutation)

if __name__ == '__main__':
  main()
