num = int(input())
even_count = 0
odd_count = 0

for i in range(num):
    current_num = int(input())
    if i % 2 == 0:
        even_count += current_num
    else:
        odd_count += current_num

if even_count == odd_count:
    print('Yes')
    print(f'Sum = {even_count}')
else:
    print('No')
    print(f'Diff = {abs(even_count - odd_count)}')
