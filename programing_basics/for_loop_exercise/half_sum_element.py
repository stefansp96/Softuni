import sys
n = int(input())
max_num = -sys.maxsize
sum_num = 0

for i in range(0, n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum_num += current_num

current_sum = sum_num - max_num

if max_num == current_sum:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - current_sum)}')
