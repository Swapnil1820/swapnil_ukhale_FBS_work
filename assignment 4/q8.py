# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n=int(input('enter starting number :'))
n2=int(input('enter end number :'))

for i in range(n,n2+1):
    if(i%7==0 and i%5==0 ):
        print(i,end=' ')