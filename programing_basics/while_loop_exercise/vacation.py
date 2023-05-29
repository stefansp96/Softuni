money_needed = float(input())
money_owned = float(input())
days_counter = 0
spend_counter = 0

while money_owned < money_needed and spend_counter < 5:
    action = input()
    money = float(input())
    days_counter += 1
    if action == 'save':
        money_owned += money
        spend_counter = 0
    elif action == 'spend':
        money_owned -= money
        spend_counter += 1
        if money_owned < 0:
            money_owned = 0

if spend_counter >= 5:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f'You saved the money for {days_counter} days.')
