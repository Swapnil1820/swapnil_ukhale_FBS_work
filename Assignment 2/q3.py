#Convert distant given in feet and inches into meter and centimeter.

# Program to convert distance from feet & inches to meters & centimeters

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter remaining inches: "))

# 1 foot = 12 inches
total_inches = (feet * 12) + inches

# 1 inch = 2.54 cm
centimeters = total_inches * 2.54

meters = int(centimeters // 100)
cm = centimeters % 100

print(f"Distance: {meters} meter and {cm} centimeter")