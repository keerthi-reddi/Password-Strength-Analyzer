# PROJECT REPORT
## Password Strength Analyzer Using Python

### 1. Introduction
Password Strength Analyzer is a simple Python-based cybersecurity project developed to evaluate the strength of user-entered passwords. It checks password length, uppercase letters, lowercase letters, numbers, special characters, and commonly used passwords.

### 2. Aim
To develop a Python program that analyzes password strength and provides basic security suggestions.

### 3. Objectives
- To check password length.
- To identify uppercase and lowercase letters.
- To detect numbers and special characters.
- To identify selected commonly used passwords.
- To calculate a basic password strength score.
- To provide suggestions for improving password security.

### 4. Tools and Technologies
- Programming Language: Python 3
- Code Editor: Visual Studio Code
- Operating System: Windows 11

### 5. Methodology
1. The program accepts a dummy password as input.
2. It calculates the password length.
3. It checks uppercase, lowercase, numeric and special characters.
4. It compares the password against a predefined list of common passwords.
5. It calculates a score based on five conditions.
6. It classifies the password strength.
7. It displays security suggestions.

### 6. Testing and Results

| Test Password | Expected Strength |
|---|---|
| admin | Very Weak |
| hello | Very Weak |
| hello123 | Moderate |
| Hello@123 | Very Strong |

The program produced the expected results for all four test cases.

### 7. Result
The Password Strength Analyzer was successfully developed and executed using Python. It evaluates basic password characteristics and displays a strength classification with improvement suggestions.

### 8. Limitations
- The common-password list contains only a few predefined examples.
- The scoring method is a basic educational approach, not an official password-security standard.
- It does not check passwords against leaked-password databases.
- It does not perform advanced password entropy analysis.

### 9. Conclusion
This project demonstrates the use of Python programming concepts such as conditional statements, loops, lists, string methods and logical operations in a basic cybersecurity application.

### 10. Disclaimer
This project is developed for educational purposes. Only dummy passwords should be used during testing. The program does not store or transmit passwords.
