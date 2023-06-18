def blacklist(some_names, some_name):
    for current_name in some_names:
        current_name_index = some_names.index(current_name)
        if current_name == some_name:
            print(f"{current_name} was blacklisted.")
            some_names.pop(current_name_index)
            some_names.insert(current_name_index, 'Blacklisted')
            blacklisted_names.append(1)
            break
        if current_name_index == len(some_names) - 1 and current_name != some_name:
            print(f'{some_name} was not found.')
    return some_names


def error(some_names, some_index):
    if len(some_names) - 1 >= some_index >= 0:
        if some_names[some_index] != 'Blacklisted' and some_names[some_index] != 'Lost':
            print(f'{some_names[some_index]} was lost due to an error.')
            some_names[some_index] = 'Lost'
            lost_names.append(1)
    return some_names


def change(some_names, some_index, some_name):
    if len(some_names) - 1 >= some_index >= 0:
        print(f"{some_names[some_index]} changed his username to {some_name}.")
        some_names.pop(some_index)
        some_names.insert(some_index, some_name)
    return some_names


friend_list = input().split(', ')
command = input()
blacklisted_names = []
lost_names = []

while command != 'Report':
    command = command.split()
    action = command[0]

    if action == 'Blacklist':
        name = command[1]
        friend_list = blacklist(friend_list, name)
    if action == 'Error':
        index = int(command[1])
        friend_list = error(friend_list, index)
    if action == 'Change':
        index = int(command[1])
        new_name = command[2]
        friend_list = change(friend_list, index, new_name)

    command = input()

print(f"Blacklisted names: {sum(blacklisted_names)}")
print(f"Lost names: {sum(lost_names)}")
print(' '.join(friend_list))
