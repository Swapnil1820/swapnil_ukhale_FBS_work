#Program to find quotient and remainder of two numbers.

divisor=int(input('enter value of 1'))
dividend=int(input('enter value of 2'))

quotient=divisor//dividend
print(f'quotient is {quotient}')

reminder=divisor%dividend
print('reminder is',reminder)