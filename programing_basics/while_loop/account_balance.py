balance = 0

while True:
    action = input()
    if action == 'NoMoreMoney':
        break

    current_amount = float(action)

    if current_amount > 0:
        balance += current_amount
        print(f'Increase: {current_amount:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {balance:.2f}')
