num1 = int(input())
num2 = int(input())
operation = input()
result = 0
type_number = ''

if operation == '+' or operation == '-' or operation == '*':
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'
    print(f'{num1} {operation} {num2} = {result} - {type_number}')

elif operation == '/':
    if num2 == 0:
        print(f'Cannot divide {num1} by zero')
    else:
        result = num1 / num2
        print(f'{num1} / {num2} = {result:.2f}')

elif operation == '%':
    if num2 == 0:
        print(f'Cannot divide {num1} by zero')
    else:
        result = num1 % num2
        print(f'{num1} % {num2} = {result}')
