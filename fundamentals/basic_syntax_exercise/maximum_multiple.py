divisor = int(input())
boundary = int(input())
max_number = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        max_number = i

print(max_number)