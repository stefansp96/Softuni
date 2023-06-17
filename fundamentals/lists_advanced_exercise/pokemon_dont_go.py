distances_list = [int(x) for x in input().split()]
removed_elements = []
index = int(input())

while distances_list:
    removed_element_value = 0
    if index < 0:
        removed_element_value = distances_list[0]
        removed_elements.append(distances_list[0])
        distances_list.pop(0)
        distances_list.insert(0, distances_list[-1])
    elif index > len(distances_list) - 1:
        removed_element_value = distances_list[-1]
        removed_elements.append(distances_list[-1])
        distances_list.pop(-1)
        distances_list.append(distances_list[0])
    else:
        removed_element_value = distances_list[index]
        removed_elements.append(distances_list[index])
        distances_list.pop(index)
    for current_index, value in enumerate(distances_list):
        if value <= removed_element_value:
            distances_list[current_index] += removed_element_value
        elif value > removed_element_value:
            distances_list[current_index] -= removed_element_value
    if len(distances_list) <= 0:
        break

    index = int(input())

print(sum(removed_elements))
