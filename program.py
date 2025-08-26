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
        return 2
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

try:
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}.")
except ValueError:
    print("Invalid input! Please enter an integer.")
