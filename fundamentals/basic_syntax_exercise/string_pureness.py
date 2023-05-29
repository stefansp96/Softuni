num_strings = int(input())

for i in range(num_strings):
    current_string = input()
    is_pure = True
    for char in current_string:
        if char == '.' or char == ',' or char == '_':
            is_pure = False
    if is_pure:
        print(f'{current_string} is pure.')
    else:
        print(f'{current_string} is not pure!')
