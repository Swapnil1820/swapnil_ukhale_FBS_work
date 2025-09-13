# Write a program to calculate area of circle

def circle_area(radius):
    return 3.14 * radius * radius

radius = float(input("Enter the radius of the circle: "))

area = circle_area(radius)
print("The area of the circle is:", area)
