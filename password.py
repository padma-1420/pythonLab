def is_valid_password(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    is_long_enough = len(password) >= 8

    return has_upper and has_lower and has_digit and is_long_enough
password = input("Enter your password: ")
if is_valid_password(password):
    print("✅ Password is valid.")
else:
    print("❌ Password is invalid. It must contain at least:")
    print("- 1 uppercase letter")
    print("- 1 lowercase letter")
    print("- 1 digit")
    print("- Minimum 8 characters")
