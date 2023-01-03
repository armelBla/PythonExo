student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
total_value = 0

for counter in student_heights:
    total_height += 1

for number in student_heights:
    total_value += number

total_value /= total_height
print(round(total_value))

