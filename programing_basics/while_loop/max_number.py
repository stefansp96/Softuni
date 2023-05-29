from sys import maxsize

max_number = -maxsize

while True:
    action = input()
    if action == 'Stop':
        break

    current_num = int(action)

    if current_num > max_number:
        max_number = current_num

print(max_number)
