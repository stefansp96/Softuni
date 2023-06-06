numbers = input().split(', ')
numbers_list = []
zeros = []
not_zeros = []

for num in numbers:
    numbers_list.append(int(num))

for number in numbers_list:
    if number == 0:
        zeros.append(number)
    else:
        not_zeros.append(number)

sorted_numbers = not_zeros + zeros
print(sorted_numbers)
