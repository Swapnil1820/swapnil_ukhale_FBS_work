# Write a program to convert days into years, weeks and days.

days=int(input('enter days :'))

#calculating years
years=days//360
print('years is :',years)

# calculating weeks
rem=days%365
weeks=rem//7
print("weeks is :",weeks)

#remaining days
days_left=rem%7
print("remaining days is :",days_left)
