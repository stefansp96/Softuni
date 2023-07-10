students = {}
number_of_students = int(input())

for current_student in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = [grade]
    else:
        students[name].append(grade)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    students[student] = average_grade

for student in list(students):
    if students[student] < 4.50:
        del students[student]

for key, value in students.items():
    print(f"{key} -> {value:.2f}")
