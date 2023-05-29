destination = input()
saved_money = 0
while destination != 'End':
    cost = float(input())
    while saved_money < cost:
        money = float(input())
        saved_money += money
        if saved_money >= cost:
            print(f'Going to {destination}!')
            break
    saved_money = 0
    cost = 0
    destination = input()