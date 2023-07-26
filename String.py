def string_manipulation():
  """
  This function demonstrates some basic string manipulation operations.
  """

  string = "hello world"

  # Get the length of the string.
  length = len(string)
  print("The length of the string is:", length)

  # Get the first character of the string.
  first_character = string[0]
  print("The first character of the string is:", first_character)

  # Get the last character of the string.
  last_character = string[-1]
  print("The last character of the string is:", last_character)

  # Get the substring from the 2nd to the 5th character.
  substring = string[2:5]
  print("The substring from the 2nd to the 5th character is:", substring)

  # Check if the string contains the substring "world".
  contains_world = "world" in string
  print("The string contains the substring 'world':", contains_world)

  # Convert the string to uppercase.
  uppercase_string = string.upper()
  print("The uppercase string is:", uppercase_string)

  # Convert the string to lowercase.
  lowercase_string = string.lower()
  print("The lowercase string is:", lowercase_string)

if __name__ == "__main__":
  string_manipulation()
