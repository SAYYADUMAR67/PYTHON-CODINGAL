import random
import secrets
import string
 
 
def generate_secure_password(
    length=16, use_uppercase=True, use_numbers=True, use_special=True
):
    """Generates a highly secure, customizable random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
 
    character_pool = string.ascii_uppercase
    password_elements = [secrets.choice(string.ascii_lowercase)]
 
    if use_uppercase:
        character_pool += string.ascii_uppercase
        password_elements.append(secrets.choice(string.ascii_uppercase))
 
    if use_numbers:
        character_pool += string.digits
        password_elements.append(secrets.choice(string.digits))
 
    if use_special:
        special_chars = "!@#$%^&*()-_=+[{]};:,.<>/?"
        character_pool += special_chars
        password_elements.append(secrets.choice(special_chars))
 
    remaining_length = length - len(password_elements)
 
    if remaining_length < 0:
        raise ValueError(
            "Length is too short for the selected character requirements."
        )
 
    password_elements += [
        secrets.choice(character_pool) for _ in range(remaining_length)
    ]
 
    secure_shuffler = random.SystemRandom()
    secure_shuffler.shuffle(password_elements)
 
    return "".join(password_elements)
 
 
def main():
    print("--- Advanced Password Generator ---")
    try:
        length = int(input("Enter password length (default 16): ") or 16)
        incl_upper = (
            input("Include uppercase letters? (y/n, default y): ").lower()
            != "n"
        )
        incl_num = input("Include numbers? (y/n, default y): ").lower() != "n"
        incl_spec = (
            input("Include special characters? (y/n, default y): ").lower()
            != "n"
        )
 
        password = generate_secure_password(
            length, incl_upper, incl_num, incl_spec
        )
        print(f"\nYour Secure Password: {password}\n")
 
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number for length.")
 
 
if __name__ == "__main__":
    main()