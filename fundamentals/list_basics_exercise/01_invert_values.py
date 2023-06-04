numbers_as_string = input().split()
list_of_numbers = []

for element in numbers_as_string:
    current_element = -int(element)
    list_of_numbers.append(current_element)

print(list_of_numbers)
