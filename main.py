import random
import string

# Function to generate a password
def generate_password(length):
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))  # Randomly select characters

# Prompt the user for the password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 6:
        print("Password length should be at least 6 characters for security.")
    else:
        print(f"Generated password: {generate_password(length)}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")