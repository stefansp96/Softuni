from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_meter = float(input())

time_for_distance = distance_in_meters * time_for_meter
water_resistance_seconds = floor(distance_in_meters / 15) * 12.5
total_time = time_for_distance + water_resistance_seconds
difference = abs(record_in_seconds - total_time)

if total_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
elif total_time >= record_in_seconds:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
