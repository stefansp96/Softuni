students = []
course_to_search = ''

while True:
    some_data = input()

    if ':' not in some_data:
        course_to_search = some_data
        break

    name, student_id, course = some_data.split(':')
    students.append({'name': name, 'student_id': student_id, 'course': course})

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['student_id']}")
