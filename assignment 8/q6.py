# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacci(n):
    a, b = 1, 1   # first two terms
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b   # update values
    return series

n = int(input("Enter number of terms: "))
fib_series = fibonacci(n)

print("Fibonacci series up to", n, "terms:")
for num in fib_series:
    print(num, end=" ")
