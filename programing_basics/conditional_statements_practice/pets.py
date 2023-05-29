from math import ceil
from math import floor


number_days = int(input())
food_left = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day = float(input()) / 1000

dog_food_needed = dog_food_day * number_days
cat_food_needed = cat_food_day * number_days
turtle_food_needed = turtle_food_day * number_days
total_food_needed = dog_food_needed + cat_food_needed + turtle_food_needed
diff = abs(food_left - total_food_needed)

if food_left >= total_food_needed:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
