def is_empty_set(set):
  """Returns True if the set is empty, False otherwise."""
  return len(set) == 0

def is_vacuously_true(statement):
  """Returns True if the statement is vacuously true, False otherwise."""
  hypothesis = statement.split("if")[0]
  consequent = statement.split("if")[1]
  return is_empty_set(hypothesis) and consequent == "true"

def main():
  empty_set = set()
  print(is_empty_set(empty_set))  # True
  print(is_vacuously_true("if there are no dogs in the room, then all dogs in the room are brown"))  # True

if __name__ == "__main__":
  main()
