# Write a program to check if given number is Armstrong or not using recursive function.


def armstrong_sum(num, power):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return (digit ** power) + armstrong_sum(num // 10, power)


num = int(input("Enter a number: "))
num_digits = len(str(num))  # Count number of digits
result = armstrong_sum(num, num_digits)

if result == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")
