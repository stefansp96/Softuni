width = int(input())
length = int(input())
height = int(input())
total_space = width * length * height
free_space = width * length * height
space_taken = 0

while free_space > 0:
    command = input()
    if command == 'Done':
        print(f'{free_space} Cubic meters left.')
        break
    else:
        free_space -= int(command)
        space_taken += int(command)

if total_space < space_taken:
    print(f'No more free space! You need {abs(total_space - space_taken)} Cubic meters more.')
