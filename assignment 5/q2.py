# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n=int(input('enter number of students :'))
total_percentage=0

for i in range (1,n+1):
    total=0
    for j in range(1,6):
        marks = int(input(f"Enter marks for subject {j} of student {i}: "))
        total += marks
    percent = total / 5
    print(f'student {i} and the percentage is {percent}')
    total_percentage += percent

average=total_percentage / n
print(f'Average percentages of students is : {average}')
