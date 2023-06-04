ticket = 150
items = input().split('|')
budget = float(input())
sell_prices = []
profit = 0

for item in items:
    type_of_item, price = item.split('->')
    price = float(price)
    price_is_valid = False
    if type_of_item == 'Clothes':
        if price <= 50:
            price_is_valid = True
    elif type_of_item == 'Shoes':
        if price <= 35:
            price_is_valid = True
    elif type_of_item == 'Accessories':
        if price <= 20.50:
            price_is_valid = True

    if price_is_valid:
        if price <= budget:
            budget -= price
            sell_price = price * 1.40
            profit += (sell_price - price)
            sell_prices.append(f'{sell_price:.2f}')

for money in sell_prices:
    print(money, end=' ')
    money = float(money)
    budget += money
print()
print(f'Profit: {profit:.2f}')
if budget >= ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
