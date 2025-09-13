# Write a program to reverse a given number using recursive function.

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    else:
        digit = num % 10
        rev = rev * 10 + digit
        return reverse_num(num // 10, rev)

num = int(input("Enter a number: "))
result = reverse_num(num)
print("Reversed number:", result)
