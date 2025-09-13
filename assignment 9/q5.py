# Write a program to find factorial using recursion.

def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
result = factorial(n)
print("Factorial of", n, "is:", result)
