students_height=input("Enter the list of students height ").split()
for n in range (0,len(students_height)):
    students_height[n]=int(students_height[n])
number_of_student=0
for student in students_height:
    number_of_student+=1
total_height=0
for height in students_height:
    total_height+=height
average=total_height/number_of_student
print(round(average))
