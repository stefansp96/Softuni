first_num = int(input())
second_num = int(input())
for character in range(first_num, second_num + 1):
    current_character = chr(character)
    print(current_character, end=' ')
