def smallest_number(some_numbers):
    min_numbers = min(some_numbers)
    return min_numbers


first_num = int(input())
second_num = int(input())
third_num = int(input())
numbers_list = [first_num, second_num, third_num]
min_number = smallest_number(numbers_list)
print(min_number)
