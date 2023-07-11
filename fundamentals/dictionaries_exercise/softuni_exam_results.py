results = {}
submissions = {}

while True:
    command = input().split('-')

    if len(command) <= 1:
        break

    elif len(command) == 2:
        name = command[0]
        del results[name]

    elif len(command) == 3:
        name, language, points = command[0], command[1], int(command[2])

        if name not in results.keys():
            results[name] = 0

        if results[name] < points:
            results[name] = points

        if language not in submissions.keys():
            submissions[language] = 1
        else:
            submissions[language] += 1

print('Results:')
for username, result in results.items():
    print(f"{username} | {result}")
print('Submissions:')
for current_language, count in submissions.items():
    print(f"{current_language} - {count}")
