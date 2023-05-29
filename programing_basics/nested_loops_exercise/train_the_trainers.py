judges = int(input())
task = input()
total_grades = 0
counter = 0

while task != 'Finish':
    grades = 0
    for i in range(1, judges + 1):
        grade = float(input())
        counter += 1
        total_grades += grade
        grades += grade

    print(f'{task} - {(grades / judges):.2f}.')
    grades = 0
    task = input()

print(f"Student's final assessment is {(total_grades / counter):.2f}.")
