fails_allowed = int(input())
fail_counter = 0
problem_counter = 0
grades_total = 0
last_problem = ''
has_failed = True

while fail_counter < fails_allowed:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        fail_counter += 1

    problem_counter += 1
    grades_total += grade
    last_problem = problem_name

if has_failed:
    print(f'You need a break, {fail_counter} poor grades.')
else:
    print(f'Average score: {(grades_total / problem_counter):.2f}')
    print(f'Number of problems: {problem_counter}')
    print(f'Last problem: {last_problem}')
