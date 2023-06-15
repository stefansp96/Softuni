def find_even_index(some_numbers):
    index_list = []
    for index in range(len(some_numbers)):
        value = some_numbers[index]
        if value % 2 == 0:
            index_list.append(index)
    return index_list


numbers_list = list(map(int, input().split(', ')))
print(find_even_index(numbers_list))
