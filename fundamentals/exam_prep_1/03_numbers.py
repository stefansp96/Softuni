number_sequence = [int(x) for x in input().split()]
average_value = sum(number_sequence) / len(number_sequence)
greater_than_average = []

for number in number_sequence:
    if number > average_value:
        greater_than_average.append(number)

greater_than_average = sorted(greater_than_average, reverse=True)

if not greater_than_average:
    print('No')
else:
    for num in range(5):
        if greater_than_average:
            print(greater_than_average.pop(0), end=' ')
