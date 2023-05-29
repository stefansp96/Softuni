drink = input()
sugar = input()
num_drinks = int(input())
total_cost = 0

if drink == 'Espresso':
    if sugar == 'Without':
        total_cost = num_drinks * (0.90 * 0.65)
    elif sugar == 'Normal':
        total_cost = num_drinks * 1
    elif sugar == 'Extra':
        total_cost = num_drinks * 1.20

    if num_drinks >= 5:
        total_cost *= 0.75

elif drink == 'Cappuccino':
    if sugar == 'Without':
        total_cost = num_drinks * (1 * 0.65)
    elif sugar == 'Normal':
        total_cost = num_drinks * 1.20
    elif sugar == 'Extra':
        total_cost = num_drinks * 1.60

elif drink == 'Tea':
    if sugar == 'Without':
        total_cost = num_drinks * (0.50 * 0.65)
    elif sugar == 'Normal':
        total_cost = num_drinks * 0.60
    elif sugar == 'Extra':
        total_cost = num_drinks * 0.70

if total_cost > 15:
    total_cost *= 0.80

print(f'You bought {num_drinks} cups of {drink} for {total_cost:.2f} lv.')
