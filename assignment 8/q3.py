# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# Function for series a: 1 + 2 + 3 + ... + n
def sum_of_natural(n):
    return n * (n + 1) // 2   # formula for sum of first n natural numbers


# Function for factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


# Function for series b: 1! + 2! + 3! + ... + n!
def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total


# Function for series c: 1^1 + 2^2 + 3^3 + ... + n^n
def sum_of_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total


# Main program
n = int(input("Enter the value of n: "))

print("a. Sum of 1 + 2 + ... + n =", sum_of_natural(n))
print("b. Sum of 1! + 2! + ... + n! =", sum_of_factorials(n))
print("c. Sum of 1^1 + 2^2 + ... + n^n =", sum_of_powers(n))
