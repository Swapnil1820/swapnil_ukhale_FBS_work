n = 5  

for i in range(1, n+1):
    # print spaces to center the numbers
    print(" " * (n - i), end="")
    
    # ascending numbers
    for j in range(i, 2*i):
        print(j, end="")
    
    # descending numbers
    for j in range(2*i - 2, i-1, -1):
        print(j, end="")
    
    print()  # new line
