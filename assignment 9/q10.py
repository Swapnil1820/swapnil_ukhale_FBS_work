# Write a program to reverse a number using recursion.

def reverse_number(num, rev=0):
    if num == 0:
        return rev
    else:
        digit = num % 10
        rev = rev * 10 + digit
        return reverse_number(num // 10, rev)


num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)
