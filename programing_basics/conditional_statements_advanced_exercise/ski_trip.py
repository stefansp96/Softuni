days_stay = int(input())
type_room = input()
review = input()

nights_stay = days_stay - 1
cost = 0
total_cost = 0

if type_room == 'room for one person':
    cost = nights_stay * 18

elif type_room == 'apartment':
    cost = nights_stay * 25
    if days_stay < 10:
        cost *= 0.70
    elif 10 <= days_stay <= 15:
        cost *= 0.65
    else:
        cost *= 0.50

elif type_room == 'president apartment':
    cost = nights_stay * 35
    if days_stay < 10:
        cost *= 0.90
    elif 10 <= days_stay <= 15:
        cost *= 0.85
    else:
        cost *= 0.80

if review == 'positive':
    total_cost = cost + cost * 0.25
elif review == 'negative':
    total_cost = cost - cost * 0.10

print(f'{total_cost:.2f}')
