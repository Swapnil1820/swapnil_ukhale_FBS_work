# Sum of all odd numbers between 1 to n 

def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):   # step = 2 → takes only odd numbers
        total += i
    return total

n = int(input("Enter the value of n: "))
print("Sum of odd numbers from 1 to", n, "=", sum_of_odds(n))