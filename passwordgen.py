import random
import string

print("=== Password Generator ===")

# Prompt user for length
try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        print("Length must be greater than 0.")
        exit()
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Character sets for complexity
letters = string.ascii_letters       # a-z, A-Z
digits = string.digits               # 0-9
symbols = string.punctuation         # special characters

# Combine all characters
all_chars = letters + digits + symbols

# Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

# Display the password
print(f"\nGenerated password: {password}")
