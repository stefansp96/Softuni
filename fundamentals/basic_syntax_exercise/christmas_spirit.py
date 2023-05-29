quantity = int(input())
days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
spirit = 0

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity
        spirit += 5
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity
        spirit += 13
    if current_day % 5 == 0:
        total_cost += tree_lights_price * quantity
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days % 10 == 0:
    spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit}')
