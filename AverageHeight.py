


student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0

for height in student_heights:
    total_height = total_height + height

total_students = 0

for student in student_heights:
    total_students += 1

average_height = total_height / total_students

print(average_height)