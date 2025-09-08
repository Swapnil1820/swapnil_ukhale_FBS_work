# Write a program to input all sides of a triangle and check whether triangle is valid or not.

a=int(input('enter first angle -'))
b=int(input('enter second angle -'))
c=int(input('enter third angle -'))

if((a+b>c )and(a+c>b)and(b+c>a)):
    print('the triange is valid')
else:
    print('invalid triangle')