number_of_cars = int(input())
wagon_list = [0] * number_of_cars
command = input()

while command != 'End':
    command = command.split(' ')
    if command[0] == 'add':
        wagon_list[-1] += int(command[1])
    elif command[0] == 'insert':
        index = int(command[1])
        wagon_list[index] += int(command[2])
    elif command[0] == 'leave':
        index = int(command[1])
        wagon_list[index] -= int(command[2])
    command = input()

print(wagon_list)
