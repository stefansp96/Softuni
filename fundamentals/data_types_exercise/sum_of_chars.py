number_of_chars = int(input())
sum_of_chars = 0

for character in range(number_of_chars):
    current_character = input()
    sum_of_chars += ord(current_character)

print(f'The sum equals: {sum_of_chars}')
