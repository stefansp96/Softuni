numbers_as_string = input().split()
numbers_as_digits = [int(num) for num in numbers_as_string]
max_number = max(numbers_as_digits)
min_number = min(numbers_as_digits)
sum_of_numbers = sum(numbers_as_digits)
print(f'The minimum number is {min_number}')
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_of_numbers}")
