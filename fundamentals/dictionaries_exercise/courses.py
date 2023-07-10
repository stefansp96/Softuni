courses = {}
command = input()

while command != 'end':
    command = command.split(' : ')
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses.keys():
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)

    command = input()

for key, values in courses.items():
    print(f"{key}: {len(values)}")
    for student in values:
        print(f"-- {student}")
