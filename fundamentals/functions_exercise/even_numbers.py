numbers = input().split(' ')
numbers_as_digits = []

for num in numbers:
    numbers_as_digits.append(int(num))

check_even = lambda x: x % 2 == 0
even_numbers = list(filter(check_even, numbers_as_digits))
print(even_numbers)