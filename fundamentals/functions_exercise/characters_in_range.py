def characters_in_range(first_char, second_char):
    characters = []
    for current_char_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_char_as_digit))
    return characters


first_character = input()
second_character = input()
result = characters_in_range(first_character, second_character)
print(' '.join(result))
