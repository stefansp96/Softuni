energy = int(input())
won_battles = 0
command = input()
game_lost = False

while command != 'End of battle':
    command = int(command)
    if command > energy:
        game_lost = True
        break

    energy -= command
    won_battles += 1

    if won_battles % 3 == 0:
        energy += won_battles

    command = input()

if game_lost:
    print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
