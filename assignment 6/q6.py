rows=6
for i in range(rows):
    print(' ' * (rows-i), end='')

    for j in range(1,2*i):
        print(j,end='')
    print()