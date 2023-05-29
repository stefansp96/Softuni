floors = int(input())
room_per_floor = int(input())

for floor in reversed(range(1, floors + 1)):

    type_room = 'A' if floor % 2 else 'O'

    if floor == floors:
        type_room = 'L'

    for room in range(room_per_floor):
        room_name = f'{type_room}{floor}{room}'
        print(room_name, end=' ')

    print()
