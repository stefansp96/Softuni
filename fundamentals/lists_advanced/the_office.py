def check_employee_happiness(some_employees):
    employees_list = list(map(int, employees.split(' ')))
    improved_happiness = [person * factor for person in employees_list ]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(h >= average_happiness for h in improved_happiness)
    total_count = len(improved_happiness)

    message = 'happy' if happy_count >= total_count / 2 else 'not happy'
    result = f'Score: {happy_count}/{total_count}. Employees are {message}!'

    return result


employees = input()
factor = int(input())
result = check_employee_happiness(employees)
print(result)
