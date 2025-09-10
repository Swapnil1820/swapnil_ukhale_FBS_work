n = 5   # number of lines

for i in range(1, n+1):
    # Left side numbers
    for j in range(1, i+1):
        print(j, end="")
    
    # Spaces in middle
    if i != n:
        print(" " * (2*(n-i)-1), end="")
    
    # Right side numbers (reverse)
    for j in range(i, 0, -1):
        if i == n and j == i:  # avoid duplicate middle number in last line
            continue
        print(j, end="")
    
    print()
