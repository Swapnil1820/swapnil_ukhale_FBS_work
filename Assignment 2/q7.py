# Find the sum of three-digit number.

a=int(input('enter three digit number'))

num1=a//100         #hundred place
num2=(a//10)%10     #tens place
num3=a%10           #ones place

sum=num1+num2+num3
print(f'the sum of three digit number is {sum}')


# num =456

# a=num%10
# num = num//10
# b=num%10
# num = num//10
# c=num%10
# num = num//10

# print(f'a : {a},b :{b},c :{c}')
# print(f"sum of the digit is {a+b+c}")