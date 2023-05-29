num_dancers = int(input())
num_points = float(input())
season = input()
place = input()

prize = 0

if place == 'Bulgaria':
    prize = num_dancers * num_points
    if season == 'summer':
        prize *= 0.95
    else:
        prize *= 0.92
else:
    prize = num_dancers * num_points
    prize += prize * 0.50
    if season == 'summer':
        prize *= 0.90
    else:
        prize *= 0.85

money_for_charity = prize * 0.75
money_left = prize - money_for_charity
money_per_person = money_left / num_dancers

print(f'Charity - {money_for_charity:.2f}')
print(f'Money per dancer - {money_per_person:.2f}')
