# WAP to calculate selling price of book based on cost price and discount.

cost_price=float(input('enter cost price -'))
discount=float(input('enter discount -'))

dis=(discount/100)*cost_price   #discount amount
selling_price=cost_price - dis

print(f'the selling price of a book is {selling_price}')