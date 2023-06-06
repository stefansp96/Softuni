numbers_string = input().split(' ')
given_message = input()
given_message_list = list(given_message)
numbers_list = []
special_message_list = []

for number in numbers_string:
    current_sum = 0
    for num in number:
        current_sum += int(num)
    numbers_list.append(current_sum)

for current_num in numbers_list:
    current_index = 0
    while current_index != current_num:
        current_index += 1
    if len(given_message) < current_index:
        current_index -= len(given_message)
        special_message_list.append(given_message_list[current_index])
        given_message_list.pop(current_index)
    else:
        special_message_list.append(given_message_list[current_index])
        given_message_list.pop(current_index)

special_message = ''.join(special_message_list)
print(special_message)

