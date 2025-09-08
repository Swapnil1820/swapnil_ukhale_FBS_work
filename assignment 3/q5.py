# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=float(input('enter angle-'))
b=float(input('enter angle-'))
c=float(input('enter angle-'))

if(a==b==c):
    print('equilateral triangle')
elif(a==b or b==c or a==c):
    print('isosceles triangle')
else:
    print('scalene triangle')