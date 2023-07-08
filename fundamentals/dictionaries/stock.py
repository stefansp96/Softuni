items = input().split()

stock = {}

for index in range(0, len(items), + 2):
    food = items[index]
    quantity = int(items[index + 1])
    stock[food] = quantity

items_to_search = input().split()

for item in items_to_search:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
