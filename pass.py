import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = 12 
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
