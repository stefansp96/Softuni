command = input()
needed_coffee = 0

while command != 'END':
    if command.lower() == 'coding' or command.lower() == 'dog' or command.lower() == 'cat' \
            or command.lower() == 'movie':
        if command.islower():
            needed_coffee += 1
        if command.isupper():
            needed_coffee += 2
    command = input()

if needed_coffee > 5:
    print('You need extra sleep')
else:
    print(needed_coffee)
