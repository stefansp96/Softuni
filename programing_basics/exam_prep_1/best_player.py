player = input()
hat_trick = False
best_player = ''
counter = 0

while player != 'END':
    goals = int(input())

    if goals > counter:
        best_player = player
        counter = goals

        if goals >= 3:
            hat_trick = True

        if goals >= 10:
            break

    player = input()

print(f'{best_player} is the best player!')

if hat_trick:
    print(f'He has scored {counter} goals and made a hat-trick !!!')
else:
    print(f'He has scored {counter} goals.')
