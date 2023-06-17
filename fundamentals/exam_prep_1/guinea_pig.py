food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000
days = 30
food_per_day = 300
not_enough = False

while days > 0:
    days -= 1
    food_quantity -= food_per_day
    if days % 2 == 0:
        hay_quantity -= food_quantity * 0.05
    if days % 3 == 0:
        cover_quantity -= guinea_pig_weight / 3
    if food_quantity < 0 or hay_quantity < 0 or cover_quantity < 0:
        not_enough = True
        break

if not_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity / 1000:.2f}, \
Hay: {hay_quantity / 1000:.2f}, Cover: {cover_quantity / 1000:.2f}.")
