items = input().split()

stock = {}

for index in range(0, len(items), + 2):
    food = items[index]
    quantity = int(items[index + 1])
    stock[food] = quantity

print(stock)
