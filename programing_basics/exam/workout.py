from math import ceil
from math import floor

days_workout = int(input())
first_day_km = float(input())
distance = first_day_km
total_distance = first_day_km

for i in range(days_workout):
    percent_increase = int(input()) / 100
    distance += distance * percent_increase
    total_distance += distance


if total_distance >= 1000:
    print(f"You've done a great job running {ceil(total_distance - 1000)} more kilometers!")
else:
    print(f'Sorry Mrs. Ivanova, you need to run {abs(floor(total_distance - 1000))} more kilometers')
