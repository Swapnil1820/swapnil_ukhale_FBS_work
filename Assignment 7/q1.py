for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')

    for j in range(1,i+1):
        if(i==j or j==1):
            print('*',end=' ')# 3 space in end ' ' to align in triangle
        else:
            print(' ',end=' ')
    print()

for i in range(1,6):
    for j in range(1,i):
        print(' ',end='')
    
    for j in range(1,7-i):
        if(j==1 or i+j==6):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()