#Write a program to calculate the percentage of student based on marks of any 5 subjects.
s1=int(input('enter first subject marks'))
s2=int(input('enter second subject marks'))
s3=int(input('enter third subject marks'))
s4=int(input('enter fourth subject marks'))
s5=int(input('enter fifth subject marks'))

marks=s1+s2+s3+s4+s5
per=marks/5
print(f'marks is : {marks}, and percentage is {per}')