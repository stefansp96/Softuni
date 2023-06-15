to_do_notes = []
command = input()
while command != 'End':
    note = command.split('-')
    priority_index = int(note[0])
    action = note[1]
    to_do_notes.append(note)
    command = input()

result = []

sorted_notes = sorted(to_do_notes)
for char in sorted_notes:
    char.remove(char[0])
    word = ' '.join(char)
    result.append(word)

print(result)