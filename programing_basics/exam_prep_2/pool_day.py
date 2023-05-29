from math import ceil

people = int(input())
entry_tax = float(input())
bed_price = float(input())
umbrella_price = float(input())

total_tax = people * entry_tax
beds_cost = ceil(people * 0.75) * bed_price
umbrella_cost = ceil(people * 0.50) * umbrella_price
total_cost = total_tax + beds_cost + umbrella_cost

print(f'{total_cost:.2f} lv.')
