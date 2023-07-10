companies = {}
command = input().split(' -> ')

while command[0] != 'End':
    company_name, employee_id = command

    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    command = input().split(' -> ')

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
