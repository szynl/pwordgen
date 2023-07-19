import secrets
import random
import string

VALID_CHARS = ""
LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = string.punctuation

VALID_CHARS = LETTERS + DIGITS + SYMBOLS

def generate_password():
    '''
    Generates a random password of length 8-32 characters.
    '''
    print("\nGenerating password...\n")
    length = random.randint(8, 32)
    password = ""
    for i in range(length):
        password += "".join(secrets.choice(VALID_CHARS))
    print(f"Your password is {password}\n")

if __name__ == "__main__":
    generate_password()
