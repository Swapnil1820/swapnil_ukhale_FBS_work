n = 5   # number of lines

for i in range(1, n+1):
    # Spaces before numbers
    print(" " * (n - i), end="")

    # Left side numbers
    for j in range(1, i+1):
        print(j, end="")

    # Right side numbers
    for j in range(i-1, 0, -1):
        print(j, end="")

    print()
