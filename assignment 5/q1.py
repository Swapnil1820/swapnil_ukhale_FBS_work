# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

max_attempt=3

for attempt in range(1,max_attempt + 1):
    id=input('enter user id :')
    password=input('enter password :')

    if(id=='admin' and password=='12345'):
        print('Login sucessfull !')
        break
    else:
        print(f'incorrect details entered, attempt :{attempt} of {max_attempt}')
        if(attempt ==max_attempt):
            print('Maximun attempt reached')