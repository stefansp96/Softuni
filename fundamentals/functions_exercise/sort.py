numbers_as_string = input().split(' ')
numbers_as_digits = [int(num) for num in numbers_as_string]
sorted_numbers = sorted(numbers_as_digits)
print(sorted_numbers)
