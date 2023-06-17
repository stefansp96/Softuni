def urgent(grocery_list, some_item):
    if some_item not in grocery_list:
        grocery_list.insert(0, some_item)
    return grocery_list


def unnecessary(grocery_list, some_item):
    if some_item in grocery_list:
        grocery_list.remove(some_item)
    return grocery_list


def correct(grocery_list, old_item, new_item):
    if old_item in grocery_list:
        item_index = grocery_list.index(old_item)
        grocery_list.remove(old_item)
        grocery_list.insert(item_index, new_item)
    return grocery_list


def rearrange(grocery_list, some_item):
    if some_item in grocery_list:
        grocery_list.remove(some_item)
        grocery_list.append(some_item)
    return grocery_list


groceries_list = input().split('!')
command = input()

while command != 'Go Shopping!':
    command = command.split()
    action = command[0]
    item = command[1]

    if action == 'Urgent':
        groceries_list = urgent(groceries_list, item)
    elif action == 'Unnecessary':
        groceries_list = unnecessary(groceries_list, item)
    elif action == 'Correct':
        second_item = command[2]
        groceries_list = correct(groceries_list, item, second_item)
    elif action == 'Rearrange':
        groceries_list = rearrange(groceries_list, item)

    command = input()

print(', '.join(groceries_list))
