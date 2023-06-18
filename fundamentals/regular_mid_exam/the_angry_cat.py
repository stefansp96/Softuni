owner_items = [int(x) for x in input().split(', ')]
entry_point_index = int(input())
type_of_value = input()
left_part = owner_items[:entry_point_index:]
right_part = owner_items[entry_point_index + 1::]
broken_items_left = []
broken_items_right = []
value_threshold = owner_items[entry_point_index]

if type_of_value == 'cheap':
    for item in left_part:
        if item < value_threshold:
            broken_items_left.append(item)
    for item in right_part:
        if item < value_threshold:
            broken_items_right.append(item)

if type_of_value == 'expensive':
    for item in left_part:
        if item >= value_threshold:
            broken_items_left.append(item)
    for item in right_part:
        if item >= value_threshold:
            broken_items_right.append(item)

total_value_left = sum(broken_items_left)
total_value_right = sum(broken_items_right)

if total_value_left >= total_value_right:
    position = 'Left'
    print(f"{position} - {total_value_left}")
else:
    position = 'Right'
    print(f"{position} - {total_value_right}")
