budget = float(input())
number_of_extras = int(input())
price_per_extra = float(input())

price_for_decor = budget * 0.10
price_for_clothing = number_of_extras * price_per_extra

if number_of_extras > 150:
    price_for_clothing = price_for_clothing * 0.90

total_sum = price_for_decor + price_for_clothing
money_left = abs(budget - total_sum)

if budget < total_sum:
    print('Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')
elif budget >= total_sum:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
