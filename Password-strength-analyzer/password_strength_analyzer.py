import re

def password_strength(password):
    # Initialize strength variables
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[@$!%*?&]', password))

    # Calculate strength
    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Determine strength level
    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

def main():
    print("Password Strength Analyzer")
    password = input("Enter a password to analyze: ")
    strength = password_strength(password)
    print(f"The strength of the password is: {strength}")

if __name__ == "__main__":
    main()
