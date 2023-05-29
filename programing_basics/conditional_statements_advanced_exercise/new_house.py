type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
expense = 0

if type_of_flowers == 'Roses':
    expense = number_of_flowers * 5
    if number_of_flowers > 80:
        expense *= 0.90

elif type_of_flowers == 'Dahlias':
    expense = number_of_flowers * 3.80
    if number_of_flowers > 90:
        expense *= 0.85

elif type_of_flowers == 'Tulips':
    expense = number_of_flowers * 2.80
    if number_of_flowers > 80:
        expense *= 0.85

elif type_of_flowers == 'Narcissus':
    expense = number_of_flowers * 3
    if number_of_flowers < 120:
        expense *= 1.15

elif type_of_flowers == 'Gladiolus':
    expense = number_of_flowers * 2.50
    if number_of_flowers < 80:
        expense *= 1.20

diff = abs(budget - expense)

if budget >= expense:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

