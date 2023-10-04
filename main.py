# Password Generator

# Import the 'random' module for generating random elements
import random

# Define lists of characters to use in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print a welcome message
print("Welcome to the PyPassword Generator!")

# Prompt the user for input
num_letters = int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to store the password characters
password_list = []

# Generate random letters and append them to the password_list based on user input
for char in range(1, num_letters + 1):
  password_list.append(random.choice(letters))

# Generate random symbols and append them to the password_list based on user input
for char in range(1, num_symbols + 1):
  password_list += random.choice(symbols)

# Generate random numbers and append them to the password_list based on user input
for char in range(1, num_numbers + 1):
  password_list += random.choice(numbers)

# Print the password_list before shuffling it
print(password_list)

# Shuffle the password_list to randomize the order of characters
random.shuffle(password_list)

# Initialize an empty string to store the final password
password = ""

# Create the final password by concatenating the characters in password_list
for char in password_list:
  password += char

# Print the final generated password
print(f"Your password is: {password}")
