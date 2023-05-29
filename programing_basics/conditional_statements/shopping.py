budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())

gpu_price = 250
cpu_price = (number_gpu * gpu_price) * 0.35
ram_price = (number_gpu * gpu_price) * 0.10

total_price = (number_gpu * gpu_price) + (number_cpu * cpu_price) + (number_ram * ram_price)
discount = 0

if number_gpu > number_cpu:
    discount = total_price * 0.15
else:
    discount = 0

final_price = total_price - discount
difference = abs(final_price - budget)

if budget >= final_price:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
