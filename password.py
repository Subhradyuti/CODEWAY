import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        print("Error: Please choose at least one character set.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_punctuation)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
