# Write a program to prompt user to enter userid and password.
# After verifying  userid and password display a 4 digit random
# number and ask user to enter the same. If user enters the same
# number then show him success message otherwise failed. (Something like captcha)

import random

u = input("Enter UserID: ")
p = input("Enter Password: ")

if u == "admin" and p == "12345":
    c = random.randint(1000, 9999)
    print("Captcha:", c)
    if int(input("Enter Captcha: ")) == c:
        print("Login Successful!")
    else:
        print("Failed! Wrong Captcha.")
else:
    print("Invalid UserID or Password")
