# Write a program to check whether a number is prime or not using recursion.

def is_prime(num, divisor=2):
    if num <= 1:
        return False
    if divisor * divisor > num:   # If divisor exceeds sqrt(num), it's prime
        return True
    if num % divisor == 0:
        return False
    return is_prime(num, divisor + 1)


num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime number.")
else:
    print(num, "is NOT a Prime number.")
