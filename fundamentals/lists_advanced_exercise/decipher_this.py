def num_to_string(some_word):
    current_string = list(some_word)
    num_as_string = []
    while current_string[0].isdigit():
        num_as_string.append(current_string[0])
        current_string.pop(0)
    num = int(''.join(num_as_string))
    current_string.insert(0, chr(num))
    return ''.join(current_string)


def replace_letters(some_word):
    current_string = list(some_word)
    current_string[1], current_string[-1] = current_string[-1], current_string[1]
    return ''.join(current_string)


print(' '.join([replace_letters(num_to_string(word)) for word in input().split()]))

