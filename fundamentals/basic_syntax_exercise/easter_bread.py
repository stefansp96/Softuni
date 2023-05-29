budget = float(input())
flour_price = float(input())
egg_pack_price = flour_price * 0.75
liter_milk_price = flour_price * 1.25
milk_for_bread = liter_milk_price * 0.25
colored_eggs = 0
loaves_of_bread = 0
price_for_bread = flour_price + egg_pack_price + milk_for_bread

while budget > price_for_bread:
    budget -= price_for_bread
    loaves_of_bread += 1
    colored_eggs += 3
    if loaves_of_bread % 3 == 0:
        colored_eggs -= (loaves_of_bread - 2)

print(f"You made {loaves_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
