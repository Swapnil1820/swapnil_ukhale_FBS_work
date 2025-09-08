# WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
divisor = int(input("Enter the divisor: "))

for i in range(start,end+1):
    if(i%divisor==0):
        print(i,end=' ')
        