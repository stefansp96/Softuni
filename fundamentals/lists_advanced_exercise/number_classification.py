numbers_list = [int(number) for number in input().split(', ')]
positive_numbers = [num for num in numbers_list if num >= 0]
negative_numbers = [num for num in numbers_list if num < 0]
even_numbers = [num for num in numbers_list if num % 2 == 0]
odd_numbers = [num for num in numbers_list if num % 2 != 0]

print(f"Positive: {', '.join(str(char) for char in positive_numbers)}")
print(f"Negative: {', '.join(str(char) for char in negative_numbers)}")
print(f"Even: {', '.join(str(char) for char in even_numbers)}")
print(f"Odd: {', '.join(str(char) for char in odd_numbers)}")
