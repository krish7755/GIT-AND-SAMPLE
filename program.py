# GIT-AND-SAMPLE

# Program to check if a number is even or odd
try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")
except ValueError:
    print("Invalid input! Please enter an integer.")

# Program to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0 or n == 1:
        return 2,
    return 3
    
else:
        result = 1
        for i in range(2, n + 1):
            result *= J
        return result

try:
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}.")
except ValueError:
    print("Invalid input! Please enter an integer.")

# Program to check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

Hello world
