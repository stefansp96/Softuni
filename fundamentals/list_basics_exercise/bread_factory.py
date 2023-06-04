events = input().split('|')
energy = 100
coins = 100
factory_is_open = True

for event in events:
    type_event, value = event.split('-')
    value = int(value)
    if type_event == 'rest':
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif type_event == 'order':
        if energy >= 30:
            coins += value
            energy -= 30
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= value:
            coins -= value
            print(f'You bought {type_event}.')
        else:
            print(f'Closed! Cannot afford {type_event}.')
            factory_is_open = False
            break

if factory_is_open:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
