tank_capacity = 255
number_of_pours = int(input())
water_filled = 0

for pours in range(number_of_pours):
    pour_amount = int(input())
    if pour_amount + water_filled > tank_capacity:
        print('Insufficient capacity!')
        continue
    else:
        water_filled += pour_amount

print(water_filled)
