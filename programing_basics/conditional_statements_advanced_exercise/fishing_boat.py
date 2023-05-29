budget = int(input())
season = input()
num_fisherman = int(input())
total_sum = 0
ship_cost = 0
discount = 0

if season == 'Spring':
    ship_cost = 3000
    if num_fisherman <= 6:
        ship_cost *= 0.90
    elif 6 < num_fisherman <= 11:
        ship_cost *= 0.85
    elif num_fisherman >= 12:
        ship_cost *= 0.75

if season == 'Summer' or season == 'Autumn':
    ship_cost = 4200
    if num_fisherman <= 6:
        ship_cost *= 0.90
    elif 6 < num_fisherman <= 11:
        ship_cost *= 0.85
    elif num_fisherman >= 12:
        ship_cost *= 0.75

if season == 'Winter':
    ship_cost = 2600
    if num_fisherman <= 6:
        ship_cost *= 0.90
    elif 6 < num_fisherman <= 11:
        ship_cost *= 0.85
    elif num_fisherman >= 12:
        ship_cost *= 0.75

if season != 'Autumn' and num_fisherman % 2 == 0:
    discount = ship_cost * 0.05

total_sum = ship_cost - discount
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
