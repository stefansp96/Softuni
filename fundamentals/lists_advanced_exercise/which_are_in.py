def find_substrings(strings_one, strings_two):
    substring_list = []
    for first_string in strings_one:
        for second_string in strings_two:
            if first_string in second_string:
                substring_list.append(first_string)
                break
    return substring_list


first_string_line = input().split(', ')
second_string_line = input().split(', ')
print(find_substrings(first_string_line, second_string_line))
