target = 10000
steps = 0

while steps < 10000:
    action = input()
    if action == 'Going home':
        steps_to_home = int(input())
        steps += steps_to_home
        break
    else:
        steps += int(action)

if steps > 10000:
    print('Goal reached! Good job!')
    print(f'{steps - target} steps over the goal!')
else:
    print(f'{abs(steps - target)} more steps to reach goal.')
