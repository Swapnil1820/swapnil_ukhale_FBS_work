# Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!

# Recursive function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Recursive function to calculate sum of factorial series
def sum_of_series(n):
    if n == 1:
        return factorial(1)
    else:
        return factorial(n) + sum_of_series(n - 1)

n = int(input("Enter the value of n: "))
result = sum_of_series(n)
print("Sum of series ", n, " =", result)
