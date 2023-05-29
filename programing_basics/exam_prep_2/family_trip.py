budget = float(input())
num_nights = int(input())
night_price = float(input())
expenses_percent = int(input()) / 100

if num_nights > 7:
    night_price *= 0.95

sleep_cost = num_nights * night_price
expense = budget * expenses_percent
total_cost = sleep_cost + expense
diff = abs(total_cost - budget)

if total_cost <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
