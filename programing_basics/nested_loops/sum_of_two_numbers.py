n1 = int(input())
n2 = int(input())
magic_num = int(input())
counter = 0
flag = False
for x1 in range(n1, n2 + 1):
    for x2 in range(n1, n2 + 1):
        counter += 1
        if x1 + x2 == magic_num:
            flag = True
            result = f'Combination N:{counter} ({x1} + {x2} = {magic_num})'
            break
    if flag:
        break

if flag:
    print(result)
else:
    print(f'{counter} combinations - neither equals {magic_num}')
