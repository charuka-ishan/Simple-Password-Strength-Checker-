from getpass import getpass

print("""
╔══════════════════════════════════════╗
║      PASSWORD STRENGTH CHECKER       ║
╚══════════════════════════════════════╝

-------------------------
Checks:
- Length >= 12
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
""")

password = getpass("Enter your password: ")

special_chars = "!@$%^&*()_-"
numbers = "0123456789"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

issues = []

if len(password) < 12:
    issues.append("Password must be at least 12 characters")

if not any(char in special_chars for char in password):
    issues.append("Add special characters")

if not any(char in numbers for char in password):
    issues.append("Add numbers")

if not any(char in upper for char in password):
    issues.append("Add uppercase letters")

if not any(char in lower for char in password):
    issues.append("Add lowercase letters")

if not issues:
    print("\n Your password is strong")
else:
    print("\n Weak password:")
    for problem in issues:
        print("-", problem)
