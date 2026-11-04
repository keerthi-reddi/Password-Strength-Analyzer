
# PASSWORD STRENGTH ANALYZER
# Developed using Python

# Step 1: Get password input
password = input("Enter a dummy password: ")

# Step 2: Check password length
length = len(password)

# Step 3: Check character types
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

# Step 4: Check common passwords
common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "letmein",
    "password123"
]

is_common = password.lower() in common_passwords

# Step 5: Calculate password score
score = 0

if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

# Step 6: Determine password strength
if is_common:
    strength = "Very Weak"
elif length < 8:
    strength = "Very Weak"
elif score <= 2:
    strength = "Weak"
elif score == 3:
    strength = "Moderate"
elif score == 4:
    strength = "Strong"
else:
    strength = "Very Strong"

# Step 7: Generate security suggestions
suggestions = []

if length < 12:
    suggestions.append("Use at least 12 characters.")

if not has_upper:
    suggestions.append("Add uppercase letters.")

if not has_lower:
    suggestions.append("Add lowercase letters.")

if not has_digit:
    suggestions.append("Add numbers.")

if not has_special:
    suggestions.append("Add special characters.")

if is_common:
    suggestions.append("Avoid commonly used passwords.")

# Step 8: Display analysis report
print("\n===== PASSWORD ANALYSIS REPORT =====")
print("Password Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Numbers:", has_digit)
print("Special Characters:", has_special)
print("Common Password:", is_common)
print("Password Score:", score, "/ 5")
print("Password Strength:", strength)

print("\n===== SECURITY SUGGESTIONS =====")

if suggestions:
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("No basic improvement suggestions.")

print("\n===== ANALYSIS COMPLETED =====")
