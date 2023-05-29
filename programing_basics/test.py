from math import ceil

wall_height = int(input())
wall_width = int(input())
percent_unpainted = int(input()) / 100
total_wall_size = wall_width * wall_height * 4
total_wall_size_for_paint = ceil(total_wall_size - (total_wall_size * percent_unpainted))
walls_painted = total_wall_size_for_paint
total_paint_used = 0

command = input()

while True:
    if command == 'Tired!':
        print(f'{walls_painted} quadratic m left.')
        break

    paint_used = int(command)
    walls_painted -= paint_used
    total_paint_used += paint_used

    if walls_painted < 1:
        if total_paint_used > total_wall_size_for_paint:
            print(f'All walls are painted and you have {abs(total_wall_size - total_paint_used)} l paint left!')
        elif total_paint_used == total_wall_size_for_paint:
            print('All walls are painted! Great job, Pesho!')
        break

    command = input()