def check_for_chairs(some_room):
    if len(some_room[0]) >= len(range(int(some_room[1]))):
        free_chairs = (len(some_room[0]) - len(range(int(some_room[1]))))
        current_result = free_chairs
    else:
        diff = (len(some_room[0]) - len(range(int(some_room[1]))))
        print(f"{abs(diff)} more chairs needed in room {current_room}")
        current_result = diff
    return current_result


number_of_rooms = int(input())
total_free_chair = []
current_room = 0
enough_chairs = True

while number_of_rooms > 0:
    current_room += 1
    room = input().split(' ')
    result = check_for_chairs(room)
    if result >= 0:
        total_free_chair.append(result)
    else:
        enough_chairs = False
    number_of_rooms -= 1

if enough_chairs:
    print(f'Game On, {sum(total_free_chair)} free chairs left')
    