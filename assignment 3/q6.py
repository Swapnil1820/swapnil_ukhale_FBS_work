# Write a program to calculate profit or loss.

cost_price=float(input('enter cost price -'))
selling_price=float(input('enter selling price'))

if(selling_price > cost_price):
    print('profit',selling_price - cost_price)
elif(cost_price > selling_price):
    print('loss',cost_price - selling_price)
else:
    print('no profit and no loss')