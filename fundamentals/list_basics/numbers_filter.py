n = int(input())
numbers = []
filtered_numbers = []

for num in range(n):
    current_num = int(input())
    numbers.append(current_num)

command = input()

if command == 'even':
    for number in numbers:
        if number % 2 == 0 or number == 0:
            filtered_numbers.append(number)
elif command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == 'negative':
    for number in numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == 'positive':
    for number in numbers:
        if number >= 0:
            filtered_numbers.append(number)

print(filtered_numbers)
