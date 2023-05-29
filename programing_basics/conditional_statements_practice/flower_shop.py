from math import floor
from math import ceil


number_magnolia = int(input())
number_hyacinth = int(input())
number_roses = int(input())
number_cactus = int(input())
price_for_gift = float(input())

price_magnolia = number_magnolia * 3.25
price_hyacinth = number_hyacinth * 4
price_roses = number_roses * 3.50
price_cactus = number_cactus * 8

total_order = (price_magnolia + price_hyacinth + price_roses + price_cactus) * 0.95
diff = abs(price_for_gift - total_order)

if total_order >= price_for_gift:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')
