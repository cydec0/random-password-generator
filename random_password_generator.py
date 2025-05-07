import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
  
  # Define the character sets to use.
  chars = string.ascii_letters  # always use letters
  if use_digits:
    chars += string.digits # add digits
  if use_special_chars:
    chars += string.punctuation # add special characters

  # Generate the password.
  password = ''.join(random.choice(chars) for _ in range(length))
  return password

def main():
  print("---RANDOM PASSWORD GENERATOR---")
  while True:
    try:
      length = int(input("Enter the desired password length: "))
      if length <= 0:
        print("Password length must be a positive integer.")
        continue  # Go back to the beginning of the loop
      break # Exit the loop if the input is valid
    except ValueError:
      print("Invalid input. Please enter an integer.")

  use_digits = input("Include digits? (y/n): ").lower() == 'y'
  use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

  try:
    password = generate_password(length, use_digits, use_special_chars)
    print(f"Generated password: {password}")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
