for i in range(1,6):
    for j in range(1,6):
        if(i==j or j==1 or i==5):
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()