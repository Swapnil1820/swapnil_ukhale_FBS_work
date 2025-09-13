# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

# Function to count number of digits
def count_digits(num):
    return len(str(num))


# Function to calculate sum of digits raised to power of count
def armstrong_sum(num):
    digits = count_digits(num)
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total

# Function to check if number is Armstrong
def is_armstrong(num):
    return num == armstrong_sum(num)


n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is NOT an Armstrong number")
