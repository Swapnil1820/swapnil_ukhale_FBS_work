#Write a program to find sum of n numbers using recursion.

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

n = int(input("Enter a number: "))
result = sum_n(n)
print("Sum of first", n, "numbers is:", result)
