# Program to Find the Roots of a Quadratic Equation

import cmath


a=float(input('enter value of a :'))
b=float(input(' enter value of b :'))
c=float(input('enter value of c :'))

# calculating b square - 4ac
x=(b**2)-(4*a*c)

# now calculating the whole formula that is -b +- under root b square - 4ac divided by 2a
y=(-b+cmath.sqrt(x))/(2*a)
z=(-b-cmath.sqrt(x))/(2*a)

print("Root 1 =", y)
print("Root 2 =", z)