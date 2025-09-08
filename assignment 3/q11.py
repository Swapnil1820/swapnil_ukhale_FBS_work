# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total=0
ticket=float(input('enter ticket price -'))

for i in range(1,6):
    age=int(input('enter age -'))

    if(age<12):
        amount=ticket*0.7
    elif(age>59):
        amount=ticket*0.5
    else:
        amount=ticket
    print('Ticket for that person is',amount)
    total+=amount
print('Total ticket price -',total)