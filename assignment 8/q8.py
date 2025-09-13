#Write a program find reverse of a number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10        # get last digit
        rev = rev * 10 + digit  # add digit to reverse
        num //= 10              # remove last digit
    return rev

n = int(input("Enter a number: "))
print("Reverse of", n, "=", reverse_number(n))
