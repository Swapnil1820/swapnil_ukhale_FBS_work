# Write a program to find sum of digits using recursion.

def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits(num // 10)


num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits of", num, "is:", result)
