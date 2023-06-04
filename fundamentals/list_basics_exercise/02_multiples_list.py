factor = int(input())
count = int(input())
multiples_list = []

for multiplier in range(1, count + 1):
    multiple = multiplier * factor
    multiples_list.append(multiple)

print(multiples_list)
