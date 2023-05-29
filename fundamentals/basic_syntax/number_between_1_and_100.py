number = float(input())

while number < 1 or number > 100:
    if 1 < number < 100:
        break
    number = float(input())

print(f'The number {number} is between 1 and 100')