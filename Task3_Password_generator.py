import string
import random

available_characters = string.ascii_letters + string.digits + string.punctuation

while True:
    password_length = input("Enter the password length (should be between 8 to 50): ")
    try:
        password_length = int(password_length)
    except ValueError:
        print("Invalid input, only numbers are accepted. Please try again")
    else:
        if 8 <= password_length <= 50:
            break
        print("Invalid input, the password length should be between 8 and 50: ")

generated_password = "".join([random.choice(available_characters) for i in range(password_length)])

print(f"\nYour generated password is: {generated_password}")