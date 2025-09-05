#Write a program to enter P, T, R and calculate Compound Interest.

P = float(input("Enter the Principal amount: "))
R = float(input("Enter the annual interest Rate (%): "))
T = float(input("Enter the Time period in years: "))

amount=P*(1+R/100)
n=amount**T
CI=amount-P
print('The compound interest is :',CI)