# WAP to print Armstrong number within a given range

# An Armstrong number is a number whose sum of cubes of its digits is equal to the number itself.
# Example: 153 → 1³ + 5³ + 3³ = 153

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end+1):
    temp = num
    sum_cube = 0
    while temp > 0:
        sum_cube += (temp % 10) ** 3
        temp //= 10
    if sum_cube == num:
        print(num, end=" ")