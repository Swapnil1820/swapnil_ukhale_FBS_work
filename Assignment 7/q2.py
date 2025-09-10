n = 5  # maximum stars in the middle

# increasing part
for i in range(1, n + 1):
    print("*" * i)

# decreasing part
for i in range(n - 1, 0, -1):
    print("*" * i)