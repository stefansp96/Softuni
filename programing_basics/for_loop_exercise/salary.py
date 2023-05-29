tabs_open = int(input())
salary = int(input())
fines = 0

for i in range(tabs_open):
    current_tab = input()
    if current_tab == 'Facebook':
        fines += 150
    elif current_tab == 'Instagram':
        fines += 100
    elif current_tab == 'Reddit':
        fines += 50

    if fines >= salary:
        print('You have lost your salary.')
        break

if salary > fines:
    print(salary - fines)
