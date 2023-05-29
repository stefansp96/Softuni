name = input()
total_grade = 0
year = 0
fail = 0

while True:
    grade = float(input())

    if grade < 4:
        fail += 1
        if fail == 2:
            current_failed_year = year + 1
            print(f'{name} has been excluded at {current_failed_year} grade')
            break
    else:
        year += 1
        total_grade += grade

    if year == 12:
        average_grade = total_grade / year
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break
