# WAP to check if a given number is prime number or not.

n=int(input('enter number :'))

if (n>1):
    for i in range(2,n):
        if(n%i==0):
            print('it is not a prime number')
            break
    else:
        print('prime number')
else:
    print('invalid number')