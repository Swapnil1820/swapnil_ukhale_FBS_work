# Convert the time entered in hh,min and sec into seconds.

hr=int(input('enter hours -'))
min=int(input('enter minutes -'))
sec=int(input('enter seconds -'))

total=(hr*3600)+(min*60)+sec
print(total)