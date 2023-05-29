number = int(input())
first_sum = 0
second_sum = 0

for i in range(number):
    first_number = int(input())
    first_sum += first_number

for i in range(number):
    second_number = int(input())
    second_sum += second_number

if first_sum == second_sum:
    print(f'Yes, sum = {first_sum}')
else:
    print(f'No, diff = {abs(first_sum - second_sum)}')
