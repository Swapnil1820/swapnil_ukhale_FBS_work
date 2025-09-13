# Write a program to find sum of digits of a number

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10   # extract last digit
        num //= 10          # remove last digit
    return total

n = int(input("Enter a number: "))
print("Sum of digits of", n, "=", sum_of_digits(n))
