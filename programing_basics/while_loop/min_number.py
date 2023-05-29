from sys import maxsize

min_number = maxsize

while True:
    action = input()
    if action == 'Stop':
        break

    current_num = int(action)

    if current_num < min_number:
        min_number = current_num

print(min_number)
