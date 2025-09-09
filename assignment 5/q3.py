# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost of ticket: "))

total_amount = 0

for i in range(1, n+1):
    age = int(input(f"Enter age of passenger {i}: "))
    if age < 12:
        price = ticket_cost * 0.7   # 30% discount
    elif age > 59:
        price = ticket_cost * 0.5   # 50% discount
    else:
        price = ticket_cost         # full price
    print(f"Passenger {i} ticket price: {price}")
    total_amount += price

print("Total Amount to be paid:", total_amount)
