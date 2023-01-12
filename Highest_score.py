student_scores = input("Input a list of student score: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

number = 0
for num in student_scores:
    if num > number:
        number = num

print(f'the highest score in the class is {number}')

