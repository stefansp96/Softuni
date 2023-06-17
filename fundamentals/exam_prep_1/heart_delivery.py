houses = [int(x) for x in input().split('@')]
command = input()
hearts = 2
current_house = 0
successful = []
not_successful = []

while command != 'Love!':
    command = command.split()
    jump_length = int(command[1])
    current_house += jump_length

    if current_house >= len(houses):
        current_house = 0

    if houses[current_house] == 0:
        print(f"Place {current_house} already had Valentine's day.")
        command = input()
        continue

    houses[current_house] -= hearts

    if houses[current_house] == 0:
        print(f"Place {current_house} has Valentine's day.")

    command = input()

for house in houses:
    if house == 0:
        successful.append(house)
    else:
        not_successful.append(house)

print(f"Cupid's last position was {current_house}.")
if len(successful) == len(houses):
    print("Mission was successful.")
else:
    print(f'Cupid has failed {len(not_successful)} places.')
