from math import floor
from math import ceil

grape_area = int(input())
grape_per_meter = float(input())
needed_wine = int(input())
number_of_workers = int(input())

area_for_wine = grape_area * 0.4
kilograms_grape = area_for_wine * grape_per_meter
liters_wine = kilograms_grape / 2.5
diff = abs(needed_wine - liters_wine)
wine_for_worker = ceil(diff) // number_of_workers

if liters_wine < needed_wine:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {ceil(liters_wine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(wine_for_worker)} liters per person.')
