price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_sum = (number_of_puzzles * price_puzzle) + (number_of_dolls * price_doll) + (number_of_bears * price_bear) + \
            (number_of_minions * price_minion) + (number_of_trucks * price_truck)

discount = 0

if number_of_minions + number_of_trucks + number_of_dolls + number_of_bears + number_of_puzzles >= 50:
    discount = total_sum * 0.25

final_price = total_sum - discount
profit = final_price - (final_price * 0.10)
difference = abs(profit - trip_price)

if profit > trip_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
