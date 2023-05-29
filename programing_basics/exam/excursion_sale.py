sea_trip = int(input())
mountain_trip = int(input())
command = input()
income = 0

while command != 'Stop':
    if command == 'sea':
        if sea_trip > 0:
            income += 680
            sea_trip -= 1
    elif command == 'mountain':
        if mountain_trip > 0:
            income += 499
            mountain_trip -= 1

    if sea_trip <= 0 and mountain_trip <= 0:
        print(f'Good job! Everything is sold.')
        break

    command = input()

print(f'Profit: {income} leva.')
