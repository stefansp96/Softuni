baggage_20 = float(input())
baggage_weight = float(input())
days = int(input())
baggage_num = int(input())

baggage_cost = 0

if baggage_weight > 20:
    baggage_cost = baggage_20
elif 10 <= baggage_weight <= 20:
    baggage_cost = baggage_20 * 0.50
else:
    baggage_cost = baggage_20 * 0.20

cost_increase = 0

if days > 30:
    cost_increase = baggage_cost * 0.10
elif 7 <= days <= 30:
    cost_increase = baggage_cost * 0.15
else:
    cost_increase = baggage_cost * 0.40

final_sum = (baggage_cost + cost_increase) * baggage_num
print(f'The total price of bags is: {final_sum:.2f} lv.')
