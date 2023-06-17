def merge(some_data, first_index, second_index):
    if first_index < 0:
        first_index = 0
    if second_index > len(some_data) - 1:
        second_index = len(some_data) - 1
    for index, data in enumerate(some_data):
        if index in range(first_index + 1, second_index + 1):
            some_data[first_index] += some_data[index]
    for index in range(second_index, first_index, - 1):
        some_data.pop(index)
    return some_data


def divide(some_data, index, partition):
    if partition > len(some_data):
        step = 1
    else:
        step = len(some_data[index]) // partition
    divided_data = some_data.pop(index)
    start = 0
    for part in range(partition):
        if part == partition - 1:
            some_data.insert(index, divided_data[start::])
            break
        else:
            some_data.insert(index, divided_data[start: start + step:])
        start += step
        index += 1
    return some_data


data_input = input().split()
command = input()

while command != '3:1':
    command = command.split()
    action = command[0]

    if action == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        result = merge(data_input, start_index, end_index)
    elif action == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        result = divide(data_input, index, partitions)

    command = input()

print(' '.join(result))

#working 100%
"""strings_input = input().split()
result = []
instructions = input()
while not instructions == "3:1":
    instructions = instructions.split()
    command = instructions[0]
    if command == 'merge':
        start = int(instructions[1])
        end = int(instructions[2])
        if start < 0:
            start = 0
        if end > len(strings_input) - 1:
            end = len(strings_input) - 1
        for index, string in enumerate(strings_input):
            if index in range(start + 1, end + 1):
                strings_input[start] += strings_input[index]
        for index in range(end, start, - 1):
            strings_input.pop(index)
    elif command == 'divide':
        index = int(instructions[1])
        partitions = int(instructions[2])
        if partitions > len(strings_input[index]):
            step = 1
        else:
            step = len(strings_input[index]) // partitions
        divide_part = strings_input.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                strings_input.insert(index, divide_part[start::])
                break
            else:
                strings_input.insert(index, divide_part[start: start + step:])
            start += step
            index += 1
    instructions = input()
print(' '.join(strings_input))"""