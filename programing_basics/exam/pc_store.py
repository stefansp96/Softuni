cpu_price = float(input()) * 1.57
gpu_price = float(input()) * 1.57
ram_price = float(input()) * 1.57
num_ram = int(input())
discount_percent = float(input())

cpu_price_discount = cpu_price - (cpu_price * discount_percent)
gpu_price_discount = gpu_price - (gpu_price * discount_percent)
ram_cost = ram_price * num_ram
total_cost = cpu_price_discount + gpu_price_discount + ram_cost

print(f'Money needed - {total_cost:.2f} leva.')
