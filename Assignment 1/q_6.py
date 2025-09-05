# Write a Program to input two angles from user and find third angle of the triangle.

a1=int(input('enter first angle :'))
a2=int(input('enter second angle :'))

#to calculate third angle
a3=180-(a1+a2)
print('the third angle is :',a3)