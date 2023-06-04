planned_gifts = input().split(' ')
command = input().split(' ')

while command[0] != 'No' and command[1] != 'Money':
    if command[0] == 'OutOfStock':
        gift = command[1]
        for current_gift in range(len(planned_gifts)):
            if planned_gifts[current_gift] in [gift]:
                planned_gifts[current_gift] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(planned_gifts):
            planned_gifts[index] = command[1]
    elif command[0] == 'JustInCase':
        planned_gifts[-1] = command[1]

    command = input().split(' ')

while 'None' in planned_gifts:
    planned_gifts.remove('None')

for i in planned_gifts:
    print(i, end=' ')
