numbers_list = list(map(int, input().split(', ')))
current_group = 10

while numbers_list:
    numbers_for_current_group = [num for num in numbers_list if num <= current_group]
    print(f"Group of {current_group}'s: {numbers_for_current_group}")
    numbers_list = [number for number in numbers_list if number not in numbers_for_current_group]
    current_group += 10
