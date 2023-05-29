budget = float(input())
season = input()

destination = ''
vacation = ''
money_spent = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation = 'Camp'
        money_spent = budget * 0.30
    elif season == 'winter':
        vacation = 'Hotel'
        money_spent = budget * 0.70

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation = 'Camp'
        money_spent = budget * 0.40
    elif season == 'winter':
        vacation = 'Hotel'
        money_spent = budget * 0.80

elif budget > 1000 and season == 'summer' or season == 'winter':
    destination = 'Europe'
    vacation = 'Hotel'
    money_spent = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{vacation} - {money_spent:.2f}')
