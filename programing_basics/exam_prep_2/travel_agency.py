city = input()
package = input()
VIP_discount = input()
days_stay = int(input())
cost = 0

if days_stay < 1:
    print('Days must be positive number!')
    exit()


if city == 'Bansko' or city == 'Borovets':
    if package == 'noEquipment':
        cost = days_stay * 80
        if VIP_discount == 'yes':
            cost *= 0.95
        if days_stay > 7:
            cost -= 80
    elif package == 'withEquipment':
        cost = days_stay * 100
        if VIP_discount == 'yes':
            cost *= 0.90
        if days_stay > 7:
            cost -= 100
    else:
        print('Invalid input!')
        exit()


elif city == 'Varna' or city == 'Burgas':
    if package == 'noBreakfast':
        cost = days_stay * 100
        if VIP_discount == 'yes':
            cost *= 0.93
        if days_stay > 7:
            cost -= 100
    elif package == 'withBreakfast':
        cost = days_stay * 130
        if VIP_discount == 'yes':
            cost *= 0.88
        if days_stay > 7:
            cost -= 130
    else:
        print('Invalid input!')
        exit()

else:
    print('Invalid input!')
    exit()


print(f'The price is {cost:.2f}lv! Have a nice time!')
