days_of_adventure = int(input())
number_of_players = int(input())
total_energy = float(input())
total_water = float(input()) * days_of_adventure * number_of_players
total_food = float(input()) * days_of_adventure * number_of_players
days_count = 0
quest_failed = False

while days_of_adventure > 0:
    energy_loss = float(input())

    if total_energy - energy_loss <= 0:
        quest_failed = True
        print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
        break

    total_energy -= energy_loss
    days_of_adventure -= 1
    days_count += 1

    if days_count % 2 == 0:
        total_energy += total_energy * 0.05
        total_water -= total_water * 0.30

    if days_count % 3 == 0:
        total_food -= total_food / number_of_players
        total_energy += total_energy * 0.10


if not quest_failed:
    print(f'You are ready for the quest. You will be left with - {total_energy:.2f} energy!')
