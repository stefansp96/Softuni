type_fuel = input()
amount_fuel = float(input())
club_card = input()

fuel_price = 0
discount = 0

if type_fuel == 'Gas':
    fuel_price = amount_fuel * 0.93
    if club_card == 'Yes':
        fuel_price = amount_fuel * 0.85

elif type_fuel == 'Gasoline':
    fuel_price = amount_fuel * 2.22
    if club_card =='Yes':
        fuel_price = amount_fuel * 2.04

else:
    fuel_price = amount_fuel * 2.33
    if club_card == 'Yes':
        fuel_price = amount_fuel * 2.21

if 20 <= amount_fuel <= 25:
    discount = fuel_price * 0.08

elif amount_fuel > 25:
    discount = fuel_price * 0.10

final_price = fuel_price - discount

print(f'{final_price:.2f} lv.')
