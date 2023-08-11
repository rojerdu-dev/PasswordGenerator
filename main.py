import random
import secrets
import string
import pyfiglet


def get_password_length() -> int:
    password_length = int(input("Enter password length: "))
    return password_length


def get_minimum_upper() -> int:
    minimum_upper = int(input("Enter minimum upper case characters: "))
    return minimum_upper


def get_minimum_lower() -> int:
    minimum_lower = int(input("Enter minimum lower case characters: "))
    return minimum_lower


def get_minimum_numeric_characters() -> int:
    minimum_numeric_characters = int(input("Enter minimum numeric characters: "))
    return minimum_numeric_characters


def get_minimum_special_characters() -> int:
    minimum_special_characters = int(input("Enter minimum special characters: "))
    return minimum_special_characters


def generate_password(
    password_legnth: int,
    minimum_upper: int,
    mininum_lower: int,
    minimum_digits: int,
    minimum_special_characters: int,
) -> str:
    # imported from string module
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numerics = string.digits
    special = string.punctuation
    all_characters = lower + upper + numerics + special

    password = ""

    for char in range(minimum_upper):
        password += "".join(random.choice(secrets.choice(upper)))

    for char in range(mininum_lower):
        password += "".join(random.choice(secrets.choice(lower)))

    for char in range(minimum_digits):
        password += "".join(random.choice(secrets.choice(numerics)))

    for char in range(minimum_special_characters):
        password += "".join(random.choice(secrets.choice(special)))

    remaining = (
        password_legnth
        - minimum_upper
        - mininum_lower
        - minimum_digits
        - minimum_special_characters
    )

    for char in range(remaining):
        password += "".join(random.choice(secrets.choice(all_characters)))

    return password


def main() -> None:
    length = get_password_length()
    uppercase = get_minimum_upper()
    lowercase = get_minimum_lower()
    numerical = get_minimum_numeric_characters()
    special_chars = get_minimum_special_characters()

    password = generate_password(length, uppercase, lowercase, numerical, special_chars)

    # Shuffle password
    password_list = list(password)
    random.shuffle(password_list)
    print("".join(password_list))


if __name__ == "__main__":
    intro = pyfiglet.figlet_format("Password Generator")
    print(intro)
    main()
