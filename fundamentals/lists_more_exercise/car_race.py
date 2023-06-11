time_numbers = input().split(' ')
total_left_car_time = []
total_right_car_time = []
zero_in_times_left = False
zero_in_times_right = False
split_cars_index = len(time_numbers) // 2
left_car_numbers = time_numbers[0:split_cars_index]
right_car_numbers = time_numbers[split_cars_index + 1:]

for left_car_time in left_car_numbers:
    total_left_car_time.append(int(left_car_time))

for right_car_time in right_car_numbers:
    total_right_car_time.append(int(right_car_time))

left_car_sum = 0
right_car_sum = 0

for current_time_left in total_left_car_time:
    left_car_sum += current_time_left
    if current_time_left == 0:
        left_car_sum *= 0.8
for current_time_right in total_right_car_time:
    right_car_sum += current_time_right
    if current_time_right == 0:
        right_car_sum *= 0.8

if left_car_sum < right_car_sum:
    print(f'The winner is left with total time: {left_car_sum:.1f}')
else:
    print(f'The winner is right with total time: {right_car_sum:.1f}')
