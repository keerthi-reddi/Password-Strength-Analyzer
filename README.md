PASSWORD STRENGTH ANALYZER USING PYTHON

1. Project Introduction
Password Strength Analyzer is a basic cybersecurity project developed using Python programming language.
The main purpose of this project is to analyze a user-entered password and identify its basic strength based on different password characteristics.
The program checks:
Password length
Uppercase letters
Lowercase letters
Numeric digits
Special characters
Commonly used passwords
After analyzing these conditions, the program calculates a password score, classifies its strength and provides security suggestions.

Project Type: Cybersecurity / Python Programming
Programming Language: Python 3
Code Editor: Visual Studio Code
Operating System: Windows 11

2. Aim of the Project
To develop a Python-based application that evaluates basic password characteristics, identifies weak passwords and provides suggestions to improve password security.

3. Objectives
Accept password input from the user.
Calculate the password length.
Identify uppercase and lowercase characters.
Check for numeric digits.
Detect special characters.
Identify selected common passwords.
Calculate a password strength score.
Classify passwords into different strength levels.
Generate security improvement suggestions.

5. Software and Tools Used
Tool
Purpose
Python 3
Programming language
Visual Studio Code
Writing and executing Python code
Windows 11
Operating system
VS Code Terminal
Running the program
GitHub

Project storage and submission
GitHub README
Project documentation

5. Python Concepts and Functions Used
5.1 input()
Accepts input from the user.
Example:
password = input("Enter a dummy password: ")
Explanation: The user enters a password, and Python stores it in the variable named password.

5.2 len()
Calculates the total number of characters in a password.
Example:
length = len(password)

5.3 any()
Checks whether at least one character satisfies a particular condition.
Example:
has_upper = any(char.isupper() for char in password)

5.4 isupper()
Checks whether a character is an uppercase letter.
Example:
char.isupper()

5.5 islower()
Checks whether a character is a lowercase letter.
Example:
char.islower()

5.6 isdigit()
Checks whether a character is a numeric digit.
Example:
char.isdigit()

5.7 isalnum()
Checks whether a character is an alphabet or a number.
Example:
char.isalnum()
In this project, it is used with not to identify special characters.

5.8 Variables
Variables store information used by the program.
Variables used:
password
length
has_upper
has_lower
has_digit
has_special
is_common
score
strength
suggestions

5.9 Lists
Lists store multiple values.
Example:
common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "letmein",
    "password123"
]

5.10 lower()
Converts a string into lowercase.
Example:
password.lower()
It helps compare passwords without considering uppercase and lowercase differences.

5.11 if, elif and else
Conditional statements are used to make decisions based on password characteristics.
They determine whether a password is Very Weak, Weak, Moderate, Strong or Very Strong.

5.12 append()
Adds a new item to a list.
Example:
suggestions.append("Add uppercase letters.")

5.13 for loop
Repeats an operation for each item in a list.
Example:
for suggestion in suggestions:
    print("-", suggestion)

5.14 print()
Displays the analysis report and security suggestions on the terminal.

5.15 Boolean Values
Boolean values are:
True
False
They indicate whether a password satisfies a particular condition.

6. Complete Python Source Code
File name: password_analyzer.py

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

7. Working Methodology
The project works in eight steps.
Input: Accepts a dummy password from the user.
Length checking: Calculates the number of characters.
Character checking: Checks uppercase, lowercase, numbers and special characters.
Common password checking: Compares the entered password with a predefined list.
Score calculation: Awards one point for each of five conditions.
Strength classification: Assigns a password strength category.
Security suggestions: Identifies missing password characteristics.
Output: Displays the complete analysis report.

9. Password Scoring System
The project uses a custom scoring system with a maximum score of 5.
Condition
Points
Length is at least 8 characters
1
Contains uppercase letters
1
Contains lowercase letters
1
Contains numbers
1
Contains special characters
1
Maximum Score
5
Password Strength Classification
Condition
Strength
Common password
Very Weak
Length below 8
Very Weak
Score 0–2 (when length is at least 8)
Weak
Score 3
Moderate
Score 4
Strong
Score 5
Very Strong
Note: Common-password and length conditions are checked before the score-based classification.

9. Test Cases and Password Analysis
Four dummy passwords were used to test the program.
Test Case 1: admin
Password: admin
Length: 5
Uppercase: False
Lowercase: True
Numbers: False
Special Characters: False
Common Password: True
Score: 1/5
Strength: Very Weak
Reason: The password is short and appears in the predefined common-password list.

Test Case 2: hello
Password: hello
Length: 5
Uppercase: False
Lowercase: True
Numbers: False
Special Characters: False
Common Password: False
Score: 1/5
Strength: Very Weak
Reason: It does not meet the minimum 8-character scoring condition and lacks other character types.

Test Case 3: hello123
Password: hello123
Length: 8
Uppercase: False
Lowercase: True
Numbers: True
Special Characters: False
Common Password: False
Score: 3/5
Strength: Moderate
Reason: It meets the length requirement and contains lowercase letters and numbers.

Test Case 4: Hello@123
Password: Hello@123
Length: 9
Uppercase: True
Lowercase: True
Numbers: True
Special Characters: True
Common Password: False
Score: 5/5
Strength: Very Strong
Reason: It satisfies all five scoring conditions.
Note: The program still recommends at least 12 characters because its suggestion threshold is 12, even though the scoring threshold is 8.

10. Security Suggestions Generated
The program provides suggestions based on missing conditions.
Examples:
Use at least 12 characters.
Add uppercase letters.
Add lowercase letters.
Add numbers.
Add special characters.
Avoid commonly used passwords.

12. How to Execute the Project
Requirements:
Python 3 installed.
Visual Studio Code installed.
Steps:
Open Visual Studio Code.
Open the project folder.
Open password_analyzer.py.
Open the integrated terminal.
Execute the following command:
python password_analyzer.py
Enter a dummy password.
Press Enter.
Observe the password analysis report.

12. Project Folder Structure
Password_Analyzer_Final/
│
├── password_analyzer.py
├── README.md
├── PROJECT_REPORT.md
│
└── screenshots/
    ├── 01_admin.png
    ├── 02_hello.png
    ├── 03_hello123.png
    └── 04_Hello123.png
    
14. Limitations
The project uses a small predefined list of common passwords.
It does not check passwords against leaked-password databases.
It does not calculate formal password entropy.
It uses a basic custom scoring method.
It does not provide protection against all password attacks.

14. Future Enhancements
Expand the common-password database.
Add password entropy estimation.
Introduce a graphical user interface.
Add more password test cases.
Integrate secure password recommendaions.
Improve the scoring algorithm

15. Conclusion
The Password Strength Analyzer was successfully developed using Python.
The project demonstrates the application of basic Python programming concepts in cybersecurity. It evaluates password characteristics, identifies selected common passwords, calculates a strength score and generates security suggestions.
This project helped develop practical knowledge of Python programming, conditional statements, loops, lists, string methods and basic password-security concepts.

16. Disclaimer
This project is developed for educational purposes only.
The scoring system is a basic custom implementation and is not an official password-security standard. The program does not store or transmit passwords.
Only dummy passwords should be used during testing.
