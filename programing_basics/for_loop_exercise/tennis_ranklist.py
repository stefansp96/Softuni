from math import floor

num_tour = int(input())
start_points = int(input())
total_points = 0
won_tour = 0

for i in range(num_tour):
    result = input()
    if result == 'W':
        won_tour += 1
        total_points += 2000
    elif result == 'F':
        total_points += 1200
    elif result == 'SF':
        total_points += 720

final_points = start_points + total_points
average_points = floor(total_points / num_tour)
percent_won = won_tour / num_tour * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{percent_won:.2f}%')
