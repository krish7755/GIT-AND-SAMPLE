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
