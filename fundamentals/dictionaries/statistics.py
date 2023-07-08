stock = {}

while True:
    data = input().split(': ')

    if 'statistics' in data:
        break

    product = data[0]
    quantity = int(data[1])

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

total_products = len(stock)
products_sum = sum(stock.values())

print('Products in stock:')
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {products_sum}")
