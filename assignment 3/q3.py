# Write a program to input angles of a triangle and check whether triangle is valid or not.

a=int(input('enter first angle -'))
b=int(input('enter second angle -'))
c=int(input('enter third angle -'))

if(a+b+c==180 and a>0 and b>0 and c>0):
    print('the triange is valid')
else:
    print('invalid triangle')