string_sequence = input().split()
new_strings = []

for word in string_sequence:
    new_word = word*len(word)
    new_strings.append(new_word)

print(''.join(new_strings))
