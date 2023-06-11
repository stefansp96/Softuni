def calculator(operation, first_num, second_num):
    if operation == 'multiply':
        return first_num * second_num
    elif operation == 'divide':
        return int(first_num / second_num)
    elif operation == 'add':
        return first_num + second_num
    elif operation == 'subtract':
        return first_num - second_num


operation = input()
first_num = int(input())
second_num = int(input())

print(calculator(operation, first_num, second_num))
