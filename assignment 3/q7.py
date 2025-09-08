# Write a program to check if user has entered correct userid and password.

id=input('enter user id -')
pas=input('enter password -')
if(id=='admin' and pas=='me1234'):
    print('Login sucessfull')
else:
    print('Login error')