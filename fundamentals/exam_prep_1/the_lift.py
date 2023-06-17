people = int(input())
lift_cars = [int(x) for x in input().split()]
MAX_CAPACITY = 4
empty_spots = False

for current_car in range(len(lift_cars)):
    while lift_cars[current_car] < MAX_CAPACITY and people > 0:
        lift_cars[current_car] += 1
        people -= 1

for car in range(len(lift_cars)):
    if lift_cars[car] < MAX_CAPACITY:
        empty_spots = True

if people == 0 and empty_spots:
    print("The lift has empty spots!")
    print(*lift_cars)
elif people > 0 and not empty_spots:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift_cars)
else:
    print(*lift_cars)
