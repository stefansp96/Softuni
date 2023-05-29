number_of_points = int(input())
bonus = 0

if number_of_points <= 100:
    bonus = 5
elif 100 < number_of_points < 1000:
    bonus = number_of_points * 0.20
elif number_of_points > 1000:
    bonus = number_of_points * 0.10

if number_of_points % 2 == 0:
    bonus += 1
elif number_of_points % 10 == 5:
    bonus += 2

print(bonus)
print(number_of_points + bonus)
