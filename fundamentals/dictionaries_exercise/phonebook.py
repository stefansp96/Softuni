phonebook = {}
command = input()

while True:
    if '-' not in command:
        break

    command = command.split('-')
    name = command[0]
    phone_number = command[1]
    phonebook[name] = phone_number

    command = input()

number_of_searches = int(command)

for search in range(number_of_searches):
    current_search = input()

    if current_search not in phonebook.keys():
        print(f"Contact {current_search} does not exist.")
    else:
        print(f"{current_search} -> {phonebook[current_search]}")
